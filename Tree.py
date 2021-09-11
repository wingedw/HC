class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
      if self.data:
        if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
      else:
         self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
    def maxDepth(self, root, depth = 0) -> int:
        if root == None:
            return depth
        return max(self.maxDepth(root.left,depth+1),self.maxDepth(root.right,depth+1))

root = Node(12)
root.insert(14)
root.insert(6)
root.insert(3)
root.insert(15)
root.PrintTree()
print(root.maxDepth(root))




