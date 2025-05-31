class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def toBinaryTree(arr):
    if not arr:
        return None

    root = BinaryTree(arr[0])
    queue = [root]
    i = 1

    while i < len(arr):
        node = queue.pop(0)

        # 左側
        if arr[i] is not None:
            node.left = BinaryTree(arr[i])
            queue.append(node.left)
        i += 1

        # 右側
        if i < len(arr) and arr[i] is not None:
            node.right = BinaryTree(arr[i])
            queue.append(node.right)
        i += 1
    return root

def minimumNode(root):
    if not root:
        return None

    # ベースケース
    if not root.left:
        return root
    return minimumNode(root.left)

# 確認用に、ノードの値だけを表示する関数
def printNode(node):
    if not node:
        print([])
    else:
        print(node.data)

# 出力
printNode(minimumNode(toBinaryTree([]))) # --> []
printNode(minimumNode(toBinaryTree([0,-10,5,None,-3,None,9]))) # --> [-10,null,-3]
printNode(minimumNode(toBinaryTree([5,3,6,2,4,None,7]))) # --> [2]
printNode(minimumNode(toBinaryTree([-2,-17,8,-18,-11,3,19,None,None,None,-4,None,None,None,25]))) # --> [-18]
printNode(minimumNode(toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]))) # --> [-10]
printNode(minimumNode(toBinaryTree([1,-5,15,-9,-4,10,17,None,-6,None,0,None,14,16,19])))# --> [-9,null,-6]