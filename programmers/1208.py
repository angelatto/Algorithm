#  나중에 Floyd-Warshall로 다시 풀어보기
import collections

def solution(n, results):
    answer = 0
    # 선수가 한 명일때
    if n == 1:
        return 1

    dic = collections.defaultdict(tuple)
    print(dic)

    for A, B in results:
        dic[A] = (0, 1)

    print(dic)


    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
