"""
< 실전에서 유용한 표준 라이브러리 >

1. 내장 함수: 기본 입출력 함수 부터 정렬 함수까지 기본적인 함수들을 제공
            파이썬 프로그램을 작성할 때 없어서는 안 되는 필수적인 기능을 포함하고 있음

2. itertools: 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들을 제공
                특히 순열의 조합 라이브러리는 코딩 테스트에서 자주 사용됨

3. heapq: 힙(Heap) 자료구조를 제공
          일반적으로 우선순위 큐 기능을 구현하기 위해 사용

4. bisect: 이진 탐색(Binary Search) 기능을 제공

5. collections: 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함

6. math: 필수적인 수학적 기능을 제공함
         팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함
"""


"""
<순열과 조합>
 순열: 서로 다른 𝑛개에서 서로 다른 𝑟개를 선택하여 일렬로 나열하는 것
    {'A', 'B', 'C'}에서 세 개를 선택하여 나열하는 경우
    : 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'
"""

from itertools import permutations

data = ['A', 'B', 'C'] # 데이터 준비

result = list(permutations(data, 3)) # 모든 순열 구하기
print(result)

"""
<순열과 조합>

조합: 서로 다른 𝑛개에서 순서에 상관 없이 서로 다른 𝑟개를 선택하는 것
    {'A', 'B', 'C'}에서 순서를 고려하지 않고 두 개를 뽑는 경우
    : 'AB', 'AC', 'BC'
"""
from itertools import combinations

data = ['A', 'B', 'C'] # 데이터 준비

result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기
print(result)

"""
-------------중복순열과 중복조합--------------------
"""
# 중복 순열
from itertools import product

data = ['A', 'B', 'C'] # 데이터 준비

result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print('> 2개를 뽑는 모든 순열 구하기 (중복 허용)')
print(result)

# 중복 조합
from itertools import combinations_with_replacement

data = ['A', 'B', 'C'] # 데이터 준비

result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print('> 2개를 뽑는 모든 조합 구하기 (중복 허용)')
print(result)

"""
------------Counter---------------------
"""
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) # 'blue'가 등장한 횟수 출력
print(counter['green']) # 'green'이 등장한 횟수 출력
print(dict(counter)) # 사전 자료형으로 반환

"""
------------최대 공약수와 최소 공배수---------------------
"""
import math

# 최소 공배수(LCM)를 구하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)

# 최대 공약수(GCD) 계산
print(math.gcd(21, 14))
# 최소 공배수(LCM) 계산 : 두 수를 곱하고 최대공약수로 나눈 몫
print(lcm(21, 14))
