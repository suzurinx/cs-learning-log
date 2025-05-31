# bst-minimum-node 問題の解法メモ

## 内容

二分探索木（BST）の最大値を探す

## 実装ポイント

- テストケースを見ると引数のリストは昇順にソートされていない
- level-oderだと推測できる

## テストケース

```python
maximumNode( toBinaryTree([0,-10,5,None,-3,None,9]))
maximumNode( toBinaryTree([5,3,6,2,4,None,7]))
maximumNode( toBinaryTree([5,3,7,2,4,6,9,None,8]))
maximumNode( toBinaryTree([-2,-17,8,-18,-11,3,19,None,-4,None,25]))
maximumNode( toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]))
maximumNode(toBinaryTree([1,-5,15,-9,-4,10,17,None,-6,None,0,None,14,16,19]))
```

## 出力

```
9
7
9
19
19
19
```

## 気づき
```python
# 再帰でBSTを構築
def insertBST(root, data):
    if not root:
        return BinaryTree(data)
    if data < root.data:
        root.left = insertBST(root.left, data)
    else:
        root.right = insertBST(root.right, data)
    return root

# 配列を順に入れる
arr = [5, 3, 7, 2, 4, 6, 9]
root = None
for num in arr:
    root = insertBST(root, num)
```

↑コードが複雑でメンテナンスが難しい

最大値を探す走査はキューでも可能だが、キューを利用した走査は全ノードをレベル別に走査するためBSTを作った意味がなくなる。

`not arr` これは `空リスト` や `None` が `True` になる。例えば 0 が与えられた場合は `False` になる。ややこしい。

## まとめ

入力配列がソート済みではないため、中央をルートにする方法ではなく、先頭から順にノードを作成していく方法を採用した。

`not arr` の挙動は、`空リスト` や `None` を対象にするのは自然だが、0 があった場合には別の条件が必要なのだとわかった。

BST を構築するアルゴリズムの選択肢（キュー・再帰・ループ）を比較できたのが良い収穫だった。