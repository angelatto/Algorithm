"""
A와 B (lev.gold-5)
- 문자열 문제
- 두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임이다.
- 문자열을 바꿀때는 두 가지 연산만 가능

- 문자열의 뒤에 A를 추가한다.
- 문자열을 뒤집고 -> 뒤에 B를 추가한다.

S를 T로 바꿀 수 있으면 1을 없으면 0을 출력하기

bucket 배열 만들고 -> 순열로 모든 경우의 수 해보기 -> 시간 초과
idea : s를 t로 만들려면 경우의 수를 다 생각해야 하므로
반대로 t에서 s를 만들어가면서 가능 여부를 판단한다.

t에서 A가 나오면 pop
B가 나오면 pop하고 뒤집는다.

"""
s = list(input())  # B
t = list(input())  # ABBA

while len(s) != len(t):
    c = t.pop()
    if c == 'B':
        t = t[::-1]
print(1 if s == t else 0)