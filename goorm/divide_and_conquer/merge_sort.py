
def merge(left, right): # 정복
    li = []

    i = 0; j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            li.append(left[i])
            i += 1
        else:
            li.append(right[j])
            j += 1

    if i == len(left):
        li.extend(right[j:])
    if j == len(right):
        li.extend(left[i:])
    return li

def merge_sort(arr):
    if len(arr) <= 1: # base condition
        return arr

    mid = len(arr) // 2

    # 분할하기
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 정복하기
    return merge(left, right)

#__main__
size = int(input())
arr = list(map(int, input().split()))

result = merge_sort(arr)
for n in result:
    print(n, end=' ')
print()
