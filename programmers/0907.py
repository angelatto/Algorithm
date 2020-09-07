from collections import deque
from itertools import combinations

def solution(relation):
    n_row=len(relation)
    n_col=len(relation[0])  #->runtime error 우려되는 부분

    candidates=[]
    for i in range(1,n_col+1):
        candidates.extend(list(combinations(range(n_col),i)))
    print(candidates) #고를 수 있는 모든 후보키 인덱스 조합(뽑기)


    #유일성을 만족하는 후보키 리스트
    final=[]
    for keys in candidates:
        tmp=[tuple([item[key] for key in keys]) for item in relation]
        # print("tmp:  " , end='')
        # print(tmp)
        if len(set(tmp))==n_row: #열(row)마다 집합으로 묶어서 원래 행 개수랑 같아야 유일성 만족
            final.append(keys)
    print(final)


    #최소성을 만족하지 못하면 지우기
    answer=set(final) #final 후보키 리스트를 집합으로 생성 -> 차집합 함수 이용하려고
    print(answer)
    for i in range(len(final)):
        for j in range(i+1,len(final)):
            # if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
            if set(final[i]) & set(final[j]) == set(final[i]): #교집합이 존재하면 후보키에서 제외한다.
                print(set(final[i]) & set(final[j]))
                answer.discard(final[j]) #집합 제거 함수 -> 여기서 remove함수 쓰면 keyError난다. 주의!! 
    print(answer)


    return len(answer)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
