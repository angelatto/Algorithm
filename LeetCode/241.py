# 분할 후 정복
# eval() 함수를 이용하여 문자열로 표현된 식을 처리

def diffWaysToCompute(input: str):
    def compute(left, right, op):
        result = []
        for l in left:
            for r in right:
                result.append(eval(str(l) + op + str(r))) #eval함수안에는 문자열
        return result

    # 낱개의 숫자 의미, 분할 결과를 리턴받는 코드
    if input.isdigit():
        return [int(input)]

    results = []
    # 분할하기
    for index, value in enumerate(input):
        if value in '+*-': #분할조건: 연산자가 나올 때
            left = diffWaysToCompute(input[:index]) #str
            right = diffWaysToCompute(input[index+1:])
            #여기서 주의해야할 것이 index를 써버리면 연산자를 포함하게 된다. +1 반드시 해주기

            # 다 쪼개지면 정복하기
            results.extend(compute(left, right, value))
    return results

print(diffWaysToCompute("2*3-4*5"))
