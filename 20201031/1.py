def solution(n, delivery):
    answer = ''
    dict = {}
    for i in range(1, n+1):
        dict[i] = '?'
# 전처리
    delivery = sorted(delivery, key=lambda x: -x[2])
    for order in delivery:  # 하나의 주문 별로
        if order[2] == 1:
            dict[order[0]] = 'O'
            dict[order[1]] = 'O'
        else: # 0이면
            if dict[order[0]] == 'O':
                dict[order[1]] = 'X'
            if dict[order[1]] == 'O':
                dict[order[0]] = 'X'

    # 결과 값
    for c in dict.values():
        answer += c
    return answer
print(solution(7,[[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]]))
