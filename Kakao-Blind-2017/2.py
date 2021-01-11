# 다트 게임 - 문자열 처리(String Manipulation)를 묻는 문제
# 난이도 - 하

def solution(dartResult):
    # 점수 0-9, 10
    domain = {'S':1, 'D':2, 'T':3}

    # 다트는 총 3번 던짐
    result = [0 for i in range(3)]

    score = ''; i = 0
    for s in dartResult:
        if s.isdigit(): # 한 세트 시작
            score += s
        if s in domain.keys():
            result[i] = int(score) ** domain[s]
            score = '' # 점수 초기화
            i += 1 # 다음 다트 세트
        if s == '*': # 스타상
            if i == 0: # 첫 번째 요소
                result[i-1] *= 2
            else:
                result[i-1] *= 2
                result[i-2] *= 2
        if s == '#': # 아차상
            result[i-1] *= -1

    return sum(result)

print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))
