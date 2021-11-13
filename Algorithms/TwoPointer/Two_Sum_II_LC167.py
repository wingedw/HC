'''
Given a 1-indexed array of integers numbers that is already sorted in 
non-decreasing order, find two numbers such that they add up to a 
specific target number. Let these two numbers be numbers[index1] and 
numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by 
one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. 
You may not use the same element twice.

This only works if array is sorted
'''
def twoSum(numbers, target):
    result = []
    i = 0
    j = len(numbers)-1
    result = []
    
    while i < j:
        _temp = numbers[i] + numbers[j]
        if  _temp == target:
            result = [i,j]
            break
        else:
            if _temp > target:
                if numbers[i] > numbers[j]:
                    i += 1
                else:
                    j -= 1
            else:
                if numbers[i] > numbers[j]:
                    j -= 1
                else:
                    i += 1
    return result


numbers = [2,7,11,15] 
target = 9
print (twoSum(numbers, target))