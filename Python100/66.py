top =  ['ABCDEF', 'BCAD', 'ADEFQRX', 'BEDFG', 'AEBFDGCH']
rule = 'ABCD'

def solution(top, rule):
    answer = []
    for block in top:
        answer.append(check(block, rule))
    return answer

def check(block, rule):
    temp = 0 # 항상 rule의 첫 인덱스로 초기화
    for b in block:
        if b in rule:
            if temp > rule.index(b):
                return '불가능'
            temp = rule.index(b)
    return '가능'

print(solution(top, rule))
