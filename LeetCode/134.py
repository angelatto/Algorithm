def canCompleteCircuit(gas, cost) -> int:
    fuel = []
    for i in range(len(gas)):
        fuel.append(gas[i] - cost[i])
    print(fuel)

    if sum(fuel) < 0: #불가능함
        return -1

    # 반복문 돌면서 마이너스가 출현하는 그 시작점은 제거하면 됨
    index, checkSum = 0, 0
    for i in range(len(fuel)):
        if checkSum + fuel[i] < 0:
            index = i + 1
            checkSum = 0
        else:
            checkSum += fuel[i]

    return index

print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
