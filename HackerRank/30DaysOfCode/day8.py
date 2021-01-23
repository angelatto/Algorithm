# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
dic = {}
for _ in range(n):
    key, value = input().split()
    dic[key] = value

while True:
    try:
        name = input()
        if name in dic:
            print(name + '=' + dic[name])
        else:
            print('Not found')
    except EOFError:
        break
