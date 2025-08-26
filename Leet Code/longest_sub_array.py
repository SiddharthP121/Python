# def longest_sub_array(array):
#     if 0 not in array:
#         array.remove(1)
#         return array
#     sub_array = []
#     longest_subarray = []
#     for i in array:
#         if i == 0:
#             longest_subarray = sub_array.copy() if len(longest_subarray) < len(sub_array) else longest_subarray
#             sub_array.clear()
#             continue
#         sub_array.append(i)
#         longest_subarray = sub_array.copy() if len(longest_subarray) < len(sub_array) else longest_subarray
#     return longest_subarray
    
# array = [1, 1, 1, 1, 1]
# print(longest_sub_array(array))
    

class Solution(object):
    def longestSubarray(self, nums):
        if 0 not in nums:
            nums.remove(1)
            return len(nums)
        sub_array = []
        longest_sub_array = []
        for i in nums:
            if i == 0:
                longest_sub_array = sub_array if len(longest_sub_array) < len(sub_array) else longest_sub_array
                sub_array = []
                continue
            sub_array.append(i)
        longest_sub_array = sub_array if len(longest_sub_array) < len(sub_array) else longest_sub_array
        return len(longest_sub_array)

nums = [1,1,0,1]
        
a = Solution()

print(a.longestSubarray(nums))