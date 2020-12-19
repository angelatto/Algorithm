# t의 모든 문자가 포함된 가장 짧은 길이의 부분 s를 구하기
# Counter와 투 포인터로 풀기
import collections

def minWindow(s, t) -> str:
    need = collections.Counter(t) # 투 포인터 사이에 들어갈 문자
    missing = len(t)
    left = start = end = 0

    # 오른쪽 포인터 이동
    for right, char in enumerate(s, 1):
        missing -= need[char] > 0
        need[char] -= 1

        # 필요 문자가 0개 이면 왼쪽 포인터 이동 판단
        if missing == 0:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1

            # 투 포인터 길이 최소로 만들기
            if not end or right - left  < end - start:
                start, end = left, right
                need[s[left]] += 1
                left += 1
                missing += 1

    return s[start:end]


print(minWindow('ADOBECODEBANC', 'ABC'))
print(minWindow("a", "aa")) # ''
print(minWindow("abc", "ac")) # abc
print(minWindow("bbaa", "aba")) # baa
