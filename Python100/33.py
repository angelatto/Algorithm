import sys

nums = sys.stdin.readline()
new = nums.rstrip()

for i in range(len(new)-1, -1, -1):
    print(new[i], end='')

print()
