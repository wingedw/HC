def BinarySearch(arr, target):
    #Return an index in sorted array of the 
    #target value if doesnt exist return -1
    l = 0
    r = len(arr)-1

    while l + 1 < r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            l = mid
        else:
            r = mid
    # Post Processing       
    if arr[l] == target:
        return l
    if arr[r] == target:
        return r
    return -1

arr = [1,2,2,3,4,5,6,7,8,9]
target = 91
print (BinarySearch(arr, target))

