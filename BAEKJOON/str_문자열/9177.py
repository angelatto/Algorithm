"""
단어 섞기 (lev.gold-5)
- 문자열, bfs 로 푸는 문제

세 개의 단어가 주어질 때
-> 첫 번째 단어와 두 번째 단어를 섞어서 세 번째 단어를 만들 수 있는지 궁금
-> 순서는 섞이면 안된다.

세 번째 단어에서 뭔가 하나씩 pop 해주면서 가능 여부를 따져주기

"""
import collections

n = int(input())
for i in range(n):
    # 하나의 테스트 케이스 - w1과 w2로 target 만들 수 있으면 yes, 아니면 no
    w1, w2, target = list(map(list, input().split()))
    result = 'yes'

    queue = collections.deque([target[-1]])
    while queue:
        t = queue.pop()
        print('t: ', t)

        if len(w1) > 0 and t != w1[-1]:
            if len(w2) > 0 and t != w2[-1]:
                result = 'no'
                break

        # 1. 일단 t에 대해서 일치하는 문자를 큐에 푸시하는 작업부터 해줘야 한다.
        if len(w1) > 0 and t == w1[-1]:
            c = w1.pop()
        if len(w2) > 0 and t == w2[-1]:
            c = w2.pop()

        target.pop()
        if len(target) > 0:
            queue.appendleft(target[-1])

    # 하나의 테스트 케이스에 대하여 답 출력
    print('Data set %d: %s' % (i+1, result))