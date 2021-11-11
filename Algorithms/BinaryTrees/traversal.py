def preorder_lazy(root):
    # check arg before using
  if not root: return
  print(root.val)
  preorder_lazy(root.left)
  preorder_lazy(root.right)

def preorder_eager(root):
    # check for null before passing arg
  print(root.val)
  if root.left: preorder_eager(root.left)
  if root.right: preorder_eager(root.right)

def inorder(root):
  if not root: return
  inorder(root.left)
  print(root.val)
  inorder(root.right)

def postorder(root):
  if not root: return
  postorder(root.left)
  postorder(root.right)
  print(root.val)

from collections import deque

def levelOrder(root):  
    # lazy check before using arg
  Q = deque()
  Q.append(root)
  while Q:
    node = Q.popleft()
    if not node: continue
    print(node)
    Q.append(node.left)
    Q.append(node.right)

def levelOrder_eager(root):
    # check before passing arg
  Q = deque()
  if root: Q.append(root)
  while Q:
    #node is guaranteed not null
    node = Q.popleft()
    print(node)
    if node.left: Q.append(node.left)
    if node.right: Q.append(node.right)
