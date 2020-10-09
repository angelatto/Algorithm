def solution(array, commands):
    answer = []

    for row in commands:
        new = array[row[0]-1:row[1]]
        new.sort()
        answer.append(new[row[2]-1])

    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
