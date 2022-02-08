"""
포도주시식
22.02.08
다이나믹 프로그래밍

6
6
10
13
9
8
1

1. 현재 포도주 안먹는 경우 -> dp[i-1]
2. 현재 포도주 먹는데 직전 포도주도 먹는경우 -> dp[i-3]+w[i-1]+w[i]
3. 현재 포도주 먹는데, 직전 포도주 안먹는 경우 -> dp[i-2]+w[i]

"""
num = int(input())
w = []
for _ in range(num):
    w.append(int(input()))

dp = [0 for _ in range(num)]
dp[0] = w[0]
if len(dp) >= 2:
    dp[1] = w[0] + w[1]
if len(dp) >= 3:
    dp[2] = max(dp[1], w[1]+w[2], w[0]+w[2])

for i in range(3, num):
    dp[i] = max(dp[i-1], dp[i-3]+w[i-1]+w[i], dp[i-2]+w[i])

# index error dp길이가 3이하인경우도 가능하니까
print(dp[-1])