import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(' '.join(list(reversed(list(map(str, arr))))))
