"""
오아시스 재결합 (lev.gold-1)
시간 복잡도 : O(n) 으로 구현해야함

아이디어 : 자신보다 키가 큰 사람이 오면 자신은 더 이상 그 다음 사람을 볼 수 없으므로 pop()
- 즉, 스택 제일 아래 저장되어 있는 키부터 내림차순을 유지해야 한다.
"""
import collections


N = int(input())
stack = []
answer = 0

for i in range(N):
    height = int(input())

    while stack and stack[-1][0] < height:  # 자신보다 키가 큰 사람이 오면
        answer += stack.pop()[1]

    if stack and stack[-1] == height:  # 같은것이 있으면
        cnt = stack.pop()[1]
        answer += cnt
        answer += 1
        stack.append((height, cnt+1))

    elif stack:  # 자신보다 키가 작은 사람이 오면
        answer += 1
        stack.append((height, 1))

# 답 출력
print(answer)