"""
곱하기 혹은 더하기

- 각 자리 숫자가 0부터 9로만 이루어진 문자열 S가 주어질 때
왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하여
숫자 사이에 x 혹은 + 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하기

- 이때 모든 연산은 왼쪽에서부터 순서대로 이루어진다.

<문제 해결 아이디어>
1. 두 수 중에 0. 1은 더하고 나머지는 곱한다.

"""

data = input()

result = int(data[0])
for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)