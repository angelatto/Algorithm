"""
접미사배열
22.02.11

baekjoon

"""

s = input()
all = []

for i in range(len(s)):
    all.append(s[i:])

all.sort()
for a in all:
    print(a)