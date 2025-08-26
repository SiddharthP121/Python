"""

class Solution(object):
    def longestSubarray(self, nums):
        if 0 not in nums:
            nums.remove(1)
            return len(nums)
        sub_array = []
        longest_sub_array = []
        count = 0
        r = 0
        for i in range(r, len(nums)):
            if nums[i] == 0:
                count += 1
                if count > 1:
                    r = i 
                    sub_array = []
                    break
                continue
            else:
                sub_array.append(nums[i]) 
            longest_sub_array = sub_array if len(sub_array) > len(longest_sub_array) else longest_sub_array    

        return longest_sub_array
     
array = [0,1,1,1,0,1,1,0,1]
a = Solution()
print(a.longestSubarray(array))

"""

class Solution(object):
    def longestSubarray(self, nums):
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
                print(zero_count)

            while zero_count > 1:
                print(zero_count)
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # We delete one element, so subtract 1
            max_len = max(max_len, right - left)

        return max_len

array = [0,1,1,1,0,1,1,0,1]
a = Solution()
print(a.longestSubarray(array))