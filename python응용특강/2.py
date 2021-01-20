import collections


def solution(shirt):
    li = collections.Counter(shirt)
    result = []
    result.append(li['XS'])
    result.append(li['S'])
    result.append(li['M'])
    result.append(li['L'])
    result.append(li['XL'])
    result.append(li['XXL'])
    return result


shirt_size = ['XS', 'S', 'L', 'L', 'XL', 'S']
print(solution(shirt_size))