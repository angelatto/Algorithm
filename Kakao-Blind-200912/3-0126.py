"""
1. 효울성 실패한 풀이 : info 배열을 점수로 오름차순 정렬시킨다음 -> query 배열에서 이진탐색으로 해당 점수 이상의 모든 info를 검사함
2. 효율성을 통과한 풀이 : info 배열에서 조건들을 키값으로, 점수를 리스트 값으로 한 딕셔너리 생성.
                    -> query 배열에서 조건에 맞는 info 딕셔너리를 찾고 그 안에서 점수로 이진탐색
                즉, info 딕셔너리에서 조건에 맞는 것만 거른 다음에, 이진탐색하는 것이 포인트이다.

"""
import collections
import bisect


def solution(info, query):
    answer = []

    info_dic = collections.defaultdict(list)
    for s in info:
        s_list = s.split()
        k, v = tuple(s_list[:-1]), int(s_list[-1])
        bisect.insort(info_dic[k], v)  # 삽입하면서 정렬하는 것보다 효율이 좋음

    for q in query:   # 하나의 케이스에 대하여 몇 명인지 구하기
        result = 0
        options = q.replace('-', '').replace(' and', '').split()
        can = set(options[:-1])
        score = int(options[-1])
        for key, value in info_dic.items():
            if can <= set(key):
                result += len(value) - bisect.bisect_left(value, score)

        answer.append(result)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))