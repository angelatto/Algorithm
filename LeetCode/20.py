def isValid(s: str) -> bool:
    stack = []
    table = {
        ')':'(',
        '}':'{',
        ']':'['
    }

    for c in s:
        if c not in table: # 시작괄호는 넣어주기
            stack.append(c)
        elif not stack or table[c] != stack.pop():
            return False
    return not stack
print(isValid("})"))
