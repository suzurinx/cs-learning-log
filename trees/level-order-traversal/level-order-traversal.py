from collections import deque


class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# 二分木構造を作る
def toBinaryTree(lst):
    # バリテーション
    # []でもエラーを返さないように設計
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

# 階層走査しリスト化する
def levelOrderTraversal(root):
    if root is None:
        return []
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        if node is None:
            result.append(None)
            continue
        result.append(node.data)
        queue.append(node.left)
        queue.append(node.right)
    while result[-1] is None:
        result.pop()
    return result

# テストケース
print(levelOrderTraversal(toBinaryTree([0,-10,5,None,-3,None,9])))
print(levelOrderTraversal(toBinaryTree([5,2,18,-4,3])))
print(levelOrderTraversal(toBinaryTree([27,14,35,10,19,31,42])))
print(levelOrderTraversal(toBinaryTree([30,15,60,7,22,45,75,None,None,17,27])))
print(levelOrderTraversal(toBinaryTree([90,50,150,20,75,95,175,5,25,66,80,92,111,166,200])))
print(levelOrderTraversal(toBinaryTree([50,17,76,9,23,54,None,None,14,19,None,None,72])))
print(levelOrderTraversal(toBinaryTree([16,14,10,8,7,9,3,2,4,1])))