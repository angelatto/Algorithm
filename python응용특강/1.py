import random


def getNumber():
    return random.randrange(1, 46)


print('** 로또 추첨을 시작합니다. **')
lotto = []
print('추첨된 로또 번호 ==> ', end='')
while len(lotto) != 6:
    n = getNumber()
    if lotto.count(n) == 0:
        lotto.append(n)
lotto.sort()
print(lotto)