def remove_duplicates(nums, value):
    i = 0
    while i < len(nums):
        if nums[i] == value:
            nums.pop(i)
        else:
            i += 1
    print(nums)
    

nums = [1, 1, 2, 3]
remove_duplicates(nums, 1)

