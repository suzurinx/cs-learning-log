class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# 二分木を反転させる
# 再帰
def invertTree(root):
    if not root:
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root

# 二分木を反転させる
# キュー
def invertTreeQueue(root):
    if not root:
        return None
    queue = [root]
    while queue:
        current = queue.pop(0)
        current.left, current.right = current.right, current.left
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return root

# リストを受け取り二分木を作る
# 受け取るテストケースのリストはただの二分木と推測
# BFSで実装する
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

# 再帰で実装する
# トップ型
def toBinaryTreeTop(arrList):
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

# 同じく再帰で実装する
# ネスト型
def toBinaryTreeNest(arrList):
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


# テストケース
print(invertTree(toBinaryTree([1, 3, 8, 2, 5, 7, 10])))
print(invertTree(toBinaryTree([])))
print(invertTree(toBinaryTree([5, 4, 3, None, None, 8])))
print(invertTree(toBinaryTree([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])))