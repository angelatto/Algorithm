# 반복해서 봐야 할 문제 
def zero_one_knapsack(cargo, capacity): #타뷸레이션 - p.634
    pack = [] # 6 * 16 이차원 배열

    for i in range(len(cargo)+1):
        pack.append([])
        for c in range(capacity+1):
            print('c: ', c)
            if i==0 or c==0:
                pack[i].append(0)
            elif cargo[i-1][1] <= c:
                # 현재 cargo(cargo[i-1])를 뽑을 지 말 지 선택하는 코드
                pack[i].append(
                    max(
                        cargo[i-1][0] + pack[i-1][c - cargo[i-1][1]],
                        pack[i-1][c]
                    ))
            else:
                pack[i].append(pack[i-1][c])

    return pack[-1][-1]

#__main__
# 화물 후보 : (달러, 무게)
cargo = [(4, 12), (2,1), (10,4), (1,1), (2,2)]
# 배낭 크기
capacity = 15
print(zero_one_knapsack(cargo, capacity))

# 결국 cargo는 bucket이고 그 중에서 뽑기 문제임.
# 그러나 몇 개를 뽑을 지 정해지지 않음!!!
# 뽑기 조건은 달러합이 '최대'이어야 하고, 'capacity이내'여야 함.

# 1개 뽑을 때 모든 경우의 수 다해보고, 2개뽑을 때 모든 경우의 수 다해보고... 이런식으로
# 5개 모두 뽑을 때까지 모든 경우의 수를 해보다간... 효율이 너무 안 좋음

#-----결론) 이렇게 모든 경우의 수를 계산해야 할 때, 다이나믹 프로그래밍은 위력을 발휘함.-----
