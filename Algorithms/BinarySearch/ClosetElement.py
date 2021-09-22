def closestelement(arr, target):
    # Return the index of the value that is closest
    # to the target value tie goes to the lower value.
    
    l = 0
    r = len(arr)-1

    while l + 1 < r:
        mid = l + (r - l) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            l = mid
        else:
            r = mid
    
    #Post Processing
    if abs(target - arr[l]) <= abs(target - arr[r]):
        return l
    else:
        return r

arr = [-3,-1,3,5,7,8,9,12,13,16]
target = 1
print (closestelement(arr, target))   
        