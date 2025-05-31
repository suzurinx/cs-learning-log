class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# level-treeを作成
def toBinaryTree(arr):
    if not arr:
        return None

    root = BinaryTree(arr[0])
    queue = [root]
    i = 1

    # キューを利用
    while i < len(arr):
        node = queue.pop(0)

        # 左側
        if arr[i] is not None:
            node.left = BinaryTree(arr[i])
            queue.append(node.left)
        i += 1

        # 右側
        # ループ内で+1をするためlen(arr)を超えない範囲にする
        if i < len(arr) and arr[i] is not None:
            node.right = BinaryTree(arr[i])
            queue.append(node.right)
        i += 1

    # level-orderで構築した二分木のルート（根のノード）を返す
    return root


# キーを探す関数
# 出力：boolean
def exists(root, key):
    # バリテーション
    # (root is None)にしない理由は、not rootの方がカバーしている範囲が大きいから
    if not root:
        return None

    queue = [root]

    while queue:
        node = queue.pop(0)
        if node.data == key:
            return True
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    # キーと同じ値がなかった場合
    return False


# テストケース
print(exists(toBinaryTree([0, -10, 5, None, -3, None, 9]), 5))  # --> True
print(exists(toBinaryTree([0, -10, 5, None, -3, None, 18]), 20))  # --> False
print(exists(toBinaryTree([5, 3, 6, 2, 4, None, 7]), 3))  # --> True
print(exists(toBinaryTree([5, 3, 6, 2, 4, None, 7]), 5))  # --> True
print(exists(toBinaryTree([5, 3, 6, 2, 4, None, 7]), 15))  # --> False
