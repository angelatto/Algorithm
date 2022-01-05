"""
1이 될 때 까지

1. N 에서 1을 뺸다.
2. N 을 K로 나눈다.

N 과 K 가 주어질 때 N이 1이 될 때까지
1번 혹은 2번의 과정을 수행해야 하는 최소 횟수 를 구하시오.

"""
count = 0
# N, K = 25, 3
# N, K을 공백을 기준으로 구분하여 입력 받기
N, K = map(int, input().split())

while N != 1:
    if N % K == 0:
        N //= K
    else:
        N -= 1
    count += 1
print(count)
