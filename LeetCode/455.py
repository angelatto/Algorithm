def findContentChildren(g, s) -> int:
    g.sort()
    s.sort()

    i = j = 0
    while i < len(g) and j < len(s):
        if g[i] <= s[j]:
            i += 1 # 다음 아이로 넘어감
        j += 1

    return i

print(findContentChildren([1,2,3], [1,1]))
