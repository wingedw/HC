'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''
def twoSum(nums, target):
    hashtable = {}
    result = []
    
    for i in range(len(nums)):
        hashtable[nums[i]] = i
    for i in range(len(nums)):
        requiredval = target - nums[i]
        if requiredval in hashtable and hashtable[requiredval] != i:
            result = [i, hashtable[requiredval]]
            break


    return result

nums = [3,2,4]
target = 6
# answer should be [1,2]
print (twoSum(nums,target))