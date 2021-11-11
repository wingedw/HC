def findNumbers(nums):
        evens = 0
        
        for  x in nums:
            if len(str(x)) % 2 == 0:
                evens += 1
        return evens

nums = [12,345,2,6,7896]
print(findNumbers(nums))