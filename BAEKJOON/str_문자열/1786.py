"""
KMP 알고리즘 - ctrl+F로 문자열 검색할 때 사용하는 알고리즘

문자열 T 에서 문자열 P 패턴이 나타나는 지점, 몇번 나타나는 지 구하기, 위치는
len(T) = n, len(P) = m
문자열 전체를 탐색하는 시간복잡도는 O(nm)이지만, KMP 알고리즘을 사용하면 O(n+m) 내에 문자열 매칭 문제를 풀어낼 수 있다.

"""


# 1. 전처리 - 접두사와 접미사를 기반으로 만드는 테이블 만들기, 시간 복잡도 : O(m)
def makeTable(P):  # P는 패턴 문자열
    table = [0] * len(P)

    i = 0
    for j in range(1, len(P)):
        while i >= 1 and P[i] != P[j]:
            i = table[i - 1]

        if P[i] == P[j]:
            i += 1
            table[j] = i
    return table


# 2. KMP 알고리즘
def KMP(T, P):
    answer = []

    table = makeTable(P)
    i = 0
    for j in range(len(T)):
        while i >= 1 and P[i] != T[j]:
            i = table[i - 1]
        if P[i] == T[j]:
            if i == len(P) - 1:  # 패턴과 일치하는 문자열을 찾았을 때, T에서 패턴이 시작되는 시작 인덱스 저장하기
                answer.append(j - len(P) + 2)
                i = table[i]
            else:
                i += 1
    return answer


# __main__
T = input()
P = input()

answer = KMP(T, P)

# 답 리턴
print(len(answer))
print(*answer)  # answer = [16], *answer = 16
