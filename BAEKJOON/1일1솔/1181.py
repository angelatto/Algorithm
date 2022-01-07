"""
01.07.22
실버5

"""
import sys

N = int(sys.stdin.readline().strip())

all = []
for _ in range(N):
    all.append(sys.stdin.readline().strip())
all = list(set(all))

for i in range(len(all)):
    all[i] = (all[i], len(all[i]))

all.sort(key=lambda one: (one[1], one[0]))
for one in all:
    print(one[0])