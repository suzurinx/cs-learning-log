from collections import deque

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def toBinaryTree(lst):
    if not lst:
        return None
    root = BinaryTree(lst[0])
    queue = deque([root])
    i = 1
    while queue:
        node = queue.popleft()
        if i < len(lst) and lst[i] is not None:
            node.left = BinaryTree(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = BinaryTree(lst[i])
            queue.append(node.right)
        i += 1
    return root

def symmetricTree(root):
    if root is None:
        return True
    def helper(left, right):
        # ベースケース
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.data != right.data:
            return False
        # ここまでがベースケース
        return helper(left.left, right.right) and helper(left.right, right.left)
    return helper(root.left, root.right)

# テストケース
print(symmetricTree(toBinaryTree([10,25,25,33,45,45,33])))
print(symmetricTree(toBinaryTree([10,25,25,33,45,45,32])))
print(symmetricTree(toBinaryTree([1,2,2,3,4,4,3])))
print(symmetricTree(toBinaryTree([3,6,6,9,12,11,9])))
print(symmetricTree(toBinaryTree([])))
print(symmetricTree(toBinaryTree([1,9,9,15,19,19,15])))
print(symmetricTree(toBinaryTree([1,2,2,None,3,None,3])))
print(symmetricTree(toBinaryTree([3,6,6,9,12,12,9])))
print(symmetricTree(toBinaryTree([3,6,7,9,12,12,9])))
print(symmetricTree(toBinaryTree([1,2,2,2,None,2])))
print(symmetricTree(toBinaryTree([1,2,3])))