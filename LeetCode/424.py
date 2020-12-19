# k개의 문자를 바꿔서 가장 긴 연속된 문자의 길이를 구하기
import collections

def characterReplacement(s: str, k: int) -> int:
    countS = collections.Counter()

    # 투 포인터
    left = right = 0
    for right in range(1, len(s)+1):
        countS[s[right-1]] += 1
        max_char_n = countS.most_common(1)[0][1]

        # k 초과시 왼쪽 포인터 이동 
        if right - left - max_char_n > k:
            countS[s[left]] -= 1
            left += 1

    return right - left

print(characterReplacement("ABAB", 2))
print(characterReplacement("AABABBA", 1))
