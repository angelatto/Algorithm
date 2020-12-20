# p.588 분할 가능한 배낭 문제 - 그리디 알고리즘 

def fractional_knapsack(cargo):
    capacity = 150
    pack = []

    # 단가 계산 -> 역순 정렬 (내림차순 정렬)
    for c in cargo:
        pack.append((c[0] / c[1], c[0], c[1]))
    pack.sort(reverse=True)

    # 단가 순 그리디 계산
    total_value: float = 0.0
    for p in pack:
        if capacity - p[2] >= 0:
            capacity -= p[2]
            total_value += p[1]
        else:
            fraction = capacity / p[2]
            total_value += p[1] * fraction
            break

    return total_value
