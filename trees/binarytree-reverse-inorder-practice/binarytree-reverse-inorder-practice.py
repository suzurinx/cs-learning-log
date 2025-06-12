# ノードを生成
class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# レベル順2分木の生成
def toBinaryTree(arrList):
    if not arrList:
        return None
    root = BinaryTree(arrList[0])
    queue = [root]
    i = 1

    while i < len(arrList):
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

# ラパー関数
def reverseInOrderTraversal(root):
    return reverseInOrderTraversalHelper(root, [])

# ヘルパー関数
def reverseInOrderTraversalHelper(root, arr):
    if root is not None:
        reverseInOrderTraversalHelper(root.right, arr)
        arr.append(root.data)
        reverseInOrderTraversalHelper(root.left, arr)
    return arr

# テスト
print(reverseInOrderTraversal(toBinaryTree([0,-10,5,None,-3,None,9])))
print(reverseInOrderTraversal(toBinaryTree([5,3,6,2,4,None,7])))
print(reverseInOrderTraversal(toBinaryTree([-2,-17,8,-18,-11,3,19,None,None,None,-4,None,None,None,25])))
print(reverseInOrderTraversal(toBinaryTree([1,-5,15,-9,-4,10,17,None,-6,None,0,None,14,16,19])))
print(reverseInOrderTraversal(toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19])))