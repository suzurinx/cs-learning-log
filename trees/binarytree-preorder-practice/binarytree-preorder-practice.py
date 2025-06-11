class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# 問題にはtoBinaryTreeがブラックボックスになっているのでこの関数を自力で実装して利用する
# どんな関数か？
    # →リストを見ると、midが取れないので平衡二分探索木ではない
    # →レベル順二分木と推測できる
    # →なので、ルートは配列の初めの要素
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

# 下の関数をそのまま実行すると改行されないため、この関数でラッピングして改行処理をおこうなう
def preOrderTraversal(root):
    preOrderTraversalHelper(root)
    print()


# 前順走査（preOrder）でプリントする関数
def preOrderTraversalHelper(root):
    print(root.data, end=" ")
    if root.left is not None:
        preOrderTraversalHelper(root.left) # ←return すると処理が止まるので書かない
    if root.right is not None:
        preOrderTraversalHelper(root.right) # ←return すると処理が止まるので書かない


# test
preOrderTraversal(toBinaryTree([0,-10,5,None,-3,None,9]))
preOrderTraversal(toBinaryTree([5,3,6,2,4,None,7]))
preOrderTraversal(toBinaryTree([-2,-17,8,-18,-11,3,19,None,None,None,-4,None,None,None,25]))
preOrderTraversal(toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]))
preOrderTraversal(toBinaryTree([1,-5,15,-9,-4,10,17,None,-6,None,0,None,14,16,19]))
preOrderTraversal(toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]))