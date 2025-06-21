class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

""""
# 合成して新しい木構造を構築する
def mergeBST(root1, root2):
    # ベースケース
    # 両方がNoneでも問題なし、returnでNoneが代入されているのでそれがかえるw
    if not root1:
        return root2
    if not root2:
        return root1

    # root1、root2の両方がある場合の処理
    newNode = BinaryTree(root1.data + root2.data)
    newNode.left = mergeBST(root1.left, root2.left)
    newNode.right = mergeBST(root1.right, root2.right)
    return newNode
"""

# 既存の構造を更新して合成する
def mergeBST(root1, root2):
    # ベースケース
    if not root1:
        return root2
    if not root2:
        return root1
    # root1とroot2の両方がある場合の処理
    root1.data += root2.data
    root1.left = mergeBST(root1.left, root2.left)
    root1.right = mergeBST(root1.right, root2.right)
    return root1

""""
# 二分木を構築（キュー）
def toBinaryTree(arrList):
    if not arrList:
        return None
    root = BinaryTree(arrList[0])
    queue = [root]
    i = 1
    while i < len(arrList):
        node = queue.pop(0)
        if arrList[i] is not None:
            node.left = BinaryTree(arrList[i])
            queue.append(node.left)
        i += 1
        if i < len(arrList) and arrList[i] is not None:
            node.right = BinaryTree(arrList[i])
            queue.append(node.right)
        i += 1
    return root
"""
"""
# 二分木を構築（再帰）
def toBinaryTree(arrList):
    if not arrList:
        return None
    return toBinaryTreeHelper(arrList, 0)

#ヘルパー関数
def toBinaryTreeHelper(arrList, i):
    if i >= len(arrList) or arrList[i] is None:
        return None
    node = BinaryTree(arrList[i])
    node.left = toBinaryTreeHelper(arrList, 2*i+1)
    node.right = toBinaryTreeHelper(arrList, 2*i+2)
    return node
"""

# 二分木を構築（内部関数型）
def toBinaryTree(arrList):
    def helper(i):
        if i >= len(arrList) or arrList[i] is None:
            return None
        node = BinaryTree(arrList[i])
        node.left = helper(2*i+1)
        node.right = helper(2*i+2)
        return node
    return helper(0)

# メモリが出力をリスト表記へ変更
def toListInOrder(root):
    if root is None:
        return []
    return toListInOrder(root.left) + [root.data] + toListInOrder(root.right)


# テストケース
print(toListInOrder(mergeBST(toBinaryTree([]), toBinaryTree([]))))
print(toListInOrder(mergeBST(toBinaryTree([0]), toBinaryTree([]))))
print(toListInOrder(mergeBST(toBinaryTree([44,12,82,2,21,70,88,None,9,18,42,66,80,83,97]), toBinaryTree([48,24,74,7,39,51,83,None,10,27,44,None,71,77,86]))))
print(toListInOrder(mergeBST(toBinaryTree([42,10,87,2,29,53,92,None,8,14,36,43,76,90,96]), toBinaryTree([57,31,76,26,45,68,94,8,27,39,46,64,74,78,96,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,99]))))
print(toListInOrder(mergeBST(toBinaryTree([45,10,69,3,12,63,75,None,None,None,30,None,None,None,85]), toBinaryTree([53,10,70,6,31,60,88,3,8,15,33,54,66,79,93,None,4,None,9,None,22,None,46,None,58,None,69,None,80,91,98]))))