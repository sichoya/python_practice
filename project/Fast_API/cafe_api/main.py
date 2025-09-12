import fastapi
print(f"FastAPI Version: {fastapi.__version__}")

from fastapi import FastAPI, HTTPException
from typing import List

# models.py에서 가져옴.
from models import MenuItem, Order, OrderRequest

# database.py에서 가져옴.
from database import menu_db, orders_db, order_counter

# FastAPI 앱 생성
# API 문서의 제목과 버전을 지정합니다.
app = FastAPI(title="Cafe Order Management API", version="1.0.0") # 초기 배포 버전 정의함.

# ------------------------------
# 메뉴 관련 API (Tags로 그룹화)
# ------------------------------

@app.get("/menu", response_model=List[MenuItem], tags=["Menu"])
async def get_menu():
    """
    **전체 메뉴 조회 API**
    - 카페의 모든 음료 메뉴를 카테고리별로 분류하여 반환합니다.
    - 메뉴의 이름, 카테고리, 서브카테고리, 사이즈별 가격 정보를 포함합니다.
    """
    return menu_db

@app.get("/menu/{item_id}", response_model=MenuItem, tags=["Menu"])
async def get_menu_item(item_id: int):
    """
    **특정 메뉴 아이템 조회 API**
    - item_id에 해당하는 메뉴 정보를 반환합니다.
    - 찾는 메뉴가 없을 경우 404 에러를 반환합니다.
    """
    for item in menu_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Menu item not found")

# ------------------------------
# 주문 관련 API (Tags로 그룹화)
# ------------------------------

@app.post("/order", response_model=Order, tags=["Order"])
async def create_order(order_request: OrderRequest):
    """
    **새 주문 생성 API**
    - 메뉴 ID, 사이즈 이름, 수량을 입력받아 주문을 생성합니다.
    - 선택한 사이즈의 총 가격을 계산하여 반환합니다.
    - 메뉴 아이템 또는 사이즈가 존재하지 않으면 404 에러를 반환합니다.
    """
    global order_counter

    # 요청된 메뉴 ID로 메뉴 아이템 찾기
    menu_item = next((item for item in menu_db if item.id == order_request.item_id), None)
    if not menu_item:
        raise HTTPException(status_code=404, detail="Menu item not found")

    # 선택한 사이즈의 가격 찾기
    selected_size = next((size for size in menu_item.sizes if size.name.lower() == order_request.size_name.lower()), None)
    if not selected_size:
        raise HTTPException(status_code=404, detail=f"Size '{order_request.size_name}' not available for this item")

    # 새로운 주문 객체 생성
    new_order = Order(
        id=order_counter,
        item=menu_item,
        size=selected_size.name,
        quantity=order_request.quantity,
        total_price=selected_size.price * order_request.quantity,
    )
    # 주문 데이터를 메모리에 저장
    orders_db.append(new_order)
    order_counter += 1
    return new_order

@app.get("/order/{order_id}", response_model=Order, tags=["Order"])
async def get_order(order_id: int):
    """
    **주문 상세 조회 API**
    - order_id에 해당하는 주문 정보를 반환합니다.
    - 해당 주문이 존재하지 않으면 404 에러를 반환합니다.
    """
    for order in orders_db:
        if order.id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")