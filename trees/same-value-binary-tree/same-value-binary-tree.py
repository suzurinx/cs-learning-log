class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
""""
# ラップ型
def treeWithTheSameValue(root):
    if not root:
        return True
    return treeWithTheSameValueHelper(root, root.data)

def treeWithTheSameValueHelper(root, value):
    if root is None:
        return True
    if root.data != value:
        return False
    return treeWithTheSameValueHelper(root.left, value) and treeWithTheSameValueHelper(root.right, value)
"""

"""
# ネスト型
def treeWithTheSameValue(root):
    if not root:
        return True
    def helper(root, value):
        if root is None:
            return True
        if root.data != value:
            return False
        return helper(root.left,value) and helper(root.right, value)
    return helper(root, root.data)
"""

"""
# キュー
def treeWithTheSameValue(root):
    if not root:
        return True
    value = root.data
    queue = [root]
    while queue:
        current = queue.pop(0)
        if current.data != value:
            return False
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return True
"""

# スタック
def treeWithTheSameValue(root):
    if not root:
        return True
    value = root.data
    queue = [root]
    while queue:
        current = queue.pop()
        if current.data != value:
            return False
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return True

# キュー
def toBinaryTree(arrList):
    if not arrList:
        return None
    root = BinaryTree(arrList[0])
    queue = [root]
    i = 1
    while queue and i < len(arrList):
        current = queue.pop(0)
        if arrList[i] is not None:
            current.left = BinaryTree(arrList[i])
            queue.append(current.left)
        i += 1
        if i < len(arrList) and arrList[i] is not None:
            current.right = BinaryTree(arrList[i])
            queue.append(current.right)
        i += 1
    return root

"""
# スタック
def toBinaryTree(arrList):
    if not arrList:
        return None
    root = BinaryTree(arrList[0])
    queue = [root]
    i = 1
    while queue and i < len(arrList):
        current = queue.pop()
        if arrList[i] is not None:
            current.left = BinaryTree(arrList[i])
            queue.append(current.left)
        i += 1
        if i < len(arrList) and arrList[i] is not None:
            current.right = BinaryTree(arrList[i])
            queue.append(current.right)
        i += 1
    return root
"""
"""
# ラップ
def toBinaryTree(arrList):
    if not arrList:
        return None
    return toBinaryTreeHelper(arrList, 0)

def toBinaryTreeHelper(arrList, i):
    if i >= len(arrList) or arrList[i] is None:
        return None
    root = BinaryTree(arrList[i])
    root.left = toBinaryTreeHelper(arrList, 2 * i + 1)
    root.right = toBinaryTreeHelper(arrList, 2 * i + 2)
    return root
"""

"""
# ネスト
def toBinaryTree(arrList):
    if not arrList:
        return None
    def helper(i):
        if i >= len(arrList) or arrList[i] is None:
            return None
        root = BinaryTree(arrList[i])
        root.left = helper(2 * i + 1)
        root.right = helper(2 * i + 2)
        return root
    return helper(0)
"""

# テストケース
print(treeWithTheSameValue(toBinaryTree([0])))             # → True
print(treeWithTheSameValue(toBinaryTree([0,1,2])))         # → False
print(treeWithTheSameValue(toBinaryTree([0,0,0,0,0,None,0]))) # → True
print(treeWithTheSameValue(toBinaryTree([1,1,1,7,1])))     # → False