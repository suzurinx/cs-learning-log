class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# テストケースの配列にNoneがないため、2分木構造を作れば完全二分木になる
def toBinaryTree(arrList):
    # エッジケース
    if arrList is None:
        return None
    root = BinaryTree(arrList[0])
    queue = [root]
    i = 1
    while i < len(arrList):
        currentNode = queue.pop(0)
        if arrList[i] is not None:
            currentNode.left = BinaryTree(arrList[i])
            queue.append(currentNode.left)
        i += 1
        if i < len(arrList) and arrList[i] is not None:
            currentNode.right = BinaryTree(arrList[i])
            queue.append(currentNode.right)
        i += 1
    return root

def countNodes(root):
    if root is None:
        return 0
    return countNodes(root.left) + countNodes(root.right) + 1

# テストケース
print(countNodes(toBinaryTree([6,11,25])))
print(countNodes(toBinaryTree([1,1,2,15,8])))
print(countNodes(toBinaryTree([6,11,25,5,9,8,4,56])))
print(countNodes(toBinaryTree([27,14,35,10,19,31,42])))
print(countNodes(toBinaryTree([30,15,60,7,22,45,75,17,27,12,14,5,79,110])))