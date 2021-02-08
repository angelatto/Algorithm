"""
막대기 (lev.silver-5)

- 2진법으로 나타냈을 때 1의 개수를 구하는 문제와 같다.
"""
n = int(input())
a = bin(n)[2:]
print(a.count('1'))
