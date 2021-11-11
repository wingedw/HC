def groupSum(nums, start = 0, target = 0):
    if not nums:
        return False
    if start >= len(nums):
        return target == 0
    if (groupSum( nums, start + 1, target - nums[start])):
         return True
    if (groupSum( nums, start + 1, target)):
         return True

    return False


nums = [2, 4, 8, 3]
print (groupSum(nums, 0, 10))
print (groupSum(nums, 0, 14))
print (groupSum(nums, 0, 9))