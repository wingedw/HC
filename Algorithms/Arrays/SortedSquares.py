def sortedSquares(nums):
    res = []
    
    for x in nums:
        y = x * x
        res.append(y)
    
    return sorted(res)

nums = [-4,-1,0,3,10]

print(sortedSquares(nums))