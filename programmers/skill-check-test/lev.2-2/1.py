def solution(citations):
    h = 0

    for h in range(max(citations), -1, -1):
        a, b = 0, 0
        for c in citations:
            if c >= h:
                a += 1
            else:
                b += 1
        if a + b == len(citations) and a >= h:
            break

    return h