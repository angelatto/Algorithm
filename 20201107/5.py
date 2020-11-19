def solution(penter, pexit, pescape, data):
    answer = penter

    len_unit = len(penter)
    list_p = [penter, pexit, pescape]

    # data 쪼개서 합치기
    i = 0
    while i < len(data):
        unit = data[i: i+len_unit]
        if unit in list_p:
            answer += pescape
        answer += unit
        i = i+len_unit

    answer += pexit
    return answer

# test case
print(solution("1100", "0010", "1001", "1101100100101111001111000000"))
print(solution("10", "11", "00", "00011011"))
