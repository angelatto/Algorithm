def sortColors(nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        red, while, blue -> 0,1,2
        pivot이 1인 퀵 정렬이다.
        네덜란드 국기 문제이다.
        O(1) constant space
        """
        print(nums)

        red, white, blue = 0, 0, len(nums)-1

        while white <= blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] > 1:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
            else:
                white += 1

        print(nums)
sortColors([2,0,2,1,1,0])
