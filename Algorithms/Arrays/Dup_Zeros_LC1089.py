'''
Given a fixed-length integer array arr, duplicate each occurrence of zero, 
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. 
Do the above modifications to the input array in place and do not return anything.
'''
def duplicateZeros(arr):
    zero_count = 0
    n = len(arr)-1
    
    for i in range(n):
        if i > n - zero_count:
            break
        if arr[i] == 0:
            
            if i == n - zero_count:# This takes care of edge case that last digit to keep is a zero do not dupe it
                arr[n] = 0
                n -= 1
                break
            zero_count += 1
    last_num = n - zero_count

    for i in range(last_num, -1, -1):
        if arr[i] == 0:
            arr[i + zero_count] = 0
            zero_count -= 1
            arr[i + zero_count] = 0
        else:
            arr[i + zero_count] = arr[i]
    return arr


arr = [1,0,2,3,4,0,5,0]

print (duplicateZeros(arr))