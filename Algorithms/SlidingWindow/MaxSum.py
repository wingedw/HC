"""
Find maximum sum of any contiguous subarray of size k
Brute Force
Iterate over entire array comparing with 
nested for loop
O(n^2)

Best?
Use sliding window compare current value with stored
maximum value
O(n)
"""
def max_sum_subarray(arr,k):
    max_sum = float('-inf')
    left = 0
    current_sum = 0
    for right, val in enumerate(arr):
        current_sum += val
        #print (left,right, current_sum)
        if right -left + 1 == k:
            max_sum = max(max_sum, current_sum)
            #subtract first value of substring
            current_sum -= arr[left]
            left += 1
    return max_sum

arr = [2,3,4,1,5,1,2]
k = 3
print (max_sum_subarray(arr,k))