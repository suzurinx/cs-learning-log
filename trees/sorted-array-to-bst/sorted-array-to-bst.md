# bst-predecessor 問題の解法メモ

## 内容

- ソート済み配列（例：[1,2,3,4,5]）からバランスの良い二分探索木（BST: Binary Search Tree）を再帰的に構築する問題
- 構築したBSTを**中順走査（in-order traversal）**して値をリストとして出力する

## 実装ポイント

もし**insertBST関数**なら

```python
class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def insertBST(root, data):
    """
    BSTにdataを挿入する。rootがNoneなら新しいノードを作って返す。
    """
    if not root:
        return BinaryTree(data)
    if data < root.data:
        root.left = insertBST(root.left, data)
    else:
        root.right = insertBST(root.right, data)
    return root

def buildBST(arr):
    """
    配列を順に挿入してBSTを作る。
    """
    root = None
    for num in arr:
        root = insertBST(root, num)
    return root
```

- insertBSTによる構築は簡単だが、**入力配列がソート済みの場合は木が偏りやすくなる**（＝最悪、線形の片側木になってしまう）
- 対して、sortedArrToBSTのように中央から再帰的に分割して構築する方法は、**必ず高さバランスの取れた木**になる

## テストケース

```python
print(inOrderTraversal(sortedArrToBST([1,2,3])))
# [1, 2, 3]
print(inOrderTraversal(sortedArrToBST([1,2,3,5,6,9,10])))
# [1, 2, 3, 5, 6, 9, 10]
print(inOrderTraversal(sortedArrToBST([-1,0,3,10,13,19,22])))
# [-1, 0, 3, 10, 13, 19, 22]
print(inOrderTraversal(sortedArrToBST([1,3,4,5,8])))
# [1, 3, 4, 5, 8]
print(inOrderTraversal(sortedArrToBST([1,4,6,10,11,14,15,20,22,25,50,61,68,72])))
# [1, 4, 6, 10, 11, 14, 15, 20, 22, 25, 50, 61, 68, 72]
```

## 気づき

- 再帰関数の中でベースケース（start > end）を明確にすることで、木の末端でNoneを返し、正しいBSTが作れる
- ヘルパー関数をネストすることで、関数をまたぐ場合に起きる再呼び出しが不要でライトに実装できる
- in-order走査は再帰的に左部分木→自分→右部分木の順で値をリストとして合成する

## まとめ

- 再帰・木構造のイメージと、ベースケース・部分問題の合成の考え方が自然に身につく。
- Pythonではネストしたヘルパー関数を使うことで、余計な引数を増やさずに済み、可読性も高まる。