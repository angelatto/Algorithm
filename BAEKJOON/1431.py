
n = int(input())

answer = []

for _ in range(n): #n번 입력 받는다.
    count = 0
    serial = input()
    for s in serial:
        if s.isdigit():
            count += int(s)

    answer.append((serial, count))

print(answer)
answer.sort(key=lambda x : (len(x[0]), x[1], x[0]))

#질문 : 다중조건일때, 각각 reverse를 T/F 각각 생각할 수 있나..?
# YES!!!   하나는 (-)부호를 붙이면 내림차순이고, (+)는 오름차순이다.

for a in answer: # 리스트
    print(a[0])
