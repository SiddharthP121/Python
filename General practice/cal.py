'''
You have given a list of numbers let nums = [12, 34, 3, 6, 7]
You will be returning the maximum sum from this list according to the formulla 
(nums[i] - nums[j]) * nums[k]

'''

nums = [2, 3, 1]
# max = 0

# for i in range(0, len(nums)):
#     for j in range(i, len(nums)):
#         for k in range(j, len(nums)):
#             cal = (nums[i] - nums[j]) * nums[k] if (nums[i] - nums[j]) * nums[k] > 0 else 0
#             if max < cal:
#                 max = cal
#                 triplets = (i, j, k)

# print(triplets, max)

triplet = [[i, j, k] for i in range(0, len(nums)) for j in range(i, len(nums)) for k in range(0, len(nums)) if ]
print(triplet)