def solution(N, stages):
    result = {}
    denominator = len(stages) #총 학생수
    for stage in range(1, N+1): #총 스테이지 수
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0

    return sorted(result, key=lambda x : result[x], reverse=True)
#sorted안의 result와 result.keys()는 같은 의미로 해석됨
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
