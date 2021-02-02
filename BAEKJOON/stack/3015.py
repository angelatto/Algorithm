"""
오아시스 재결합 (lev.gold-1)
시간 복잡도 : O(n) 으로 구현해야함

아이디어 : 자신보다 키가 큰 사람이 오면 자신은 더 이상 그 다음 사람을 볼 수 없으므로 pop()
- 즉, 스택 제일 아래 저장되어 있는 키부터 내림차순을 유지해야 한다.
"""
N = int(input())
stack = []
ans = 0
for _ in range(N):
    x = int(input())

    # 1. 자신보다 큰 값이 들어오면
    while stack and stack[-1][0] < x:
        ans += stack.pop()[1]  # 연속한 숫자가 하나의 숫자로 압축되어 있음

    # 3. 자신과 같은 값이 들어오면
    if stack and stack[-1][0] == x:
        cnt = stack.pop()[1]  # 연속한 숫자 개수
        ans += cnt
        if len(stack) != 0:
            ans += 1
        stack.append((x, cnt + 1))
    else:
        if len(stack) != 0:
            ans += stack[-1][1]
        stack.append((x, 1))

print(ans)