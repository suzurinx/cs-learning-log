from collections import deque

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def toBinaryTree(arrList):
    # エッジケース:空リストを除外
    # is Noneの形といつも迷う
    if not arrList:
        return None
    root = BinaryTree(arrList[0])
    queue = deque()
    queue.append(root)
    i = 1
    while queue:
        node = queue.popleft()
        if i < len(arrList) and arrList[i] is not None:
            node.left = BinaryTree(arrList[i])
            queue.append(node.left)
        i += 1
        if i < len(arrList) and arrList[i] is not None:
            node.right = BinaryTree(arrList[i])
            queue.append(node.right)
        i += 1
    return root


def rightLevelNode(root):
    if not root:
        return []
    queue = deque()
    queue.append(root)
    result = []
    while queue:
        levelSize = len(queue)
        for i in range(levelSize):
            node = queue.popleft()
            if i == levelSize -1:
                result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result

# テストケース
print(rightLevelNode(toBinaryTree([1,2])))
print(rightLevelNode(toBinaryTree([1,2,3,None,4,5,6])))
print(rightLevelNode(toBinaryTree([0,1,2,None,4,None,5])))
print(rightLevelNode(toBinaryTree([0,3,None,None,8])))
print(rightLevelNode(toBinaryTree([3,7,5,6,None,9,None])))
print(rightLevelNode(toBinaryTree([1,2,3,4,5,6,7,8,None,9,10,11,None,None,12,None,13])))