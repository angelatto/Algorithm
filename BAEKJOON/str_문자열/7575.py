"""
# 바이러스 문제, lev.gold1
# 공통으로 나타나는 코드의 길이가 K이상인 경우 : YES, 없으면 NO
# 슬라이딩 윈도우 크기를 'K로 설정' 해서 존재여부 체크하면 될 듯
"""


def solution():
    N, K = list(map(int, input().split()))
    # 전처리
    programs = [];
    for _ in range(N):
        input()
        programs.append(input().split())

    for z in range(len(programs[0]) - K + 1):
        tmp = programs[0][z:z+K]
        for m in range(1, N): # 다른 프로그램에 tmp와 같은 문자열이 있는지 확인, 반대도 확인하기
            candi1 = ''.join(programs[m]).find(''.join(tmp))
            candi2 = ''.join(programs[m][::-1]).find(''.join(tmp))

            if candi1 == -1 and candi2 == -1: # 가장 가까운 반복문만 빠져나간다.
                break

            if m == N-1:
                return 'YES'

    return 'NO'


# __main__
print(solution())
