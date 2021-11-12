'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''
def twoSum(nums, target):
    '''
    DOES NOT WORK
    I originally thought that two point would work but logic breaks when you 
    your params are something like nums = [3,2,4] target = 6
    See LeetCode_1.py in hashtables for working solution.
    '''
    i = 0
    j = len(nums)-1
    result = []
    
    while i < j:
        _temp = nums[i] + nums[j]
        if  _temp == target:
            result = [i,j]
            break
        else:
            if _temp > target:
                if nums[i] > nums[j]:
                    i += 1
                else:
                    j -= 1
            else:
                if nums[i] > nums[j]:
                    j -= 1
                else:
                    i += 1
    return result

nums = [3,2,4]
target = 6
# answer should be [1,2]
print (twoSum(nums,target))