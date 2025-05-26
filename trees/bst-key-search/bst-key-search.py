class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# リスト（配列）を取得してヘルパー関数を作成
# 先頭、中間、末尾の３点を利用して再帰的にSBTを作成する
def sortedArrayToBST(arr):
    return sortedArrayToBSTHelper(arr, 0, len(arr) - 1)  # endはインデックスにする


# ヘルパー関数
def sortedArrayToBSTHelper(arr, start, end):
    # ベースケース(範囲外に達したらNone。これが葉ノードになる)
    # 引数に空arrが渡されても機能する（エッジケース）
    if start > end:
        return None

    # 中間点を見つける
    mid = (start + end) // 2

    # leftの構造を再帰的に作成
    # -1するのはmidを除外するため
    left = sortedArrayToBSTHelper(arr, start, mid - 1)

    # rightの構造を再帰的に作成
    # +1するのはmidを除外するため
    right = sortedArrayToBSTHelper(arr, mid + 1, end)

    # left、rightがベースケースに達したらマージする
    # 葉ノードから再帰的に作成される
    return BinaryTree(arr[start], left, right)


# in-order(中順走査)でSBTを出力する
# return文は一文というルールがある
# リストの合成は＋で繋げるというルールを利用して再帰的処理を実装する
def inOrderTraversal(node):
    if node is None:
        return []
    return inOrderTraversal(node.left) + [node.data] + inOrderTraversal(node.right)


# BSTにkeyが存在するのか確認する
def keyExist(key, bst):
    # ベースケース兼エッジケース（葉ノードまで到達してもkeyがない場合）
    if bst is None:
        return False
    # 合致する場合のベースケース（その時点でTrueを返す）
    if bst.data == key:
        return True

    # 再帰的処理・left
    if key < bst.data:
        return keyExist(key, bst.left)
    # それ以外・right
    # ＝になる値が重複するようだが、ベースケースに流すために必要なこと
    return keyExist(key, bst.right)

# テストケース
balancedBST = sortedArrayToBST([1,2,3,4,5,6,7,8,9,10,11])
print(keyExist(6, balancedBST))
print(keyExist(10, balancedBST))
print(keyExist(45, balancedBST))

