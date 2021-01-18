def solution(operations):
    queue = []
    for oper in operations:
        if oper.startswith('I'):  # 삽입
            queue.append(int(oper.split()[1]))
            queue.sort()
        elif queue:  # 삭제
            if int(oper.split()[1]) == 1:  # 최댓값 삭제
                queue.pop()
            else:  # 최솟값 삭제
                queue.pop(0)

    if not queue:
        return [0, 0]
    return [queue[-1], queue[0]]