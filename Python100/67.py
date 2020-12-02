def solution(n):
    people = 0
    total = 0

    while(True):
        total = people*(people-1)/2
        if n<total:
            break
        people+=1
    times = int(n - (people-1)*(people-2)/2)

    return [times, people]

print(solution(59))
