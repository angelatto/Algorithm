limit = int(input())
people = int(input())

weight = []
for i in range(people):
    weight.append(int(input()))

weight.sort() # 원본 무게 오름 차순으로 정렬

count = 0
for i in weight:
    if (limit-i) >= 0:
        limit -= i
        count += 1

print(count)
