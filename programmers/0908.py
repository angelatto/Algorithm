# -*- coding: utf-8 -*-
def isBalance(str): #균형잡힌 문자열인지 체크
    count0 = str.count('(')
    count1 = str.count(')')
    if count0 == count1: return True
    else:   return False

def isRight(str): #올바른 문자열인지 체크
    if (str[0] != '(') | isBalance(str) == False:
        return False
    stack = []
    for s in str:
        if s == '(':
            stack.append(s)
        elif s == ')':
            try:
                stack.pop()
            except IndexError:
                return False
    if len(stack) == 0:
        return True
    return False

def solution(p):
    #1단계
    if p == '': return p
    if isRight(p):
        return p

    #2단계 : 문자열을 분리 u는 균형잡힌 문자열
    u, v = '', ''
    for i in range(len(p)):
        if u == '' or isBalance(u) == False :
            u += p[i]
        else:  #균형잡힌 최소길이의 u를 구힌디. 나머지는 v이다.
            v = p[i:]
            break

    #3단계
    if isRight(u) == True:
        return u+solution(v)
    else:   #4단계
        answer = ''
        answer += '('
        answer += solution(v)
        answer += ')'
        for i in range(1, len(u)-1):
            if u[i] == '(':
                answer += ')'
            elif u[i] == ')':
                answer += '('

    return answer


print(solution(")("))
print(solution("(()())()"))
print(solution("()(())()"))
