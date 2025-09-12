from fastapi import FastAPI

"""
단일 경로 고려하는 애플리케이션에서 주로 사용
"""
app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Hello World"
    }
# uvicorn이 하나의 엔트리 포인트만 실행할 수 있기 때문이다ㅏ.

"""
여러 함수를 사용하느 연속적인 라우트 처리는? -> APIRouter 클래스 사용 --> 다중 라우팅 허용
"""

"""
APIRouter - fastapi 패키지에 포함되어 있다. 
: 애플리케이션 라우팅과 로직을 독립적으로 구성하고 모듈화할 수 있다.
"""

