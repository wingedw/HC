def maxDepth(root) -> int:
    if not root:
        return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    
    return(max(left,right)+1)
    
root = [3,9,20,None,None,15,7]
print (maxDepth(root))
