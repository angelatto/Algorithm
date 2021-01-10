def solution(black_caps):
    people = len(black_caps) # 사람 수
    answer = [0 for i in range(people)]

    answer[1] = 2 if black_caps[0] == 0 else 1
    answer[people-2] = 2 if black_caps[people-1] == 0 else 1

    for i in range(1, people-1):
        if black_caps[i] == 0: #양 옆이 흰 색
            answer[i-1] = answer[i+1] = 2
        if black_caps[i] == 2: # 둘 다  검은 색
            answer[i-1] = answer[i+1] = 1
        if black_caps[i] == 1: # 양 쪽에 아무거나 하나는 검은색
            if answer[i-1] == 1 or answer[i+1] == 2:
                answer[i-1] = 1
                answer[i+1] = 2
            if answer[i+1] == 1 or answer[i-1] == 2:
                answer[i-1] = 2
                answer[i+1] = 1
    return answer

# print(solution([1,1,2,0]))
# print(solution([1,1,1]))
