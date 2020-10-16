def search(nums, target: int) -> int:
    try:
        return nums.index(target)
    except ValueError:
        return -1
print(search([4,5,6,7,0,1,2], 33))
