# http://127.0.0.1:8000/docs
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class MenuResponse(BaseModel):
    메뉴: List[str]

class OrderResponse(BaseModel):
    메시지: str
    주문번호: int | None = None

@app.get("/menu", response_model=MenuResponse)
def get_menu():
    return {"메뉴": ["아메리카노", "라떼", "카푸치노"]}

@app.post("/orders", response_model=OrderResponse)
def create_order():
    return {"메시지": "주문완료", "주문번호": 1001}

@app.put("/orders/1001", response_model=OrderResponse)
def update_order(orders_data: dict):
    return {"메시지": "주문이 수정되었습니다."}

@app.patch("/orders/1001", response_model=OrderResponse)
def patch_order(orders_data: dict):
    return {"메시지": "주문 옵션이 변경되었습니다."}

@app.delete("/orders/1001", response_model=OrderResponse)
def cancel_order():
    return {"메시지": "주문이 취소되었습니다."}
