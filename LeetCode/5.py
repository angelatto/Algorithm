def longestPalindrome(s):
#1. 모든 팰린드롬 경우의 수를 구하고 -> 그 중에서 가장 긴 길이를 리턴한다..?
    #모든 서브 스트링에 대하여 sub == sub[::-1] 이면 펠린드롬이다.
    # 중간에서 넓게 확장해 나가는 ..? 
    for i in range(len(s)):
        s[i:]



print(longestPalindrome("babad"))
