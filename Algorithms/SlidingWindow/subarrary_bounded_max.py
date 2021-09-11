"""
795. Number of Subarrays with Bounded Maximum
Given an integer array nums and two integers left and right,
return the number of contiguous non-empty subarrays such that
the value of the maximum array element in that subarray is in 
the range [left, right].

Example 1:

Input: nums = [2,1,4,3], left = 2, right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
Example 2:

Input: nums = [2,9,2,5,6], left = 2, right = 8
Output: 7
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= left <= right <= 10^9

The test cases are generated so that the answer will fit in a 32-bit integer.
Runtime: 480 ms, faster than 71.19% of Python online 
submissions for Number of Subarrays with Bounded Maximum.
Memory Usage: 19.7 MB, less than 10.17% of Python online 
submissions for Number of Subarrays with Bounded Maximum.
"""

def numSubarrayBoundedMax(nums, left, right) -> int:
    res = 0
    count = 0
    start = 0
    for end in range(len(nums)):
        #print(val,nums[end])
        if nums[end] >= left and nums[end] <= right:
            count = end - start +1
            res += count
            #print(count,res)
        elif nums[end] < left:
            res += count
        else:
            start = end + 1
            count = 0
    return res
            
      
nums = [2,9,2,5,6]

left = 2
right = 8

print (numSubarrayBoundedMax(nums, left, right))