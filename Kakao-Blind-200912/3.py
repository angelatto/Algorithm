def solution(info, query):
    answer = []
#정확성은 ok이지만 효율성이 zero임
    people = len(info)
    all_info = []
    for person in info:
        p = person.split()
        p.append(True)
        all_info.append(p)#하나의 리스트는 4개의 조건과 점수 1개와 불리안으로 이루어짐

    # print(all_info)
    # 언어별로 3가지 디비 테이블 만들기 -> 디비 클러스터링

    for q in query:
        #하나의 쿼리에 대하여 몇명이 있는지 답을 구한후에 answer 배열에 정답 삽입
        list_q = q.split() #8개로 이루어짐 : -도 고려하기
        # print(list_q) #의미있는 인덱스는 0, 2, 4, 6, 7이다!!!!
        #조건을 하나씩 체크하면서 범위 추려나가기
        #점수 문자열인거 주의 int()
        for one in all_info:
            if one[0] != list_q[0] and list_q[0] != '-':
                one[5] = False
                continue
            if one[1] != list_q[2] and list_q[2] != '-':
                one[5] = False
                continue
            if one[2] != list_q[4] and list_q[4] != '-':
                one[5] = False
                continue
            if one[3] != list_q[6] and list_q[6] != '-':
                one[5] = False
                continue
            if int(one[4]) < int(list_q[7]):
                one[5] = False
                continue
        count = 0
        for one in all_info:
            if one[5] == True:
                count += 1
        answer.append(count)

        #all_info의 t/f초기화
        for one in all_info:
            one[5] = True
    return answer
