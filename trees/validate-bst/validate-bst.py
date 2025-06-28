from collections import deque

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# 木構造を作る
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

# inOrder判定
def validateBST(root):
    values = []
    def inOrder(node):
        if node is None:
            return None
        inOrder(node.left)
        values.append(node.data)
        inOrder(node.right)
    inOrder(root)
    for i in range(1, len(values)):
        if values[i] <= values[i-1]:
            return False
    return True

"""
# 有効な二分木を判定する
# 再帰
def validateBST(root):
    def helper(node, minValue, maxValue):
        if node is None:
            return True
        if not minValue < node.data < maxValue:
            return False
        return helper(node.left, minValue, node.data) and helper(node.right, node.data, maxValue)
    return helper(root, float('-inf'), float('inf'))
"""

# テストケース
print(validateBST(toBinaryTree([0,None,-1])))
print(validateBST(toBinaryTree([4,1,5]) ))
print(validateBST(toBinaryTree([15,10,20,8,12,16,25])))
print(validateBST(toBinaryTree([30,15,60,7,22,45,75,None,None,17,27])))
print(validateBST(toBinaryTree([5,1,2,3,4])))
print(validateBST(toBinaryTree([5,1,4,None,None,3,6])))
print(validateBST(toBinaryTree([])))
print(validateBST(toBinaryTree([5,3,9,1,6,8])))
print(validateBST(toBinaryTree([1])))
print(validateBST(toBinaryTree([1,2])))