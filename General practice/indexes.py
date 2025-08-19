nums = [3, 3]
target = 6

for i in nums:
    for j in range(nums.index(i) + 1 , len(nums)):
        if target == i + nums[j]:
            ind_list = [nums.index(i), j]
            print(ind_list) 