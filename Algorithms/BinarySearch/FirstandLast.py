def searchRange(nums, target):
# Given an array of integers nums sorted in 
# ascending order, find the starting and 
# ending position of a given target value.
# LC 34
    l = 0
    r = len(nums) - 1
    lower = -1
    upper = -1

    if not nums: return [lower,upper]
    #Get Lower
    while l + 1 < r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            r = mid
        elif nums[mid] < target:
            l = mid
        else:
            r = mid
    if nums[l] == target: lower = l
    elif nums[r] == target: lower = r
    
    # Get upper
    l = 0
    r = len(nums) - 1
    while l + 1 < r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            l = mid
        elif nums[mid] < target:
            l = mid
        else:
            r = mid
    if nums[r] == target: upper = r
    elif nums[l] == target: upper = l

    return [lower, upper]

arr = [1,2,2,2,2,4,5,6,7,7,8]
target = 1
print(searchRange(arr,target))