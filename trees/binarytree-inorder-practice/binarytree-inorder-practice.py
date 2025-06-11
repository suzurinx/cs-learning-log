class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# 問題文の 引数（root） がブラックボックスの関数（toBinaryTree）になっているので、自力で作成する
# テストケースから
# - 平衡二分探索木ではないと推測できる
# - リストの先頭がルートで、レベル順二分木であると推測できるため、レベル順でノードを走査し二分木を実装する
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


# printInOrderを呼び出し、出力の後に改行処理をする（ラッピング）
def inOrderTraversal(root):
    printInOrder(root)
    print()


# 中順走査で出力する関数
def printInOrder(root):
    if root is not None:
        printInOrder(root.left)
        print(root.data, end=" ")
        printInOrder(root.right)


# テストケース
inOrderTraversal(toBinaryTree([0, -10, 5, None, -3, None, 9]))
inOrderTraversal(toBinaryTree([5, 3, 6, 2, 4, None, 7]))
inOrderTraversal(
    toBinaryTree(
        [-2, -17, 8, -18, -11, 3, 19, None, None, None, -4, None, None, None, 25]
    )
)
inOrderTraversal(toBinaryTree([3, -3, 13, -7, 1, 6, 18, -10, -4, 0, 2, 5, 8, 15, 19]))
inOrderTraversal(
    toBinaryTree([1, -5, 15, -9, -4, 10, 17, None, -6, None, 0, None, 14, 16, 19])
)
inOrderTraversal(toBinaryTree([3, -3, 13, -7, 1, 6, 18, -10, -4, 0, 2, 5, 8, 15, 19]))
