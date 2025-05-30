class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# level-order でBSTを構築する
# 問題文から SBT を利用できないと判断
# ❶引数が完全な上旬の配列でない ❷中央値が取れない ❸空の枝を持つ概念がない
def toBinaryTree(arr):
    # ベースケース
    # if arr in None
    # 明示的にNoneを受け取る設計に向いている
    # not arrの利点
    # None / [] / '' / 0 などの「空っぽ系」全般に幅広く「空」のケースを防ぎたいとき
    if not arr:
        return None

    # 値に意味と役割を与えるために変数をつける
    root = BinaryTree(arr[0])
    # 次に子をつけるノードを入れるキューを作る
    # 最初はルートしかないのでこれを入れる
    queue = [root]
    # 配列のインデックス1から子ノードとして利用する
    i = 1

    # 配列の終わりまで順番に子ノードに設定する
    while i < len(arr):
        # 今からつける子ノードの親ノードを取り出す
        node = queue.pop(0)
        # 左の子ノード
        if arr[i] is not None:
            node.left = BinaryTree(arr[i])
            queue.append(node.left)
        i += 1

        # 右の子ノード
        # rightという変数はないがiで状態遷移しているところがポイント
        if i < len(arr) and arr[i] is not None:
            node.right = BinaryTree(arr[i])
            queue.append(node.right)
        i += 1

    return root


# BST内でkeyを探索して、見つかればノードを返す
def treeSearch(root, key):
    # バリテーション
    # (root is None にしない理由は not rootの方がカバーしている範囲が大きくこの関数を利用される場面ではこちらの方が想定されるから)
    if not root:
        return None

    queue = [root]

    while queue:
        node = queue.pop(0)
        if node.data == key:
            return node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return None


# 与えられたノード以下をlevel-orderで配列に変換
def printTree(node):
    if node is None:
        # Noneを返してもいいが、テストケースで[]が求められている表現なので[]を出力するようにする
        return []
    result = []
    queue = [node]
    while queue:
        current = queue.pop(0)
        result.append(current.data if current else None)
        if current:
            queue.append(current.left)
            queue.append(current.right)

    # 葉ノードについたNoneを削除する
    while result and result[-1] is None:
        result.pop()

    return result


# テストケース
tree1 = toBinaryTree([0, -10, 5, None, -3, None, 9])
print(printTree(treeSearch(tree1, 5)))  # → [5, None, 9]
print(printTree(treeSearch(tree1, 20)))  # → []

tree2 = toBinaryTree([5, 3, 6, 2, 4, None, 7])
print(printTree(treeSearch(tree2, 3)))  # → [3, 2, 4]
print(printTree(treeSearch(tree2, 5)))  # → [5, 3, 6, 2, 4, None, 7]
print(printTree(treeSearch(tree2, 15)))  # → []
