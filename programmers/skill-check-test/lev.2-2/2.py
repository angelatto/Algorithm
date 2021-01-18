def solution(s):
    # 이진 변환의 횟수와 제거된 모든 0의 개수
    c_bin, c_zero = 0, 0

    while s != '1':
        c_bin += 1
        # 1. 0을 제거
        c_zero += s.count('0')
        temp = s.count('1')

        # 2. len(s) 를 2진법으로 표현한 문자열로 바꾼다.
        s = bin(temp)[2:]

    answer = [c_bin, c_zero]
    return answer


print(solution("110010101001"))