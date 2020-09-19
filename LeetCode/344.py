def reverseString(s) -> None:
#풀이 1)     s[:] = s[::-1]
#풀이 2)     s.reverse()
#풀이 3)   투포인터를 이용한 스왑
    left, right = 0 , len(s)-1
    while left < right:
        s[left] , s[right] = s[right], s[left]
        left += 1
        right -= 1
    print(s)


print(reverseString(["h","e","l","l","o"]))
