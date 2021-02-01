"""
오큰수 (lev.gold-4)
거꾸로 입력 받는 다고 생각하고, 스택은 내림차순을 유지해야 한다.
- 입력값이 백만임
"""
n = int(input())
heights = list(map(int, input().split()))
result = []
stack = []

for i in range(n - 1, -1, -1):
    while stack and stack[-1] <= heights[i]:  # 자신보다 크거나 같으면 팝
        stack.pop()

    if stack:
        result.append(stack[-1])
    else:
        result.append(-1)

    stack.append(heights[i])

print(*result[::-1])