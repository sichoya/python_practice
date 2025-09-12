import fastapi
print(f"FastAPI 버전: {fastapi.__version__}")
from fastapi import FastAPI
# import uvicorn
############################################

# app = FastAPI()
"""기본구조: python으로 실행 """

# @app.get("/")
# def read_root():
#     return {"message: 설치 완료"}

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port = 8000) 


# FastAPI 앱 인스턴스 생성
# Uvicorn은 이 'app' 객체를 찾아서 실행합니다.
# 출력 양식: uvicorn main:app --reload

# """ uvicorn 실행 """
# @app.get("/")
# async def read_root():
#     """
#     기본 경로('/')에 대한 API 엔드포인트입니다.
#     접속 테스트용 메시지를 반환합니다.
#     """
#     return {"message": "지금부터 Hello World API를 시작합니다."}

# @app.get("/hello")
# def say_hello():

#     return {"greeting" : "Hello World", "cafe" : "Coffee Shop"}

""" 선언적 라우팅 """

""" 전통적인 방식 - 함수 선언 후 라우팅 연동 """
# import flask
# from flask import Flask

# app = Flask(__name__)
# def get_menu():
#     return {"메뉴":"커피"}

# def create_order():
#     return {"주문":"주문완료"}

# app.add_url_rule('/menu', 'get_menu', get_menu, methods = ['GET'])
# app.add_url_rule('/order', 'create_order', create_order, methods = ['POST'])


# """ Fast API방식 """
# @app.get("/menu")
# def get_menu():
#     return {"메뉴":"커피"}

# @app.post("/order")
# def create_order():
#     return {"메시지":"주문완료"}


""" 리소스 조회 """
# app.get()

# 리소스 추가
# app.post()

# Put: 전체 리소스 수정에 활용
# Patch: 일부 필드 변경에 활용
# app.put() vs # app.patch()

# 리소스 삭제
# app.delete()


""" FastAPI HTTP 메소드 활용 """
""" Cafe 주문 시스템"""
app = FastAPI()

# GET - 메뉴보기
@app.get("/menu")
def get_menu():
    return {"메뉴":["아메리카노","라떼","카푸치노"]}

# POST - 주문하기
@app.post("/orders")
def create_order():
    return {"메시지":"주문완료", "주문번호": 1001}

# PUT - 주문 변경
@app.put("/orders/1001")
def update_order(orders_data:dict):
    return {"메시지":"주문이 수정되었습니다."}

# PUT - 주문 변경
@app.patch("/orders/1001")
def patch_order(orders_data:dict):
    return {"메시지":"주문 옵션이 변경되었습니다."}
    
# PUT - 주문 변경
@app.delete("/orders/1001")
def cancel_order():
    return {"메시지":"주문이 취소되었습니다.."}

