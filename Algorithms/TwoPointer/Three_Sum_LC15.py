
'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
 such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''
def threeSum(nums):
    result = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i - 1] != nums[i]:
            twoSum(nums, i, result)
    return result
    
def twoSum(numbers, i, result):

    left = i + 1
    right = len(numbers)-1

    while left < right:
        _temp = numbers[i] + numbers[left] + numbers[right]
        if _temp < 0:
            left += 1
        elif _temp > 0:
            right -= 1
        else:
            result.append([numbers[i], numbers[left], numbers[right]])
            left += 1
            right -= 1
            # make sure we do not do a repeat three sum
            while left < right and numbers[left] ==  numbers[left - 1]:
                left += 1



nums = [-1,0,1,2,-1,-4]
print (threeSum(nums))