from typing import List
from models import MenuItem, BeverageSize

# 메뉴 데이터베이스
menu_db: List[MenuItem] = [
    # 콜드브루 커피
    MenuItem(
        id=1,
        name="나이트로 바닐라 크림",
        category="콜드브루 커피",
        subcategory="나이트로 바닐라 크림",
        sizes=[BeverageSize(name="Grande", price=6100)]
    ),
    MenuItem(
        id=2,
        name="돌체 콜드 브루",
        category="콜드브루 커피",
        subcategory="돌체 콜드 브루",
        sizes=[BeverageSize(name="Tall", price=5800), BeverageSize(name="Grande", price=6300), BeverageSize(name="Venti", price=6800)]
    ),
    MenuItem(
        id=3,
        name="제주 비자림 리저브 콜드 브루",
        category="콜드브루 커피",
        subcategory="제주 비자림 리저브 콜드 브루",
        sizes=[BeverageSize(name="Tall", price=6500), BeverageSize(name="Grande", price=7000), BeverageSize(name="Venti", price=7500)]
    ),
    MenuItem(
        id=4,
        name="콜드 브루",
        category="콜드브루 커피",
        subcategory="콜드 브루",
        sizes=[BeverageSize(name="Tall", price=4900), BeverageSize(name="Grande", price=5400), BeverageSize(name="Venti", price=5900)]
    ),
    MenuItem(
        id=5,
        name="리저브 콜드 브루",
        category="콜드브루 커피",
        subcategory="리저브 콜드 브루",
        sizes=[BeverageSize(name="Tall", price=5900), BeverageSize(name="Grande", price=6400)]
    ),

    # 에스프레소
    MenuItem(
        id=6,
        name="프렌치 바닐라 라떼",
        category="에스프레소",
        subcategory="프렌치 바닐라 라떼",
        sizes=[BeverageSize(name="Tall", price=5200), BeverageSize(name="Grande", price=5700), BeverageSize(name="Venti", price=6200)]
    ),
    MenuItem(
        id=7,
        name="에스프레소 마키아또",
        category="에스프레소",
        subcategory="에스프레소 마키아또",
        sizes=[BeverageSize(name="Tall", price=3600), BeverageSize(name="Grande", price=4100)]
    ),
    MenuItem(
        id=8,
        name="카페 아메리카노",
        category="에스프레소",
        subcategory="카페 아메리카노",
        sizes=[BeverageSize(name="Tall", price=4500), BeverageSize(name="Grande", price=5000), BeverageSize(name="Venti", price=5500)]
    ),
    MenuItem(
        id=9,
        name="아이스 카페 아메리카노",
        category="에스프레소",
        subcategory="아이스 카페 아메리카노",
        sizes=[BeverageSize(name="Tall", price=4500), BeverageSize(name="Grande", price=5000), BeverageSize(name="Venti", price=5500)]
    ),
    MenuItem(
        id=10,
        name="헤이즐넛 오트 아이스 쉐이큰 에스프레소",
        category="에스프레소",
        subcategory="헤이즐넛 오트 아이스 쉐이큰 에스프레소",
        sizes=[BeverageSize(name="Grande", price=6100)]
    ),
    MenuItem(
        id=11,
        name="아이스 카푸치노",
        category="에스프레소",
        subcategory="아이스 카푸치노",
        sizes=[BeverageSize(name="Tall", price=5000), BeverageSize(name="Grande", price=5500), BeverageSize(name="Venti", price=6000)]
    ),
    MenuItem(
        id=12,
        name="카푸치노",
        category="에스프레소",
        subcategory="카푸치노",
        sizes=[BeverageSize(name="Tall", price=5000), BeverageSize(name="Grande", price=5500), BeverageSize(name="Venti", price=6000)]
    ),
    MenuItem(
        id=13,
        name="카라멜 마키아또",
        category="에스프레소",
        subcategory="카라멜 마키아또",
        sizes=[BeverageSize(name="Tall", price=5900), BeverageSize(name="Grande", price=6400), BeverageSize(name="Venti", price=6900)]
    ),
    MenuItem(
        id=14,
        name="아이스 카라멜 마키아또",
        category="에스프레소",
        subcategory="아이스 카라멜 마키아또",
        sizes=[BeverageSize(name="Tall", price=5900), BeverageSize(name="Grande", price=6400), BeverageSize(name="Venti", price=6900)]
    ),
    MenuItem(
        id=15,
        name="바닐라 빈 라떼",
        category="에스프레소",
        subcategory="바닐라 빈 라떼",
        sizes=[BeverageSize(name="Tall", price=5600), BeverageSize(name="Grande", price=6100), BeverageSize(name="Venti", price=6600)]
    ),
    MenuItem(
        id=16,
        name="아이스 바닐라 빈 라떼",
        category="에스프레소",
        subcategory="아이스 바닐라 빈 라떼",
        sizes=[BeverageSize(name="Tall", price=5600), BeverageSize(name="Grande", price=6100), BeverageSize(name="Venti", price=6600)]
    ),

    # 프라푸치노
    MenuItem(
        id=17,
        name="자몽 망고 코코 프라푸치노",
        category="프라푸치노",
        subcategory="자몽 망고 코코 프라푸치노",
        sizes=[BeverageSize(name="Grande", price=6800)]
    ),
    MenuItem(
        id=18,
        name="카페 브륄레 프라푸치노",
        category="프라푸치노",
        subcategory="카페 브륄레 프라푸치노",
        sizes=[BeverageSize(name="Tall", price=5900), BeverageSize(name="Grande", price=6400), BeverageSize(name="Venti", price=6900)]
    ),
    MenuItem(
        id=19,
        name="자바 칩 프라푸치노",
        category="프라푸치노",
        subcategory="자바 칩 프라푸치노",
        sizes=[BeverageSize(name="Tall", price=6300), BeverageSize(name="Grande", price=6800), BeverageSize(name="Venti", price=7300)]
    ),
    MenuItem(
        id=20,
        name="인절미 제주 말차 크림 프라푸치노",
        category="프라푸치노",
        subcategory="인절미 제주 말차 크림 프라푸치노",
        sizes=[BeverageSize(name="Grande", price=6800)]
    ),
    MenuItem(
        id=21,
        name="제주 말차 크림 프라푸치노",
        category="프라푸치노",
        subcategory="제주 말차 크림 프라푸치노",
        sizes=[BeverageSize(name="Grande", price=6300)]
    ),
    MenuItem(
        id=22,
        name="초콜릿 크림 칩 프라푸치노",
        category="프라푸치노",
        subcategory="초콜릿 크림 칩 프라푸치노",
        sizes=[BeverageSize(name="Tall", price=5900), BeverageSize(name="Grande", price=6400), BeverageSize(name="Venti", price=6900)]
    ),

    # 블렌디드
    MenuItem(
        id=23,
        name="피치 망고 선셋 블렌디드",
        category="블렌디드",
        subcategory="피치 망고 선셋 블렌디드",
        sizes=[BeverageSize(name="Grande", price=6800)]
    ),
    MenuItem(
        id=24,
        name="딸기 딜라이트 요거트 블렌디드",
        category="블렌디드",
        subcategory="딸기 딜라이트 요거트 블렌디드",
        sizes=[BeverageSize(name="Grande", price=6200)]
    ),
    MenuItem(
        id=25,
        name="피치 망고 블렌디드",
        category="블렌디드",
        subcategory="피치 망고 블렌디드",
        sizes=[BeverageSize(name="Tall", price=6300), BeverageSize(name="Grande", price=6800), BeverageSize(name="Venti", price=7300)]
    ),

    # 스타벅스 피지오
    MenuItem(
        id=26,
        name="쿨 라임 피지오",
        category="스타벅스 피지오",
        subcategory="쿨 라임 피지오",
        sizes=[BeverageSize(name="Tall", price=5900), BeverageSize(name="Grande", price=6400)]
    ),
    MenuItem(
        id=27,
        name="라이트 핑크 자몽 피지오",
        category="스타벅스 피지오",
        subcategory="라이트 핑크 자몽 피지오",
        sizes=[BeverageSize(name="Tall", price=5900), BeverageSize(name="Grande", price=6400)]
    ),

    # 티
    MenuItem(
        id=28,
        name="아이스 얼그레이 티",
        category="티",
        subcategory="아이스 얼그레이 티",
        sizes=[BeverageSize(name="Tall", price=4500), BeverageSize(name="Grande", price=5000), BeverageSize(name="Venti", price=5500)]
    ),
    MenuItem(
        id=29,
        name="복숭아 아이스 티",
        category="티",
        subcategory="복숭아 아이스 티",
        sizes=[BeverageSize(name="Tall", price=5800), BeverageSize(name="Grande", price=6300), BeverageSize(name="Venti", price=6800)]
    ),
    MenuItem(
        id=30,
        name="복숭아 핫 티",
        category="티",
        subcategory="복숭아 핫 티",
        sizes=[BeverageSize(name="Tall", price=5800), BeverageSize(name="Grande", price=6300), BeverageSize(name="Venti", price=6800)]
    ),
    MenuItem(
        id=31,
        name="아이스 자몽 허니 블랙 티",
        category="티",
        subcategory="아이스 자몽 허니 블랙 티",
        sizes=[BeverageSize(name="Tall", price=5700), BeverageSize(name="Grande", price=6200), BeverageSize(name="Venti", price=6700)]
    ),
    MenuItem(
        id=32,
        name="스타벅스 클래식 밀크 티",
        category="티",
        subcategory="스타벅스 클래식 밀크 티",
        sizes=[BeverageSize(name="Tall", price=5100), BeverageSize(name="Grande", price=5600), BeverageSize(name="Venti", price=6100)]
    )
]

# 주문 데이터를 저장할 리스트
orders_db: List = []
order_counter = 1 # 주문 번호 자동 증가