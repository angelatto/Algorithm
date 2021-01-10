import collections
def solution(lottos):
    list_A = [] # 당첨 번호 리스트
    list_B = [] # 보너스 번호 리스트

    for lotto in lottos:
        week = lotto.split()
        for num in week:
            if num.startswith('('): # 보넌스
                list_B.append(num)
            else: # 당첨번호
                list_A.append(num)

    counterA = collections.Counter(list_A)
    counterB = collections.Counter(list_B)

    for n in range(1, 46):
        if str(n) not in counterA:
            counterA[str(n)] = 0
        if str(n) not in counterB:
            counterB[str(n)] = 0

    li_A = sorted(list(counterA.items()), key=lambda a : (-a[1], int(a[0])))
    resultA = []; i = 0
    for i in range(6):
        resultA.append(li_A[i][0])
    print('resultA', resultA)

    # li_b에서 괄호 제거하고 여기서 정렬한다음에 ,
    # resultA에 없는 숫자중에 -> 맨 처음꺼 하나 보너스로 만들기

    li_B = list(counterB.items())
    new_B = []
    for l in li_B:
        new_B.append(list(l))

    for t in new_B:
        if t[0].startswith('('):
            if len(t[0]) == 3:
                t[0] = t[0][1:2]
            if len(t[0]) == 4:
                t[0] = t[0][1:3]

    new_B = sorted(new_B, key=lambda a : (-a[1], int(a[0])))
    print(new_B)

    bonus = 0
    for l in new_B:
        if l[0] not in resultA:
            bonus = l[0]
            break

    resultA.append(int(bonus))
    resultA = list(map(int, resultA))
    resultA.sort()

    answer = ''
    for i in range(len(resultA)):
        if resultA[i] == int(bonus):
            answer += '('+str(bonus)+')' + ' '
        else:
            answer += str(resultA[i]) + ' '

    return answer.rstrip()

# print(solution(["15 10 39 5 1 21 (22)", "11 5 (10) 39 1 8 44", "(39) 10 5 22 15 9 20", "22 10 5 1 (15) 3 2", "10 (5) 22 1 15 41 38", "10 5 39 33 17 14 (1)"]))
# print(solution(["10 18 23 33 (15) 29 45", "42 (5) 45 32 15 23 12", "19 6 12 16 35 34 (17)", "(15) 23 26 21 20 37 12", "15 20 39 9 (18) 5 12", "18 (20) 11 5 22 21 25", "42 44 23 8 5 22 (20)"]))
