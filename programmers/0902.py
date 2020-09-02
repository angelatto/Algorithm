def solution(dartResult):
    answer = 0

    #0-10 문자열이 딤긴 리스트를 생성.
    num = []
    for i in range(0, 11):
        num.append(str(i))

    scope = {'S':1, 'D':2, 'T':3}
    opt = {'*':2, '#':-1}

    dart = []; new=0; number = ''
    for s in dartResult:
        # 10인거는 처리 못함 !!! -> 시작점 말고 끝점 찾기
        #-> scope이 나올때까지를 숫자로 인식하기
        if s in num :
            number += s # 0-10까지 가능 아 10인거 처리를 안함..
        if s in scope:
            new = int(number)
            new = new ** scope[s]
            dart.append(new) #아직 옵션이 나오기 전이다.
            number = ''
        elif s in opt: # 첫판에서 나오는지 아닌지 구분
            dart[len(dart)-1] *= opt[s]
            if len(dart) != 1 and (s == '*'):
                dart[len(dart)-2] *= opt[s]

            

    return sum(dart)

print(solution('1D2S#10S'))
