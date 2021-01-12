# 폰켓몬 
def solution(nums): # len(nums) 항상 짝수
    size = len(nums) / 2

    len_set = len(set(nums))
    if len_set >= size:
        return size
    return len_set

print([3,1,2,3])
