"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

"""
# O(n3) -> summing part within the first loop and carry over -> O(n2) ->  
nums = [-2,1,-3,4,-1,2,1,-5,4]
l, r = 0, 1
max_sub_array = nums[1]

def max_sub_array(nums):
    total = 0
    res = nums[0]
    start, end = 0, 0
    for n, i in enumerate(nums):
        # if total < 0:
        #     total = 0
            # start = n
        total += i
        # if total > res:
        #     end = n
        res = max(total, res)
    return res

print(max_sub_array(nums))
