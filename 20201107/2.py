def solution(s, op):
    answer = []
    for i in range(1, len(s)): 
        if op == "+":
            answer.append(int(s[:i]) + int(s[i:]))
        if op == "-":
            answer.append(int(s[:i]) - int(s[i:]))
        if op == "*":
            answer.append(int(s[:i]) * int(s[i:]))
    return answer

print(solution("1234", "+"))
