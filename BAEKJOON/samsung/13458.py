"""
시험 감독 (lev.bronze-2)
b는 하나만, c는 여러 개 가능
"""
n = int(input())
li = list(map(int, input().split()))
b, c = list(map(int, input().split()))

result = 0
for case in li:  # 하나의 케이스마다 감독관 수 구하기 - 최솟값
    case -= b
    result += 1

    if case > 0:  # c를 뺸다.
        m, v = divmod(case, c)
        result += m
        if v != 0:
            result += 1

print(result)
