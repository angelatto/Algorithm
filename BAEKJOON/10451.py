import sys

testcase = int(input())
for _ in range(testcase): #2개
    n = int(input()) #8개

    def get_cnt():
        cnt = 0
        # idx는 인덱스인데 인덱스로 보고 1-n까지 체크할꺼라서
        sequential = [0] + list(map(int, sys.stdin.readline().split()))
        visit  = [0] * (n + 1) #방문 여부 확인

        # idx:          1 2 3 4 5 6 7 8
        # sequential: 0 3 2 7 8 1 4 5 6
        # visit:      0 0 0 0 0 0 0 0 0

        for idx in range(1, n+1): #1~n까지
            i = idx
            if visit[i] == 0: #처음 방문한 것이면
                cnt += 1
            else:
                continue

            while not visit[i]: #방문안했다면...사이클 최대한 돌아서 방문표시하기
                visit[i] = 1
                i = sequential[i]

        return cnt

    print(get_cnt())
