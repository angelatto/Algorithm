def lengthOfLongestSubstring(s: str) -> int:
    # 중복 문자 없이 최대 길이의 서브스트링 길이를 리턴하라
    dic = {}
    max_length = start = 0

    # start 는 서브스트링 시작 포인터
    for index, char in enumerate(s):
        if char in dic and start <= dic[char]: # 중복 문자 등장
            start = dic[char] + 1
        else: # 처음 보는 문자 -> 최대 길이 갱신
            max_length = max(max_length, index - start + 1)
            print(start, index)
        # 현재 문자의 위치 삽입
        dic[char] = index
    return max_length

print(lengthOfLongestSubstring("tmmzuxt"))
