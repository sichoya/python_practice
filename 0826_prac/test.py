
# 람다 함수
get_max = lambda a, b: a if a>b else b
print(get_max(10, 20))  # Output: 20

cal_area = lambda w,h : w*h
print(cal_area(10, 20))  # Output: 200

# 람다 함수와 map, filter, reduce
from functools import reduce
# def square(x):
#     return x * x    
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers)) # 리스트나 항목 등에 적용할 때 사용
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # 짝수만 필터링(즉, 조건에 맞는 것만.)
print(even_numbers)  # Output: [2, 4]


sum_of_numbers = reduce(lambda x, y: x * y, numbers) # 전체 항목을 순차적으로 적용하여 하나의 값으로 축약.
print(sum_of_numbers)  # Output: 120         

# 람다 함수 예제
def apply_function(func, value):
    return func(value)
result = apply_function(lambda x: x + 10, 5)
print(result)  # Output: 15
# 람다 함수 예제
