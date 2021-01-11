import collections
def solution(lottos):
    list_A = [] # 당첨 번호 리스트
    list_B = [] # 보너스 번호 리스트

    for lotto in lottos: # 7주차
        week = lotto.split()
        for num in week:
            if num.startswith('('): # 보너스
                list_B.append(num)
            else: # 당첨번호
                list_A.append(num)

    # 리스트의 요소들을 괄호 지우고 온전히 숫자로 다듬기
    def f(t): # 괄호 지우기  -> re 모듈 쓰는 거로 다시 수정 예정
        if t.startswith('('):
            if len(t) == 3: # 1-9
                t = t[1:2]
            if len(t) == 4: # 10-45
                t = t[1:3]
        return int(t)

    list_A = list(map(int, list_A))
    list_B = list(map(f, list_B))

    counterA = collections.Counter(list_A)
    counterB = collections.Counter(list_B)

    for n in range(1, 46):
        if n not in counterA:
            counterA[n] = 0
        if n not in counterB:
            counterB[n] = 0

    # print('counterA: ', counterA)
    # print('counterB: ', counterB)
    #--------------------여기까지 Counter 처리  ------------------------

    li_A = sorted(list(counterA.items()), key=lambda a : (-a[1], a[0]))
    resultA = [li_A[i][0] for i in range(6)]

    #--------------------여기까지 당첨 번호 6개 출력  --------------------------

    li_B = sorted(list(counterB.items()), key=lambda a : (-a[1], a[0]))
    bonus = 0
    for tu in li_B:
        if tu[0] not in resultA:
            bonus = tu[0]
            break
    #--------------------여기까지 보너스 번호 1개 출력  --------------------------

    resultA.append(bonus)
    resultA.sort()
    resultA = list(map(str, resultA))
    answer = ' '.join(resultA)
    answer = answer.replace(str(bonus), '(' + str(bonus) + ')', 1)

    return answer

print(solution(["15 10 39 5 1 21 (22)", "11 5 (10) 39 1 8 44", "(39) 10 5 22 15 9 20", "22 10 5 1 (15) 3 2", "10 (5) 22 1 15 41 38", "10 5 39 33 17 14 (1)"]))
print(solution(["10 18 23 33 (15) 29 45", "42 (5) 45 32 15 23 12", "19 6 12 16 35 34 (17)", "(15) 23 26 21 20 37 12", "15 20 39 9 (18) 5 12", "18 (20) 11 5 22 21 25", "42 44 23 8 5 22 (20)"]))
