def isAnagram(s: str, t: str) -> bool:
    # 두 문자열을 정렬해서 같은지 다른지 비교하기
    return sorted(s) == sorted(t)

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
