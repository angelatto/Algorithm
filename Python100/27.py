import sys

names = list(map(str, sys.stdin.readline().split()))
scores = list(map(int, sys.stdin.readline().split()))

# a = dict()
# for key, value in zip(names, scores):
#     a[key] = value

print(dict(zip(names, scores)))
