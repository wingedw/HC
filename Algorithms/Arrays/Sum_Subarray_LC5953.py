'''
You are given an integer array nums. The range of a subarray of 
nums is the difference between the largest and smallest element 
in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within 
an array.'''

def subArrayRanges(nums):
    res = 0
    for i in range(len(nums)):
        _min = float("inf")
        _max = -float("inf")
        for j in range(i, len(nums)):
            _max = max(_max, nums[j])
            _min = min(_min, nums[j])
            res += _max - _min
    return res

#nums = [1,2,3] # answer 4
nums = [4,-2,-3,4,1] # answer 59

print (subArrayRanges(nums))