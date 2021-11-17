'''
Given an array nums of n integers, return an array of all the unique 
quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
'''

def fourSum(nums, target):
    result = []
    n = len(nums)
    nums.sort()

    for i in range(n):
        if nums[i] > target:
            i += 1
            break
        


    return result


nums = [1,0,-1,0,-2,2] 
target = 0

print (fourSum(nums,target))