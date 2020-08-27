#입출력 속도 : sys.stdin.readline() > raw_input() > input
# a = [int(x) for x in input().split()]

import sys
a = list(map(int, sys.stdin.readline().split()))# 하나의 라인을 입력받는 경우
print(int(sum(a) // 3))


#여러라인을 입력받는 경우
# n = sys.stdin.readline()
# a = [sys.stdin.readline() for i in range(n)]
