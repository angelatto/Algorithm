import sys

s = sys.stdin.readline()
if s.isupper(): print('YES')
else: print('NO')

ss = sys.stdin.readline()
for i in range(len(ss)):
    if ss[i] == ss[i].upper(): print(ss[i], end='')
    else:  continue
