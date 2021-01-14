"""
- 전화번호 목록 lev.gold4
- 시간초과 : python3 -> pypy3로 돌려보니 시간초과 해결
- python3의 시간초과 문제를 해결하기 위해서 line23 : input() -> sys.stdin.readline() 로 변경하였다.
"""
import sys


def solution():
    def check_phone(phone): # 한 번호가 다른 번호의 접두어인 경우가 없어야 한다.
        if len(phone) == 1:
            return True
        # 사전순 정렬되어 있기 때문에 앞뒤만 비교해도 됨 -> O(N)
        for i in range(len(phone) - 1):
            if phone[i] == phone[i+1][:len(phone[i])]:
                return False
        return True

    t = int(input())
    phones = []
    for _ in range(t):
        n = int(input())
        phone = [sys.stdin.readline().strip() for _ in range(n)] # input() 에서 sys.stdin.readline() 로 수정
        phone.sort()
        phones.append(phone)
   
    return ['YES' if check_phone(phone) else 'NO' for phone in phones]


answer = solution()
for a in answer:
    print(a)
