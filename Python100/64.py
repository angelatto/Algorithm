weight = int(input())

# 7kg, 3kg -> 가장 적게 옮길 수 있는 횟수 출력
# 불가능하면 -1 출력

result = 0

while True:
    if weight % 7 == 0:
        result += weight // 7
        print(result)
        break
    else:
        weight -= 3
        result += 1
        if weight < 0:
            print(-1)
            break
