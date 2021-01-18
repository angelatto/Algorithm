# 효율성까지 체크하는 문제 -> 이 문제는 정답 체크 못했음

def solution(stones, k):
    result = 0

    # 0이 나오면 그 돌은 밟지 못함, 그 다음꺼 밟아야 하는데 그게 k이하
    flag = True
    while flag:
        for i in range(len(stones)):
            if stones[i] != 0 or i == len(stones)-1:
                stones[i] -= 1
            else:
                # stones[i+1 : i+k] 안에 모두 0만 있으면 브레이크 -> flag = False
                if sum(stones[i:i+k]) == 0:
                    flag = False
                    break

        if flag:
            result += 1
        else:
            break

    return result


print(solution([2,4,5,3,2,1,4,2,5,1], 3)) # 3