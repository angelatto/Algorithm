def solution(grades, weights, threshold):
    dict_sc = {"A+":10, "A0":9, "B+":8, "B0":7, "C+":6, "C0":5,
                "D+":4, "D0":3, "F":0}

    sum = 0
    for i in range(len(grades)):
        sum += dict_sc[grades[i]] * weights[i]
    return sum-threshold


print(solution(["A+","D+","F","C0"], [2,5,10,3], 50))
