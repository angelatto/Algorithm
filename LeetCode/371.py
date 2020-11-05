def getSum(a: int, b: int) -> int:
    MASK = 0xFFFFFFFF
    INT_MASk = 0x7FFFFFFF

    while b != 0:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

    if a > INT_MASk:
        a = ~(a ^ MASK)
    return a
print(getSum(1, 2))
