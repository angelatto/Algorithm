# 뉴스 클러스터링 - 자카드 유사도를 직접 계산하는 프로그램을 작성하는 문제
# 난이도 - 중

# 합집합 길이가 0 인경우도 리턴 65536 예외 처리 해줘야함
# 문자열 각각을 다중 집합으로 만들기, 대소문자 구분하지 않음
# if 영문자가 아닌 문자가 있으면 그 덩어리는 버린다.
import collections

def solution(str1, str2):
    # 1. 먼저 다중집합 두 개 만든다
    setA = [str1[i:i+2].upper() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    setB = [str2[i:i+2].upper() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

    # 2. 그 다음, 교집합 합집합 길이 구하기
    counterA = collections.Counter(setA)
    counterB = collections.Counter(setB)

    # 교집합
    intersection = sum((counterA & counterB).values())

    print(counterA & counterB)
    print(counterA | counterB)


    # 합집합
    union = sum((counterA | counterB).values())

    answer = intersection / union if union != 0 else 1
    return int(answer * 65536)

print(solution('FRANCE', 'french'))
# print(solution('handshake', 'shake hands'))
# print(solution('aa1+aa2', 'AAAA12'))
# print(solution('E=M*C^2', 'e=m*c^2'))
