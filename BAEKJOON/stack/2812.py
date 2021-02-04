"""
크게 만들기 (lev.glod-5)

5 2
45559

"""
N, k = list(map(int, input().split()))
num = input()  # string
stack = []
result = 0

for i in range(N):  # 문자

    if len(stack) == k:
        print(stack)
        result = max(result, int(''.join(stack)))
        target = min(int(stack[-1]), int(num[i]))
        # 둘 중 더 작은 값을 제거한다.
        print(int(stack[-1]), int(num[i]))
        # stack.remove(target)
        print(stack)

    stack.append(num[i])

print(result)