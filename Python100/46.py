
#리스트 컴프리핸션 이용
list_num = [str(i) for i in range(1, 101)]

#split의 반대 개념 join함수 이용 즉, 문자열로 구성된 리스트를 하나의 문자열로 변환
all = ''.join(list_num)

result = 0
for n in all:
    result += int(n)

print(result)
