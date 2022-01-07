"""
01.07.21
실버4


S = A[0] × B[0] + ... + A[N-1] × B[N-1]

S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자.
 단, B에 있는 수는 재배열하면 안 된다.
S의 최솟값을 출력하는 프로그램을 작성하시오


5
1 1 1 6 0
2 7 8 3 1

"""
import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
B = list(map(int, sys.stdin.readline().strip().split()))

A.sort(reverse=True)
B.sort()

S = list(map(lambda x, y: x*y, A, B))

# S가 최솟값이 나오도록
print(sum(S))
