"""
탑 (lev.gold-5)
- 스택은 내림차순을 유지해야 한다. 즉, 자신보다 큰 값이 올 때 처리를 해줘야 한다.
"""

n = int(input())
heights = list(map(int, input().split()))
stack = []  # 인덱스를 저장
result = []
for i, h in enumerate(heights):
    while stack and heights[stack[-1]] < h:
        stack.pop()

    if stack and heights[stack[-1]] >= h:
        result.append(stack[-1] + 1)
    else:
        result.append(0)

    stack.append(i)

print(*result)
