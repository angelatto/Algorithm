def minWindow(s: str, t: str) -> str:

    if s == t:
        return s

    def checkS(s, t): # t가 s의 부분집합인지
        ls = list(s)

        for i in t:
            if i in ls:
                ls.remove(i)
            else:
                return False
        return True

    # 길이가 len(t)일 때부터 +1 씩 슬라이싱 ??
    min_size = len(t)
    while True:
        if min_size > len(s):
            break
        for i in range(len(s) - min_size + 1):
            if checkS(s[i:i+min_size], t):
                return s[i:i+min_size]
        min_size += 1

    return ""
