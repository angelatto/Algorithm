"""
문자열 폭발 (lev.gold-4)
- 대소문자 고려 안했음
-> 이 문제는 틀린문제임 while문 안써도 돌아감. 즉, 반복문 1번만 돌면 해결되는 테스트케이스만 존재.
-> 내 코드에서 while문 지우고 돌려도 정답처리됨.

idea : 문자열에서 하나씩 스택에 넣는다.
-> 넣은 값이 target의 마지막 문자와 같다면 스택에서 끝에서부터 그 타겟의 길이만큼 확인하고 같으면 그 타켓만큼 pop

"""
s = input()
target = input()

while True:
    if s == '':
        break
    flag = True
    stack = []
    for c in s:
        stack.append(c)
        if c == target[-1] and ''.join(stack[len(stack)-len(target):]) == target:
            flag = False
            for _ in range(len(target)):
                stack.pop()
    s = ''.join(stack)
    if flag:
        break

if s == '':
    print('FRULA')
else:
    print(s)