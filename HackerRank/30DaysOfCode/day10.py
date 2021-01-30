import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    num = bin(n)

    maxlen = 0
    temp = 0
    for i in range(len(num)):
        if num[i] == '1':
            temp += 1
            maxlen = max(maxlen, temp)
        else:
            temp = 0
    print(maxlen)
