"""
리스트 컴프리헨션
: 리스트를 초기화 하는 방법 중 하나
  대괄호 안에 조건문과 반복문을 적용하여 리스트를 초기화 할 수 있음
"""
# 0부터 9까지의 수를 포함하는 리스트
array = [i for i in range(10)]
print(array)

# N X M 크기의 2차원 리스트 초기화
n = 4
m = 3
array = [[0] * m for _ in range(n)]
print(array)