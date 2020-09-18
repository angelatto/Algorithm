import collections
import re
def isPalindrome( s: str) -> bool:
    #풀이-1
        # s = s.lower()
        # new = ''
        # for _ in s:
        #     if _.isalnum():
        #         new += _
        # for i in range(len(new)//2):
        #     if new[i] !=  new[len(new)-1-i]:
        #         return False
        # return True


    #풀이-2
        # strs = collections.deque()
        # for c in s:
        #     if c.isalnum():
        #         strs.append(c.lower())
        #
        # while len(strs) > 1:
        #     if strs.popleft() != strs.pop():
        #         return False
        # return True

    #풀이-3 문자열을 조작할 떄는 항상 슬라이싱을 우선으로 사용하는 편이 속도 개선에 유리하다.
        s = s.lower()
        s = re.sub('[^0-9a-z]', '', s)
        print(s)
        return s == s[::-1]
print(isPalindrome("race a car"))
