user_input = list(map(int, input().split(' ')))
print(user_input)

def sol(l):
    last = max(user_input)
    if sum(user_input) == sum(range(1, last+1)):
        return 'YES'
    return 'NO'

    # l = sorted(l)
    # for i in range(len(l) - 1):
    #     if l[i]+1 != l[i+1]:
    #         return 'NO'
    # return 'YES'
print(sol(user_input))
