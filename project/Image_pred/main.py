def mini_mnist():
    """
    8x8 숫자 이미지 분류 (sklearn digits 데이터셋 사용)
    """
    from sklearn.datasets import load_digits
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import confusion_matrix

    import numpy as np
    import matplotlib.pyplot as plt

    import matplotlib.font_manager as fm

    # macOS에서 한글 폰트 설정
    # Set Korean font for macOS
    plt.rcParams['font.family'] = 'AppleGothic'
    # 마이너스 기호 깨짐 방지
    # Prevent minus sign from breaking
    plt.rcParams['axes.unicode_minus'] = False
    # 데이터 로드
    digits = load_digits()
    X, y = digits.data, digits.target
    X = X / 16.0 # 정규화 (0~16 -> 0-1)

    # 원-핫 인코딩
    y_onehot = np.eye(10)[y]

    # 훈련/테스트 데이터 분할
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_onehot, test_size=0.2, random_state=42
    )
    
    
    print("미니 MNIST 과제")
    print(f"훈련 데이터: {X_train.shape}")
    print(f"테스트 데이터: {X_test.shape}")
    print(f"클래스 수: 10개 (0-9 숫자)")
    
    # TODO: 다중 클래스 분류 신경망 구현
    # 1. 입력층: 64개 (8x8 이미지)
    # 2. 은닉층: 적절한 크기
    # 3. 출력층: 10개 (0-9 숫자)
    # 4. Softmax 활성화 함수
    # 5. Cross-Entropy 손실 함수
    class DigitClassifier:
        def __init__(self, input_size=64, hidden_size=128, output_size=10, learning_rate=0.05):
            self.learning_rate = learning_rate
            # TODO: 네트워크 구조 구현
            self.learning_rate = learning_rate
            self.W1 = np.random.randn(input_size, hidden_size) * 0.01
            self.b1 = np.zeros((1, hidden_size))
            self.W2 = np.random.randn(hidden_size, output_size) * 0.01
            self.b2 = np.zeros((1, output_size))
            
        def softmax(self, z):
            # TODO: Softmax 함수 구현
            exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))
            return exp_z / np.sum(exp_z, axis=1, keepdims=True)

        def cross_entropy_loss(self, y_pred, y_true):
            # TODO: Cross-Entropy 손실 구현
            m = y_true.shape[0]
            log_likelihood = -np.log(y_pred[range(m), np.argmax(y_true, axis=1)] + 1e-9)
            return np.sum(log_likelihood) / m
            
        def forward(self, X):
            # TODO: 입력층 = 순전파
            Z1 = np.dot(X, self.W1) + self.b1
            A1 = np.maximum(0, Z1) # ReLU
            Z2 = np.dot(A1, self.W2) + self.b2
            A2 = self.softmax(Z2)
            
            # 역전파를 위해 중간 결과 저장
            self.Z1 = Z1
            self.A1 = A1
            self.A2 = A2
            return A2
            
        def backward(self, X, y):
            # TODO: 출력층 = 역전파
            m = X.shape[0]
            dZ2 = self.A2 - y
            dW2 = np.dot(self.A1.T, dZ2) / m
            db2 = np.sum(dZ2, axis=0, keepdims=True) / m
            dA1 = np.dot(dZ2, self.W2.T)
            dZ1 = dA1 * (self.Z1 > 0).astype(float)
            dW1 = np.dot(X.T, dZ1) / m
            db1 = np.sum(dZ1, axis=0, keepdims=True) / m
            
            # 가중치 업데이트
            self.W2 -= self.learning_rate * dW2
            self.b2 -= self.learning_rate * db2
            self.W1 -= self.learning_rate * dW1
            self.b1 -= self.learning_rate * db1
            
        def predict(self, X):
            # TODO: 예측 함수
            A2 = self.forward(X)
            return np.argmax(A2, axis=1)
            
        def accuracy(self, X, y):
            # TODO: 정확도 계산
            y_pred = self.predict(X)
            y_true_labels = np.argmax(y, axis=1)
            return np.mean(y_pred == y_true_labels) * 100
    
    # 모델 학습 및 평가
    model = DigitClassifier()
    epochs = 10000
    for epoch in range(epochs):
        y_pred = model.forward(X_train)
        model.backward(X_train, y_train)

    # 훈련 및 테스트 정확도 출력
    print("\n구현 후 다음을 확인하세요:")
    train_accuracy = model.accuracy(X_train, y_train)
    print(f"- 훈련 정확도: {train_accuracy:.2f}%")
    test_accuracy = model.accuracy(X_test, y_test)
    print(f"- 테스트 정확도: {test_accuracy:.2f}%")
    print("각 숫자별 예측 성능(혼동행렬 참고)")
    
    # 모델 학습 및 평가
    print("\n구현 후 다음을 확인하세요:")
    print("- 훈련 정확도: 90% 이상")
    print("- 테스트 정확도: 85% 이상")
    print("- 각 숫자별 예측 성능(혼동행렬 참고)")
    
    # 혼동 행렬 시각화
    y_test_labels = np.argmax(y_test, axis=1)
    y_pred_labels = model.predict(X_test)
    cm = confusion_matrix(y_test_labels, y_pred_labels)
    
    plt.figure(figsize=(8, 8))
    plt.matshow(cm, cmap=plt.cm.Blues, fignum=1)
    
    plt.title('Confusion Matrix')
    plt.xticks(range(10), range(10))
    plt.yticks(range(10), range(10))
    
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, format(cm[i, j], 'd'),
                    ha="center", va="center",
                    color="white" if cm[i, j] > cm.max() / 2 else "black")
    
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()
    
mini_mnist()