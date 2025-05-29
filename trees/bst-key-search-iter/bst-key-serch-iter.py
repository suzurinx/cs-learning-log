class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# SBTのメイン関数
# (長さから-1しているのはインデックスが欲しいから)
def sortedArrayToSBT(arr):
    return sortedArrayToSBTHelper(arr, 0, len(arr) - 1)


# SBTのヘルパー関数
# （再帰ごとに範囲を特定し、中央ノードをルートにするため）
def sortedArrayToSBTHelper(arr, start, end):
    # ベースケース
    # 範囲外になることを条件にしている
    # エッジケースの役割も担えている
    if end < start:
        return None

    # 中間点を求める
    # (中間点を除く前後が再帰範囲になる)
    mid = (start + end) // 2

    # 中間点より左側を再帰的に進む
    left = sortedArrayToSBTHelper(arr, start, mid - 1)

    # 中間点より右側を再帰的に進む
    right = sortedArrayToSBTHelper(arr, mid + 1, end)

    # 左右の葉ノードに達したらマージする
    # 根ノード
    return BinaryTree(arr[mid], left, right)


# BSTにkeyが含まれているかイテレーターを利用して探索する
# 再帰ではなく、ループでBSTを探索する実装
# True,Falseを返す
def keyExist(key, BST):
    # BSTのノードをイテレーターにしている
    # (dataにも参照先にもアクセス可能)
    iterator = BST
    while iterator:
        if iterator.data == key:
            # 値を返すことで関数処理を終了するため、ループ中でも break は利用しない
            # break はループ処理の中で状態を変えてから処理を続けたい時に利用する
            return True
        if key < iterator.data:
            iterator = iterator.left
        else:
            iterator = iterator.right

    return False


balancedBST = sortedArrayToSBT([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
print(keyExist(6, balancedBST))
print(keyExist(10, balancedBST))
print(keyExist(45, balancedBST))
