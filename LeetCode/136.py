def singleNumber(nums) -> int:
    result = 0
    for n in nums:
        print(result)
        result ^= n
    return result
print(singleNumber([5,1,2,1,2]))
