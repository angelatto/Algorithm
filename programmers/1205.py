import heapq

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0

    # begin -> target 이 되가는 최단경로
    queue = [(answer, begin)]

    #큐에 넣을 수 있는 조건을 만족하는 단어들 찾기
    def check(now, w): # 두 단어의 차이가 한 글자, 인덱스도 같아야함
        count = 0
        for i in range(len(w)):
            if now[i] != w[i]:
                count += 1

        if count == 1:
            return True
        return False

    # bfs 탐색
    while queue:
        answer, now = heapq.heappop(queue)
        if now == target:
            return answer

        for w in words: #큐에 넣을 수 있는 조건을 만족하는 단어들 찾기
            if check(now, w):
                heapq.heappush(queue, (answer+1, w))

    return 0

# test-case
print(solution("hht", "cog", ['hhi', 'hot', 'dot', 'dog', 'lot', 'log', 'cog']))
