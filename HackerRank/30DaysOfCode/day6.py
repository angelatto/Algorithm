n = int(input())
result = []
for _ in range(n):
    s = input()
    result.append(s[::2] + ' ' + s[1::2])

for r in result:
    print(r)