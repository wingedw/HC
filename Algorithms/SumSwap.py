'''
Swap single number from two lists to make the sum of each list equal
if possible return [number from list1, number from list 2]
if not possible return []
'''
def SumSwap(arr1,arr2):
    res = []
    dict_arr2 = {}
    arr1sum = sum(arr1)
    arr2sum = sum(arr2)
    
    if (arr1sum+arr2sum)% 2 != 0: # if sum is odd swaps wont work
        return res
       
    if arr1sum == arr2sum: # already equal
        return res

    delta = abs(arr1sum-arr2sum)
 
    for i in arr2:
        if i not in dict_arr2.keys():
            dict_arr2.update({i:1})

    for num in arr1:
        target = delta - num
        if target > 0 and dict_arr2[target]:
            return [num,target]

    return res

arr1 = [1,2,2,1,1,4]
arr2 = [3,6,3,3]

print (SumSwap(arr1,arr2))