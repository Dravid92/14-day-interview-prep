"""
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
"""

def three_sum(nums):
    #sum should be equal to zero
    nums.sort()
    res = []
    for i in range(len(nums)):
        j, k = i+1 , len(nums)-1
        if i>0 and nums[i] == nums[i-1]:
            continue
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total == 0:
                j += 1
                k -= 1
                res.append([nums[i], nums[j], nums[k]])
                if j< k and nums[j] == nums[j-1]:
                    j += 1
                if j<k and nums[k] == nums[k+1]:
                    k -=1
            elif total > 0:
                k -= 1
            else:
                j += 1
    return res


nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))



