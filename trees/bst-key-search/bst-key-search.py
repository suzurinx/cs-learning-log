class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# リスト（配列）を取得してヘルパー関数を作成
# 先頭、中間、末尾の３点を利用して再帰的にSBTを作成する
def sortedArrayToBST(arr):
    return sortedArrayToBSTHelper(arr, 0, len(arr) - 1) # endはインデックスにする

# ヘルパー関数
def sortedArrayToBSTHelper(arr, start, end):
    # ベースケース(範囲外に達したらNone。これが葉ノードになる)
    # 引数に空arrが渡されても機能する（エッジケース）
    if start > end: return None

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

def inOrderTraversal(node):
    pass

def keyExist(key, node):
    pass