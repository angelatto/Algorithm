def solution(str):
    start = (50 - len(str)) // 2
    result = ''
    for i in range(50):
        if i == start:
            result += str
        elif start+1 <= i < start+len(str):
            continue
        else:
            result += '='
    return result

#========================hi========================
str = input()
if len(str) > 50:
    print('50글자 미만으로 입력하세요')
else:
    # sol1
    print(solution(str))
    # sol2 - format 함수 이용
    print("{0:=^50}".format(str))
