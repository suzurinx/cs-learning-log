class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def sortedArrayToBST(arr):
    return sortedArrayToBSTHelper(arr, 0, len(arr) - 1)

def sortedArrayToBSTHelper(arr, start, end):
    # バリテーション兼ベースケース
    # ベースケースは範囲外の定義で設定
    # 空リストが渡されてもNoneを返す
    if end < start:
        return None

    # arrの中央
    mid = (start + end) // 2

    # leftの構造を再帰的に走査
    left = sortedArrayToBSTHelper(arr, start, mid - 1)
    # rightの構造の再帰的に走査
    right = sortedArrayToBSTHelper(arr, mid + 1, end)

    # マージ
    return BinaryTree(arr[mid], left, right)

# in-order
def inOrderTraversal(node):
    if node is None:
        return []
    return inOrderTraversal(node.left) + [node.data] + inOrderTraversal(node.right)

# テストケース
balancedBST = sortedArrayToBST([1,2,3,4,5,6,7,8,9,10,11])
print(inOrderTraversal(balancedBST))
