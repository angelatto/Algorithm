import collections

def leastInterval(tasks, n: int) -> int:

    counter = collections.Counter(tasks)
    result = 0

    while True:
        sub_count = 0 # 초기화

        for task, count in counter.most_common(n+1):
            print(task, count)
            sub_count += 1
            result += 1

            counter.subtract(task)
            # 0 이하인 아이템을 counter에서 제거함
            counter += collections.Counter()

        if not counter:
            break
        else: #idle 개수
            result += n+1 - sub_count
        print('Result: ', result)

    return result

print(leastInterval(["A","A","A","B","B","B"], 2))
# print(leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))
