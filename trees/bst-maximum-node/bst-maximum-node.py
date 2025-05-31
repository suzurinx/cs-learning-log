class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

# 二分探索木を作成する
def toBinaryTree(arr):
    if not arr:
        return None
    root = BinaryTree(arr[0])
    queue = [root]
    i = 1

    # キューを利用した方法
    while i < len(arr):
        node = queue.pop(0)

        if arr[i] is not None:
            node.left = BinaryTree(arr[i])
            queue.append(node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            node.right = BinaryTree(arr[i])
            queue.append(node.right)
        i += 1

    return root

# 最大値を探す
# キューを利用した探索は BST を作成した意味がなくなる
def maximumNode(root):
    if root is None:
        return None

    if not root.right:
        return  root
    return maximumNode(root.right)

def printNode(root):
    if not root:
        print([])
    else:
        print(root.data)

# 出力
printNode(maximumNode(toBinaryTree([0,-10,5,None,-3,None,9])))
printNode(maximumNode(toBinaryTree([5,3,6,2,4,None,7])))
printNode(maximumNode(toBinaryTree([5,3,7,2,4,6,9,None,8])))
printNode(maximumNode(toBinaryTree([-2,-17,8,-18,-11,3,19,None,-4,None,25])))
printNode(maximumNode(toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19])))
printNode(maximumNode(toBinaryTree([1,-5,15,-9,-4,10,17,None,-6,None,0,None,14,16,19])))