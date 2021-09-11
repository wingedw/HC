"""
Find the smallest sub list with a sum greater
 than or equal to S
Params
arr = list of positive integers
s = integer
"""
def small_sub_list(arr, s):
    sub_min_size = float('inf')
    current_sum = 0
    left = 0
    for right, val in enumerate(arr):
        current_sum += val
        while current_sum >= s:
            sub_min_size = min(sub_min_size, right - left +1)
            current_sum -= arr[left]
            left += 1
    return sub_min_size

arr = [2, 4, 1, 3, 5, 5, 1]
s = 11

print (small_sub_list(arr, s))


