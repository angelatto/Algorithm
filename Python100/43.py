num = int(input())
result = ''

while num > 0:
    result += str(num % 2)
    num = num // 2

print(result)
