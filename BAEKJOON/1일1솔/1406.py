"""
01.07.22
실버3

<교훈>
1. 디버깅의 중요성
2. 입력 시 엔터제거 ->  sys.stdin.readline().strip()
3. 자료구조 선택 시 주의하기
-> 리스트나 문자열의 삽입, 삭제는 O(N) >> but, 스택이나 deque의 pop, push는 O(1)

<문제 해결 아이디어>
문제에서 커서는 문장의 맨 앞, 문장의 맨 뒤, 문장의 중간중간 위치한다고 했는데
-> 여기서 스택 자료구조를 사용할 힌트를 얻어야 한다.
'커서를 기준으로' 문장을 커서 앞 뒤로 스택 2개로 쪼갠다.
그럼 커서 앞에 문자를 제거한다는 것은 첫번째 스택에 pop()하는 것과 같은 의미이다.
그럼 문자열 중간에 문자를 삽입 또는 삭제하는 것은 O(N)인 것과 비교할 때
자료구조를 달리한다면 시간을 많이 단축시킬 수 있다.


L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
P $	$라는 문자를 커서 왼쪽에 추가함

"""
import sys

str = sys.stdin.readline().strip()
num = int(sys.stdin.readline().strip())
stack_front = list(str)
stack_back = []

for _ in range(num):
    line = sys.stdin.readline().split()
    cmd = line[0]
    if len(line) > 1:
        x = line[1]

    if cmd == 'L':
        if stack_front:
            stack_back.append(stack_front.pop())
    elif cmd == 'D':
        if stack_back:
            stack_front.append(stack_back.pop())
    elif cmd == 'B':
        if stack_front:
            stack_front.pop()
    elif cmd == 'P':
        stack_front.append(x)


print(''.join(stack_front) + ''.join(reversed(stack_back)))