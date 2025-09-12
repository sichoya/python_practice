# 실행 방법(VS COde zsh)
# /bin/zsh  uvicorn cafe_api:app --reload --port 8000


"""
FastAPI를 활용한 카페 주문 관리 시스템
"""
import fastapi
print(f"FastAPI Version: {fastapi.__version__}")

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# FastAPI 앱 생성
app = FastAPI(title="Cafe Order Management API", version="1.0.0") # 최초로 만든 것이기때문에 vesion ="1.0.0" 이렇게 초기 배포 버전으로 지정.

# ------------------------------
# 데이터 모델 정의
# ------------------------------

# 메뉴 아이템 모델
# 메뉴 항목의 스키마로 요청/응답에서 자동 타입 검증.
class MenuItem(BaseModel):
    id: int
    name: str
    price: int

# 주문 요청 모델
# 클라이언트가 post/order로 보낼 때 사용되는 요청 바디 스키마 아래 두 가지를 요구함.
class OrderRequest(BaseModel):
    item_id: int
    quantity: int

# 주문 응답 모델
# 서버가 반환하는 주문의 구조: 아래 4가지항목
# Pydantic이 자동으로 타입 검사(ex. 문자열 대신 int 들어오면 Error) + docs에서 폼으로 입력 가능
class Order(BaseModel):
    id: int
    item: MenuItem
    quantity: int
    total_price: int


# ------------------------------
# 임시 데이터베이스 (메모리 기반)
# ------------------------------

menu_db = [
    MenuItem(id=1, name="Americano", price=3000),
    MenuItem(id=2, name="Latte", price=4000),
    MenuItem(id=3, name="Cappuccino", price=4500),
]

# 메모리 저장소는 프로덕션에 적합하지 않음(서버 재시작 시 데이터 사라짐, 동시성 문제 발생 가능).
# 코드 구현을 위해 만듦


orders_db: List[Order] = []
order_counter = 1  # 주문 번호 자동 증가


# ------------------------------
# 메뉴 관련 API
# ------------------------------

@app.get("/menu", response_model=List[MenuItem], tags=["Menu"])
async def get_menu():
    """
    전체 메뉴 조회 API
    - 카페의 모든 음료 메뉴를 반환합니다.
    """
    return menu_db


@app.get("/menu/{item_id}", response_model=MenuItem, tags=["Menu"])
async def get_menu_item(item_id: int):
    """
    특정 메뉴 아이템 조회 API
    - item_id에 해당하는 메뉴 정보를 반환합니다.
    """
    for item in menu_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Menu item not found")


# ------------------------------
# 주문 관련 API
# ------------------------------

@app.post("/order", response_model=Order, tags=["Order"])
async def create_order(order_request: OrderRequest):
    """
    새 주문 생성 API
    - 메뉴 ID와 수량을 입력받아 주문을 생성합니다.
    - 총 가격도 함께 계산하여 반환합니다.
    """
    global order_counter

    # 메뉴에서 해당 item 찾기
    menu_item = next((item for item in menu_db if item.id == order_request.item_id), None)
    if not menu_item:
        raise HTTPException(status_code=404, detail="Menu item not found")

    # 주문 생성
    new_order = Order(
        id=order_counter,
        item=menu_item,
        quantity=order_request.quantity,
        total_price=menu_item.price * order_request.quantity,
    )
    orders_db.append(new_order)
    order_counter += 1
    return new_order


@app.get("/order/{order_id}", response_model=Order, tags=["Order"])
async def get_order(order_id: int):
    """
    주문 상세 조회 API
    - order_id에 해당하는 주문 정보를 반환합니다.
    """
    for order in orders_db:
        if order.id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")
