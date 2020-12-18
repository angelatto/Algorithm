import collections

def maxSlidingWindow(nums, k: int):
    answer = []
    window = collections.deque()
    cur_max = float('-inf')

    for i, v in enumerate(nums):
        window.append(v)
        if i < k-1:
            continue

        if cur_max == float('-inf'):
            cur_max = max(window)
        elif v > cur_max:
            cur_max = v

        answer.append(cur_max)

        # 선입선출, 이때 빠지는 값이 최댓값과 같으면 초기화
        if cur_max == window.popleft():
            cur_max = float('-inf')

    return answer

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
