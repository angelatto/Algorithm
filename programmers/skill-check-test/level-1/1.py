def solution(s):
    answer = ''

    idx = 0
    for i in range(len(s)):
        if s[i] == ' ':
            idx = 0
            answer += ' '
            continue

        if idx == 0 or idx % 2 == 0:
            answer += s[i].upper()
        elif idx % 2 != 0:
            answer += s[i].lower()
        idx += 1

    return answer