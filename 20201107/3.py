def solution(money, expected, actual):
    answer = money
    betmoney = 100
    flag = 0 # 전판에서 이기면 0. 지면 1
    for i in range(len(expected)):
        # 종료 조건
        if answer <= 0:
            answer = 0
            return answer
        if expected[i] == actual[i]: # 이김
            answer += betmoney
            if flag == 1: # 졌다가 이기면
                betmoney = 100
            flag = 0
        elif expected[i] != actual[i]: # 짐
            answer -= betmoney
            betmoney *= 2
            flag = 1
            if betmoney > answer:
                betmoney = answer
    return answer

#print(solution(1200, ['T', 'T', 'H', 'H', 'H'],['H', 'H', 'T', 'H', 'T']))
print(solution(1500, ['H', 'H', 'H', 'T', 'H'], ['T', 'T', 'T', 'H', 'T']))
