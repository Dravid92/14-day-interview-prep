"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""
# brute force
def max_sliding_window(nums, k):
    l , r = 0, k
    res = []
    while r<=len(nums):
        sub_arr = nums[l:r]
        print(sub_arr)
        max_value = max(sub_arr)
        res.append(max_value)
        l += 1
        r += 1
    return res
from collections import deque
# efficient
def eff_max_sliding_window(nums, k):
    i, j = 0, k-1
    q = deque()
    while q and nums[i] > nums[q[-1]]:
            q.pop()
        
    for i in range(k):
        q.append(nums[i])

    

    q = i



nums = [1]
k = 1
print(max_sliding_window(nums, k))



arr = [1,3,-1,-3,5,3,6,7]
largest = second_largest = 0
for n,i in enumerate(arr):
     if i > arr[largest]:
          largest = n

arr.pop(largest)
# print(arr[largest])
print(arr)
for k in arr:
     if k > second_largest:
          second_largest = k

print(second_largest)
    