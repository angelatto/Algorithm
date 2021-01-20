def solution(s):
    result = ''

    before = ''
    for c in s:
        if c != before:
            result += c
            before = c

    return result


s = 'senteeeencccccceeee'
print(solution(s))