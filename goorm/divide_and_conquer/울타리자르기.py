# n = int(input())
# arr = list(map(int, input().split()))
# 구름 IDE에서 주의할 것은 모든 출력값을 리턴값으로 인식하는 것이다.

n = 7
arr = [7,1,5,9,6,7,3]

max_size = max(arr)

for i in range(n-1):
    flag = True
    for j in range(i+1, n):
        if flag and arr[i] <= arr[j]:
            current = arr[i] * (j-i+1)
            max_size = max(current, max_size)
        else:
            flag = False

# 답
print(max_size)
