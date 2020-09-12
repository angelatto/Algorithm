from itertools import combinations

def solution(orders, course): #완탐인듯
    answer = []
    #코스요리 개수는 코스배열에 담긴 개수만 따진다.
    #사람 수
    people = len(orders)
    for c in course: #전체 반복문: 코스에 따라서 생각하기
        #ex - c가 2일때 가능한 모든 조합 뽑아내서 리스트로 만들어내기
        candidates=[]
        for order in orders:
            candidates.extend(list(combinations(order, c)))

        # print(candidates)
        if len(candidates) == 0:
            continue

        #하나의 리스트에 대하여 개수를 세서 딕셔너리 만들기
        # 앞뒤순서... 여기서 딕셔너리 만들기 전에 미리 정렬하기
        dict = {}
        for cand in candidates:
            cand = sorted(cand)
            cand = tuple(cand)
            if cand not in dict.keys(): #처음 삽입
                dict[cand] = 1
            else:
                dict[cand] += 1
        # print(dict)
        #가장 많이 조합된 조합을 고르기 - 여러개일수도있음
        num = max(dict.values())
        if num < 2: continue

        for d in dict.items():
            s = list(d[0])
            s = ''.join(s)
            if d[1] == num: #가장 많이 조합된거라면, num이 2이상이라면 결과에 담기
                answer.append(s)

        answer.sort()

    return answer
# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
# print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
