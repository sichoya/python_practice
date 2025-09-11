# 1번: 'Book', 'Library', 'Member'클래스를 정의함.
# 2번: 구현한 각 클래스를 테스트 하였음.
# 3번: 테스트 예시 코드
### 1번 ###

class Book:
    """ 도서 정보 관리 클래스 """
    def __init__(self, title, author, isbn, launch_year):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._launch_year = launch_year
        self._is_available = True # 대출 가능 여부


    def __str__(self):
        return f"'{self._title}' by {self._author} ({self._launch_year}) -ISBN: {self._isbn}"
    
    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @property
    def isbn(self):
        return self._isbn
    
    @property
    def launch_year(self):
        return self._launch_year
    
    @property
    def is_available(self):
        return self._is_available

    @is_available.setter
    def is_available(self, status):
        if isinstance(status, bool):
            self._is_available = status
        else:
            raise TypeError("대출 가능 상태는 boolean 값이어야 합니다.")


class Member:
    """ 도서관 회원 정보 및 대출 목록을 관리하는 클래스 """
    def __init__(self, name, member_id):
        self._name = name
        self._member_id = member_id
        self._borrowed_books = [] # 대출목록

    def __str__(self):
        return f"회원: {self._name} (ID: {self._member_id})"
    
    @property
    def name(self):
        return self._name
    
    @property
    def member_id(self):
        return self._member_id
    
    @property
    def borrowed_books(self):
        return self._borrowed_books
    
    def borrow_book(self, book):
        if book not in self._borrowed_books:
            self._borrowed_books.append(book)
            return True #, f" {self.name}님, '{book.title}' 대출이 완료되었습니다."
        else:
            return False #, f" {self.name}님, 이미 '{book.title}' 대출중입니다."
            


    def return_book(self, book):
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
            return True #, f" {self.name}님, '{book.title}' 반납이 완료되었습니다."
        else:
            return False #, f" {self.name}님, 대출 목록에 '{book.title}'이(가) 없습니다." 


from abc import ABC, abstractmethod

class SearchStrategy(ABC):
    """검색 전략의 기본 인터페이스"""
    @abstractmethod
    def search(self, books, query):
        pass


class TitleSearchStrategy(SearchStrategy):
    """제목 검색 전략"""
    def search(self, books, query):
        return [book for book in books.values() 
                if query.lower() in book.title.lower()]

class AuthorSearchStrategy(SearchStrategy):
    """저자 검색 전략"""
    def search(self, books, query):
        return [book for book in books.values() 
                if query.lower() in book.author.lower()]

class ISBNSearchStrategy(SearchStrategy):
    """ISBN 검색 전략"""
    def search(self, books, query):
        return [books[query]] if query in books else []

class Library:
    """도서관 시스템의 주요 기능을 관리하는 클래스"""
    def __init__(self, search_strategies=None):
        self._books = {}    # isbn을 키로 하는 도서 딕셔너리
        self._members = {}  # 회원 ID를 키로 하는 회원 딕셔너리
        # 🎯 DI 패턴: 외부에서 전략 주입 가능, 기본값으로 호환성 유지
        self._search_strategies = search_strategies or self._create_default_strategies()
    
    def _create_default_strategies(self):
        """기본 검색 전략들 생성"""
        return {
            "title": TitleSearchStrategy(),
            "author": AuthorSearchStrategy(),
            "isbn": ISBNSearchStrategy()}

    # 도서 관리
    def add_book(self, book):
        if isinstance(book, Book) and book.isbn not in self._books:
            self._books[book.isbn] = book
            print(f"도서 추가: {book}")
        else:
            print(f"오류: '{book.title}' (isbn: {book.isbn}) 도서가 이미 존재하거나 잘못된 객체입니다.")

    def remove_book(self, isbn):
        if isbn in self._books:
            book_to_remove = self._books.pop(isbn)
            print(f"도서 삭제: {book_to_remove}")
            return True
        print("오류: 해당 isbn의 도서가 없습니다.")
        return False

    # 도서 검색 (개방-폐쇄 원칙 적용)
    # def search_books(self, query, search_type="title"):
    #     results = []
    #     if search_type == "title":
    #         results = [book for book in self._books.values() if query.lower() in book.title.lower()]
    #     elif search_type == "author":
    #         results = [book for book in self._books.values() if query.lower() in book.author.lower()]
    #     elif search_type == "isbn":
    #         if query in self._books:
    #             results.append(self._books[query])
    #     else:
    #         print("오류: 유효하지 않은 검색 유형입니다. (title, author, isbn 중 선택)")
    #     return results



    def search_books(self, query, search_type="title"):
        if search_type in self._search_strategies:
            strategy = self._search_strategies[search_type]
            return strategy.search(self._books, query)
        else:
            available_types = ", ".join(self._search_strategies.keys())
            print(f"오류: 유효하지 않은 검색 유형입니다. ({available_types} 중 선택)")
            return []



    # 회원 관리
    def register_member(self, member):
        if isinstance(member, Member) and member.member_id not in self._members:
            self._members[member.member_id] = member
            print(f"회원 등록: {member}")
        else:
            print("오류: 회원 ID가 이미 존재하거나 잘못된 객체입니다.")

    # 대출/반납 기능
    def borrow_book(self, member_id, isbn):
        if member_id in self._members and isbn in self._books:
            member = self._members[member_id]
            book = self._books[isbn]
            if book.is_available:
                if member.borrow_book(book):
                    book.is_available = False
                    print(f"'{member.name}'님이 '{book.title}'을(를) 대출했습니다.")
                else:
                    print("오류: 이미 대출한 도서입니다.")
            else:
                print("오류: 해당 도서는 이미 대출 중입니다.")
        else:
            print("오류: 회원 ID 또는 도서 isbn을 찾을 수 없습니다.")

    def return_book(self, member_id, isbn):
        if member_id in self._members and isbn in self._books:
            member = self._members[member_id]
            book = self._books[isbn]
            if not book.is_available:
                if member.return_book(book):
                    book.is_available = True
                    print(f"'{member.name}'님이 '{book.title}'을(를) 반납했습니다.")
                else:
                    print("오류: 대출 목록에 해당 도서가 없습니다.")
            else:
                print("오류: 해당 도서는 이미 반납된 상태입니다.")
        else:
            print("오류: 회원 ID 또는 도서 isbn을 찾을 수 없습니다.")

    # 회원별 대출 현황
    def get_borrowed_status(self, member_id):
        if member_id in self._members:
            member = self._members[member_id]
            borrowed_list = member.borrowed_books
            if borrowed_list:
                print(f"\n--- '{member.name}'님의 대출 현황 ---")
                for book in borrowed_list:
                    print(f"- {book}")
            else:
                print(f"\n'{member.name}'님은 대출한 도서가 없습니다.")
        else:
            print("오류: 존재하지 않는 회원 ID입니다.")

### 2번 ###
## -- 사용해보기 --##

if __name__ == "__main__":
    # Library 객체 생성
    my_library = Library()

    # 요청하신 도서들로 Book 객체 생성 및 추가
    # 실제 ISBN과 출판 연도는 임의로 작성되었습니다.
    book1 = Book("혼모노", "성해나", "978-89-6014-411-1", 2021)
    book2 = Book("안녕이라 그랬어", "김애란", "978-89-546-2182-0", 2013)
    book3 = Book("소년이 온다", "한강", "978-89-364-3424-6", 2014)

    print("--- 도서 추가 ---")
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)
    print("\n" + "="*40 + "\n")

    # 기존 회원 이름으로 Member 객체 생성 및 등록
    member1 = Member("병직", "M001")
    member2 = Member("지우", "M002")
    member3 = Member("태수", "M003")

    print("--- 회원 등록 ---")
    my_library.register_member(member1)
    my_library.register_member(member2)
    my_library.register_member(member3)
    print("\n" + "="*40 + "\n")

    # 도서 검색 기능 테스트
    print("--- '소년이 온다' 제목으로 검색 ---")
    results_title = my_library.search_books("소년이 온다", "title")
    for result in results_title:
        print(result)

    print("\n--- '김애란' 저자 이름으로 검색 ---")
    results_author = my_library.search_books("김애란", "author")
    for result in results_author:
        print(result)
    print("\n" + "="*40 + "\n")

    # 도서 대출 및 반납 기능 테스트
    print("--- 도서 대출 시도 ---")
    my_library.borrow_book("M001", book2.isbn)  # 병직이 '안녕이라 그랬어' 대출
    my_library.borrow_book("M002", book3.isbn)  # 지우가 '소년이 온다' 대출
    my_library.borrow_book("M001", book2.isbn)  # 이미 대출한 책을 다시 대출 시도 (실패)

    print("\n--- 회원별 대출 현황 확인 ---")
    my_library.get_borrowed_status("M001")
    my_library.get_borrowed_status("M002")

    print("\n" + "="*40 + "\n")

    print("--- 도서 반납 시도 ---")
    my_library.return_book("M001", book2.isbn)  # 병직이 '안녕이라 그랬어' 반납
    my_library.get_borrowed_status("M001") # 반납 후 현황 확인

    print("\n" + "="*40 + "\n")

    # 도서 삭제 기능 테스트
    print("--- 도서 삭제 시도 ---")
    my_library.remove_book(book1.isbn)
    my_library.remove_book("non-existent-isbn") # 없는 ISBN 삭제 시도 (실패)


### 3번 ###
## -- 사용예시 코드 --##
##  아래코드부터 가장 하단에 있는 코드 전까지 주석을 풀고 예시에 맞게 실행하면 됩니다.

if __name__ == "__main__":
     # Library 클래스의 인스턴스(객체)를 생성합니다.
     my_library = Library()

     # --- 도서 데이터 준비 ---
     # 실제 도서 정보를 담을 Book 객체들을 생성하세요.
     # 예: book1 = Book("제목1", "저자1", "ISBN1", 2023)
     book1 = ...
     book2 = ...
     book3 = ...
    
     # 생성된 도서 객체들을 도서관에 추가합니다.
     print("--- 도서 추가 ---")
     my_library.add_book(book1)
     my_library.add_book(book2)
     my_library.add_book(book3)
     print("\n" + "="*40 + "\n")

     # --- 회원 데이터 준비 ---
     # 실제 회원 정보를 담을 Member 객체들을 생성하세요.
     # 예: member1 = Member("이름1", "ID1")
     member1 = ...
     member2 = ...
    
     # 생성된 회원 객체들을 도서관에 등록합니다.
     print("--- 회원 등록 ---")
     my_library.register_member(member1)
     my_library.register_member(member2)
     print("\n" + "="*40 + "\n")

     # --- 기능 테스트 ---
     print("--- 도서 검색 기능 테스트 ---")
     # 원하는 검색 조건으로 도서를 검색하고 결과를 출력합니다.
     # 예: my_library.search_books("검색어", "title")
     print("--- 제목으로 검색 ---")
     results_title = my_library.search_books("...", "title")
     for result in results_title:
         print(result)

     print("\n--- 저자명으로 검색 ---")
     results_author = my_library.search_books("...", "author")
     for result in results_author:
         print(result)
     print("\n" + "="*40 + "\n")

     # --- 대출 및 반납 테스트 ---
     print("--- 도서 대출 시도 ---")
     # 대출을 원하는 회원 ID와 도서 ISBN을 넣어 대출을 시도합니다.
     # 예: my_library.borrow_book("ID1", "ISBN1")
     my_library.borrow_book("...", "...")
     my_library.borrow_book("...", "...")
     print("\n" + "="*40 + "\n")
    
     print("--- 도서 반납 시도 ---")
     # 반납을 원하는 회원 ID와 도서 ISBN을 넣어 반납을 시도합니다.
     my_library.return_book("...", "...")
     print("\n" + "="*40 + "\n")

     # --- 도서 삭제 테스트 ---
     print("--- 도서 삭제 시도 ---")
     # 삭제를 원하는 도서의 ISBN을 넣어 도서를 삭제합니다.
     # 예: my_library.remove_book("ISBN1")
     my_library.remove_book("...")
     my_library.remove_book("...") # 존재하지 않는 도서 삭제 시도

## 
