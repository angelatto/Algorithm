def solution(n_list):
    result = 0

    for n in n_list:
        if n.count('j') + n.count('k') > 0:
            result += 1
    return result


name_list = ['james', 'loke', 'oliver','jack']
print(solution(name_list))