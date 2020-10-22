def hammingDistance(x: int, y: int) -> int:
    return bin(x ^ y).count('1')

print(hammingDistance(1, 4))
