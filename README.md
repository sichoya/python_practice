# python_practice
## AIaaS를 위한 머신러닝&AI 학습 프로젝트

> 이 저장소는 다양한 파이썬 프로젝트와 기초 연습 코드를 포함하고 있습니다.


## 📈 학습 진행도

- [o] Python 기초 및 심화 (100%)
- [o] 도서관 관리 시스템 (100%)
- [x] 파일 처리 시스템 (진행중)
- [o] OCR 구현 (100%)
- [o] 이미지 분류 (100%)
- [o] 컴퓨터 비전 기초 (100%)
- [x] 챗봇 구현 (진행중)
- [o] FastAPI 서버 (100%)

## 📁 디렉터리 구조

```plaintext
~/Python/
├── project/                     # 메인 프로젝트 (Python 3.12)
│   ├── Computer_Vision/         # 컴퓨터 비전 ✅ [완료] (Python 3.12)
│   │   └── Vision_prac.ipynb    # 비전 실습 노트북
│   ├── image_pred/              # 이미지 분류 ✅ [완료] (Python 3.12)
│   │   ├── confusion_matrix_result.png  # 성능 평가 결과
│   │   ├── hyperparameter.txt           # 하이퍼파라미터 설정
│   │   └── main.py                      # 메인 실행 파일
│   ├── ChatBot/                 # 챗봇 프로젝트 🔄 [진행중] (Python 3.12)
│   ├── Fast_API/                # API 서버 ✅ [완료] (Python 3.12)
│   │   ├── cafe_api/            # 카페 주문 시스템
│   │   │   ├── cafe_api.py      # 메인 API 애플리케이션
│   │   │   ├── database.py      # 데이터베이스 연결 및 설정
│   │   │   ├── main.py          # 서버 실행 파일
│   │   │   ├── models.py        # 데이터 모델 정의
│   │   │   └── process.txt      # 프로세스 문서
│   │   └── practice_api/        # API 실습
│   │       ├── api.py           # API 엔드포인트
│   │       ├── apirouter.py     # 라우터 설정
│   │       ├── test_main.py     # 테스트 파일
│   │       └── todo.py          # To-Do 기능 구현
│   └── OCR/                     # 문자인식 ✅ [완료] (Python 3.9)
│       ├── high_quality_image.png       # 고품질 테스트 이미지
│       ├── low_quality_image.png        # 저품질 테스트 이미지
│       ├── medium_quality_image.png     # 중품질 테스트 이미지
│       ├── practice_OCR.ipynb           # OCR 실습 노트북
│       └── sample_image.png             # 샘플 이미지
│
├── basic/                       # 기초 학습 (Python 3.12)
│   ├── 0826_prac/               # 기초 환경 ✅ [완료] (Python 3.12)
│   │   ├── binary_data.bin      # 바이너리 데이터 처리
│   │   ├── new_data.csv         # CSV 데이터 처리
│   │   ├── levelup.ipynb        # 기초 실습 노트북
│   │   └── test.py              # 기초 테스트 스크립트
│   ├── 0827_prac/               # 심화 환경 ✅ [완료] (Python 3.12)
│   │   └── 0827.ipynb           # 심화 실습 노트북
│   ├── Library/                 # 도서관리서비스 ✅ [완료] (Python 3.12)
│   │   ├── Library.py           # 도서관 시스템 메인 모듈
│   │   ├── li_test.py           # 시스템 테스트
│   │   ├── Library_test.ipynb   # 테스트 노트북
│   │   └── Library예제_설명.txt  # 시스템 설명서
│   └── File_p/                  # 파일처리기 🔄 [진행중] (Python 3.12)
│       ├── ex_file.csv          # 파일 처리 예제
│       └── File_sys.ipynb       # 파일 시스템 구현
│
├── txt/                         # 환경 설정 파일
│   ├── requirements39.txt       # Python 3.9 의존성
│   └── requirements312.txt      # Python 3.12 의존성
│
├── setup_conda_envs.sh          # Conda 환경 설정 스크립트
└── README.md                    # 프로젝트 문서
```

## ⚙️ 개발 환경

| 구분 | 상세 정보 |
|------|-----------|
| **OS** | macOS |
| **IDE** | VS Code |
| **Python** | 3.9 (OCR), 3.12 (나머지 프로젝트) |
| **가상환경** | Conda |
| **주요 라이브러리** | TensorFlow, FastAPI, OpenCV, scikit-learn, pandas, numpy |


## 가상환경

ocr_projects           /opt/miniconda3/envs/ocr_projects    (Python 3.9)

python_main            /opt/miniconda3/envs/python_main     (Python 3.12)

## ⚙️ 초기 환경 설정 방법

각 프로젝트에 필요한 Conda 가상 환경은 `setup_conda_envs.sh` 스크립트를 실행하여 자동으로 설정할 수 있습니다. 이 스크립트는 프로젝트별로 다른 파이썬 버전을 관리합니다.



### 개별 프로젝트 실행

#### 📖 도서관 관리 시스템
```bash
cd basic/Library/
python Library.py
# 또는 Jupyter 노트북으로 실행
jupyter notebook Library_test.ipynb
```

#### 🔍 OCR 프로젝트
```bash
conda activate py39  # Python 3.9 환경 활성화
cd project/OCR/
jupyter notebook practice_OCR.ipynb
```

#### 🖼️ 이미지 분류
```bash
cd project/image_pred/
python main.py
```

#### 👁️ 컴퓨터 비전
```bash
cd project/Computer_Vision/
jupyter notebook Vision_prac.ipynb
```

#### ⚡ FastAPI 서버
```bash
# 카페 주문 시스템
cd project/Fast_API/cafe_api/
uvicorn main:app --reload

# API 실습 서버
cd project/Fast_API/practice_api/
python api.py
```

서버 실행 후 브라우저에서 `http://localhost:8000/docs` 접속하여 API 문서 확인

## 📊 주요 성과물

### ✅ 완료된 프로젝트

#### 1. **도서관 관리 시스템**
- 완전한 CRUD 시스템 구축
- 객체지향 프로그래밍 적용
- 도서 대여/반납 로직 구현

#### 2. **OCR (광학 문자 인식)**
- 다양한 품질의 이미지 처리 성공
- 전처리부터 텍스트 추출까지 완전 구현
- Python 3.9 환경에서 안정적 동작

#### 3. **이미지 분류 시스템**
- Confusion Matrix 기반 성능 평가 완료
- 하이퍼파라미터 튜닝 적용
- 모델 성능 시각화 구현

#### 4. **컴퓨터 비전 기초**
- 이미지 처리 기법 습득
- OpenCV 활용한 실시간 처리
- 다양한 비전 알고리즘 실습

#### 5. **FastAPI 서버**
- **카페 주문 시스템**: 주문 관리, 데이터베이스 연동
- **실습 API**: RESTful API 설계 및 구현
- **To-Do 시스템**: 작업 관리 API


### 🔄 진행 중인 프로젝트

#### 1. **파일 처리 시스템** (진행중)
- 다양한 파일 형식 처리 (CSV, Binary, Text)
- 예외 처리 및 로깅 시스템
- 체계적인 파일 관리 구조


#### 2. **ChatBot 시스템** (진행중)
- 자연어 처리 기반 대화 시스템
- 의도 분석 및 응답 생성
- 머신러닝 기반 학습 구조


## 🛠️ 기술 스택

### Backend
- **Python**: 메인 개발 언어
- **FastAPI**: 고성능 웹 API 프레임워워크
- **SQLAlchemy**: ORM 및 데이터베이스 관리

### AI/ML
- **TensorFlow/Keras**: 딥러닝 모델 개발
- **scikit-learn**: 머신러닝 알고리즘
- **OpenCV**: 컴퓨터 비전 처리
- **pandas/numpy**: 데이터 분석 및 처리

### Development Tools
- **Jupyter Notebook**: 실험 및 프로토타이핑
- **VS Code**: 메인 IDE
- **Conda**: 환경 관리
- **Git**: 버전 관리

## 📝 학습 노트

### Python 기초 → 심화
1. **기본 문법**: 변수, 함수, 클래스, 제어문
2. **고급 기능**: 파일 처리, 예외 처리, 모듈화
3. **객체지향**: 상속, 캡슐화, 다형성 적용

### AI/ML 실습
1. **데이터 처리**: pandas를 활용한 데이터 전처리
2. **모델 구현**: 직접 구현을 통한 원리 이해
3. **성능 평가**: 다양한 메트릭을 통한 모델 평가

### 웹 개발
1. **API 설계**: RESTful 원칙 준수
2. **데이터베이스**: 관계형 DB 설계 및 연동
3. **테스팅**: 단위 테스트 및 API 테스트

## 🎯 다음 목표

- [ ] 파일처리기 생성
- [ ] ChatBot 프로젝트 완성
- [ ] FastAPI 서버 배포 (Docker) (미정)
- [ ] 프로젝트 간 통합 시스템 구축
- [ ] 클라우드 배포 (AWS/GCP)
- [ ] CI/CD 파이프라인 구축

---

*Last Updated: 2025년 진행중*