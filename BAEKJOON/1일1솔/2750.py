"""
01.11.22
브론즈1

"""
N = int(input())

array = []
for _ in range(N):
    array.append(int(input()))
array.sort()

for num in array:
    print(num)
