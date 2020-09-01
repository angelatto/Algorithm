
def solution(N, stages):
    fail = {}

    denominator = len(stages) # 총 학생 수

    for i in range(1, N+1): #1번 스테이지부터 각각의 실패율 구해나가기
        # count = 0; count2 = 0 #분자 , 분모
        # for j in stages:
        #     if j >= i: count2 += 1
        #     if j == i: count += 1

        if denominator == 0:
            fail[i]  = 0
        else:
            count = stages.count(i)
            fail[i] = count / denominator
            denominator -= count

    # 각 스테이지 마다 각각의 실패율을 저장함 (N개의 스테이지를 딕셔너리로 저장)
    # key : 스테이지 넘버 1~N , value : 실패율
    # 리턴값은 value로 내림차순 하고서 그 key를 리턴한다 -> 정렬 1차 기준은 value, 2차 기준은 key인 셈이다.

    return sorted(fail.keys(), key=lambda x : fail[x], reverse=True)

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
