"""
문자열 잘라내기 (lev.gold-5)
실제로 테이블의 가장 위의 행을 삭제하면 pop(0) -> O(n) 시간이 소요되므로, 삭제하지않고 인덱스로 범위를 좁혀간다.

- 시간초과 해결 방법 : 이분탐색
mid 번쨰 행부터 시작하는 테이블을 검사 후에 동일한 문자열이 발견되면 -> mid 이전을 탐색하고
만약에 발견되지 않으면 더 큰 값을 찾기 위해 mid 이후의 행
3 6
qwerty
aswder
tfhtwd

6 6
qwerty
asdfgh
qwequm
xcjotx
zcyrwq
hklrsd
"""
# import time
import sys
input = sys.stdin.readline

# start = time.time()
R, C = list(map(int, input().split()))
table = [''.join(input().split()) for _ in range(R)]  # 개행 문자 제거

count = 0
i, j = 0, len(table)-1
while i <= j:
    mid = i + (j - i) // 2
    print(i, mid, j)

    result = set([t for t in zip(*table[mid:j+1])])
    print(result)
    if len(result) != C:  # 동일한 문자열 발견
        j = mid-1
    else:
        i = mid+1
print(count)
# print("time :", time.time() - start)