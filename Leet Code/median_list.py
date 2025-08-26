import math
'''

def median_part(res):
    if len(res) % 2 == 1:
        median = math.floor(len(res) / 2)
        print(median)
        print(res[median])
    else:
        median_1 = int(len(res) / 2)
        median_2 = int(len(res) / 2 - 1)
        print(median_1, median_2)
        print((res[median_1] + res[median_2]) / 2)

nums_1 = [ 1, 2 ]
nums_2 = [ 3, 4 ]

res = nums_1 + nums_2
res.sort()
median_part(res)
'''

def find_median_simple(nums1, nums2):
    """Merges two lists, sorts them, and finds the median."""
    res = nums1 + nums2
    res.sort()
    n = len(res)

    if n == 0:
        return None

    # This approach works for both odd and even length lists
    mid1_idx = (n - 1) // 2
    mid2_idx = n // 2
    return (res[mid1_idx] + res[mid2_idx]) / 2

# Example Usage
nums_1 = [1, 2]
nums_2 = [3, 4]
print(f"The median of the resultant array is {find_median_simple(nums_1, nums_2)}")