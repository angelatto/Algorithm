def solution(dirs):
    answer = 0

    dic = {'U': (1, 0), 'R': (0, 1), 'D': (-1, 0), 'L': (0, -1)}
    visited = []

    cur = [0, 0]
    for dir in dirs:
        x = cur[0] + dic[dir][0]
        y = cur[1] + dic[dir][1]

        if not (-5 <= x <= 5 and -5 <= y <= 5):
            continue

        if (cur[0], cur[1], x, y) not in visited:
            visited.append((cur[0], cur[1], x, y))
            visited.append((x, y, cur[0], cur[1]))
            answer += 1

        cur[0] = x
        cur[1] = y

    return answer
