from pydantic import BaseModel
from typing import List, Optional

# MenuItem, BeverageSize --> database.py


# 음료 사이즈 모델
# 음료가 가질 수 있는 다양한 사이즈와 가격을 정의합니다.
class BeverageSize(BaseModel):
    name: str  # 예: "Tall", "Grande", "Venti"
    price: int # 사이즈에 따른 가격

# 메뉴 아이템 모델
# 개별 메뉴 항목의 스키마입니다. 카테고리, 서브카테고리, 그리고 여러 사이즈 정보를 포함합니다.
class MenuItem(BaseModel):
    id: int
    name: str
    category: str
    subcategory: str
    sizes: List[BeverageSize] # 여러 BeverageSize 객체들을 리스트로 가집니다.
    description: Optional[str] = None # 메뉴에 대한 선택적 설명

# 주문 요청 모델
# 클라이언트가 주문을 생성할 때 보내는 데이터의 스키마입니다.
class OrderRequest(BaseModel):
    item_id: int        # 주문할 메뉴의 ID
    size_name: str      # 주문할 음료의 사이즈 이름 (예: "Grande")
    quantity: int       # 주문 수량

# 주문 응답 모델
# 서버가 주문 생성 후 반환하는 데이터의 스키마입니다.
class Order(BaseModel):
    id: int             # 생성된 주문의 고유 ID
    item: MenuItem      # 주문한 메뉴 아이템 정보
    size: str           # 주문한 사이즈
    quantity: int       # 주문 수량
    total_price: int    # 총 주문 가격 (수량 * 사이즈 가격)