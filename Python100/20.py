import sys

nums = list(map(int, sys.stdin.readline().split()))

print(nums[0] // nums[1], nums[0] % nums[1])
