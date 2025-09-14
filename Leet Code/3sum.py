'''
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''

'''
def sum_triplet(l):
    triplet_list = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            for k in range(j, len(l)):
                rule = i != j and i != k and j != k
                if l[i] + l[j] + l[k] == 0 and rule:
                    triplet = [l[i], l[j], l[k]]
                    triplet.sort()
                    if triplet not in triplet_list:
                        triplet_list.append(triplet) 
    return triplet_list

nums = nums = [-1,0,1,2,-1,-4]
print(sum_triplet(nums))
'''
'''

def sum0(a, b, c):
    if a + b + c == 0:
        return [a, b, c]
nums = [-1,0,1,2,-1,-4]
list_ = {tuple(sorted((nums[i], nums[j], nums[k]))) 
         for i in range(len(nums)) 
         for j in range(i, len(nums)) 
         for k in range(j, len(nums)) 
         if nums[i] + nums[j] + nums[k] == 0 and i != j and i != k and j != k }

list1 = [list(triplet) for triplet in list_]
print(list1)

'''


'''
nums = [-1,0,1,2,-1,-4]
nums_list = []
n = 0
for i in range(n, len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            if nums[i] + nums[j] + nums[k] == 0 and i != j and i != k and j != k and sorted([nums[i], nums[j], nums[k]]) not in nums_list:
                nums_list.append(sorted([nums[i], nums[j], nums[k]]))
            n = j+1

print(nums_list)

'''
nums = [-1,0,1,2,-1,-4]
n = 0
nums_list = []
while n <= len(nums):
    for i in range(n, len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0 and i != j and  i != k and j != k and sorted([nums[i], nums[j], nums[k]]) not in nums_list:
                    nums_list.append(sorted([nums[i], nums[j], nums[k]]))
                    n = j+1
                    break
            

print(nums_list)


