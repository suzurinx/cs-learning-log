from collections import deque

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data =data
        self.left = left
        self.right = right
""""
# ループ型:BSTにkeyのノードを追加する
def bstInsert(root,key):
    if not root:
        return BinaryTree(key)
    iterator = root
    while iterator is not None:
        if key < iterator.data:
            if iterator.left is None:
                iterator.left = BinaryTree(key)
                break
            iterator = iterator.left
        elif key > iterator.data:
            if iterator.right is None:
                iterator.right = BinaryTree(key)yatto
                break
            iterator = iterator.right
        else:
            break
    return root
"""
"""
# 再帰型：木構造を作成する
def toBinaryTree(lst):
    def helper(i):
        if i >= len(lst):
            return None
        root = BinaryTree(lst[i])
        root.left = helper(2 * i + 1)
        root.right = helper(2 * i + 2)
        return root
    return None if not lst else helper(0)
"""
# BFS型：木構造を作成する
def toBinaryTree(lst):
    if not lst:
        return None
    root = BinaryTree(lst[0])
    queue = deque()
    queue.append(root)
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

# 再帰型：BSTにkeyのノードを追加する
def bstInsert(root,key):
    if not root:
        return BinaryTree(key)
    if key < root.data:
        root.left = bstInsert(root.left, key)
    elif key > root.data:
        root.right = bstInsert(root.right, key)
    return root

# 作成した木構造をリストに戻す
def binaryTreeToList(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            result.append(None)
        else:
            result.append(node.data)
            queue.append(node.left)
            queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result

# テストケース
print(binaryTreeToList(bstInsert(toBinaryTree([0,-10,5,None,-3,None,9]), 20)))
print(binaryTreeToList(bstInsert(toBinaryTree([0,-10,5,None,-3,None,9]), 2)))
print(binaryTreeToList(bstInsert(toBinaryTree([5,2,18,-4,3,None,None]), 3)))
print(binaryTreeToList(bstInsert(toBinaryTree([5,2,18,-4,3,None,None]), 10)))
print(binaryTreeToList(bstInsert(toBinaryTree([27,14,35,10,19,31,42]), 15)))
print(binaryTreeToList(bstInsert(toBinaryTree([27,14,35,10,19,31,42]), 23)))
print(binaryTreeToList(bstInsert(toBinaryTree([30,15,60,7,22,45,75,None,None,17,27]), 8)))
print(binaryTreeToList(bstInsert(toBinaryTree([90,50,150,20,75,95,175,5,25,66,80,92,111,166,200]), 79)))
print(binaryTreeToList(bstInsert(toBinaryTree([50,17,76,9,23,54,None,None,14,19,None,None,72]), 57)))
print(binaryTreeToList(bstInsert(toBinaryTree([16,14,10,8,7,9,3,2,4,1]), 35)))