def firstmatching(arr,target):
    # Find the first element in sorted array
    # that matches target value.
    l = 0
    r = len(arr) - 1

    if arr[0] == target: return 0

    while l +1 < r:
        mid = l + (r - l) // 2
        if arr[mid] == target:
            r = mid
        elif arr[mid] < target:
            l = mid
        else:
            r = mid
    
    #Post Process
    if arr[l] == target: return l
    if arr[r] == target: return r

    return -1

arr = [1,2,2,2,2,4,5,6,7,7,8]
target = 2
print(firstmatching(arr,target))