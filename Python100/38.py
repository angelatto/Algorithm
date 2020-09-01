scores = list(map(int, input().strip().split()))

scores.sort(reverse=True) #원본 리스트를 내림차순으로 정렬

print(scores)

limit = 3; count = 0
for i in range(len(scores)):
    if limit == 0: break
    count += 1
    if scores[i] != scores[i+1]:
        limit -= 1



print(count)
