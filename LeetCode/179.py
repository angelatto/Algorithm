# 풀이1 - 모든 경우의 수 구하기 ------> time limit exceeded !!!
# : """모든 조합"""을 구해서 다시 int로 구해서 max를 찾기
# 풀이2
# : 하나씩 값을 붙여가면서 가장 큰 수 """하나"""를 만들어간다. -> 즉, 삽입정렬!!
def to_swap(n1:int, n2:int) -> bool:
    return str(n1)+str(n2) < str(n2)+str(n1)

def largestNumber(nums) -> str:
    i = 1
    while i < len(nums):
        j = i
        while j > 0 and to_swap(nums[j-1], nums[j]):
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1
        i += 1
    return str(int(''.join(map(str, nums))))

print(largestNumber([9,6,3,0,7,4,1,8,5,2]))
