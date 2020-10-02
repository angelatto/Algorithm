score = {}
for i in range(1, 9):
    score[i] = int(input())

new = sorted(score.items(), key= lambda x : x[1], reverse=True)

# print(score) - 딕셔너리 형태 
# print(score.items()) - 튜플 형태로 (key, value)
#print(new)

# 총점 구하기
total = 0; count = 0; rank = []
for score in new:
    if count == 5:
        break
    rank.append(score[0])
    total += score[1]
    count += 1
rank.sort()

print(total)
for _ in rank:
    print(_ , end=' ')
print()
