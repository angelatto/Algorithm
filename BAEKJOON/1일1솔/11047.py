"""
동전0
22.02.10

10 4200
1
5
10
50
100
500
1000
5000
10000
50000
"""
n, money = map(int, input().split())
list = [int(input()) for _ in range(n)]
result = 0
for m in list[::-1]:
    if money == 0:
        break
    if m <= money:
        result += money // m
        money -= (money // m) * m

print(result)