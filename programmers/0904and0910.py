def compress(s, i): #s를 i단위로 압축해서 리턴
    n = s.count(s[0:i]) # 반복되는 횟수
    if n == 1: return s[0:i]
    return str(n) + s[0:i]


def solution(s):
    answer = s
    for i in range(1, len(s)+1): #i는 문자열을 자르는 단위이다.
        str = ''; j = 0  #i가 변할 때마다 초기화
        before_comp = ''
        while 1:
            #종료조건이 어려움
            if j >= len(s): break 

            if s[j:j+i] ==  s[j+i:j+i+i]: #같으면 압축
                before_comp += s[j:j+i]

            else: #다른게 나오면 그 앞까지 압축 작업
                before_comp += s[j:j+i] #여기가 중요!!!
                str += compress(before_comp, i)
                before_comp = '' # 초기화
            j+=i

        if len(answer) > len(str) and str != '': #최소 길이 찾기
            answer = str
    #    print(i, ": ", answer)
    return len(answer)

#print(solution("abcabcabcabcdededededede"))
