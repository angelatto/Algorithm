# 연속되는 문자열 압축하기
# aaabbbbcdddd -> a3b4c1d4
# ------------ 첫번째 풀이 ---------------
# input = input()
# answer = ''
#
# stack = []
# for i in range(len(input)):
#     if i != len(input)-1 and input[i] == input[i+1]:
#         stack.append(input[i])
#     else:
#         stack.append(input[i])
#         answer = answer + input[i] + str(len(stack))
#         stack.clear()
#
# print(answer) # 정답 리턴

# ------------ 다른 풀이 ---------------
import re

input_data = 'aaabbccccccasss'
rule = re.compile('[a-c]+')

one = re.findall('b', input_data)
two = re.findall(rule, input_data)
three = re.findall('(\\w)(\\1*)', input_data)

print(one)
print(two)
print(three)

s = ''
for i, j in three:
    s += str(len(j)+1)+i
print(s)
