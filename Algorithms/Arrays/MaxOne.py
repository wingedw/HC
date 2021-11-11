def findMaxConsecutiveOnes(nums):
        total = 0
        max1 = 0
        for x in nums:
            if x == 1:
                total += 1
            else:
                max1 = max(max1,total)
                total = 0
        
        return max(max1,total)

nums = [1,1,0,1,1,1]

print (findMaxConsecutiveOnes(nums))