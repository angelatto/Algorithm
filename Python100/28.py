import sys

s = sys.stdin.readline()

for i in range(len(s) - 2):
    print(s[i], s[i+1], sep='')
