# binaryTree-inOrder-practice 問題の解法メモ

## 内容

入力で与えられる配列（arrList）からレベル順で二分木を構築し、その**中順走査（in-order traversal）**をプリントする

## 実装ポイント

- toBinaryTree関数でリストの値をもとにレベル順二分木を構築する
    - Noneの値を適切にスキップし、空のノード（葉の欠損）を表現する
	- queueを使って順にノードを割り当てていく
- inOrderTraversalはラッパー関数として、printInOrderの出力後に改行処理を追加する
- printInOrderは、中順（左→ルート→右）でノードを再帰的にprint出力する
- 「ノードがNoneかどうか」の判定は、if root is not None: でOK

## テストケース

```python
inorderTraversal(toBinaryTree([0,-10,5,None,-3,None,9]))
inorderTraversal(toBinaryTree([5,3,6,2,4,None,7]))
inorderTraversal(toBinaryTree([-2,-17,8,-18,-11,3,19,None,None,None,-4,None,None,None,25]))
inorderTraversal(toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]))
inorderTraversal(toBinaryTree([1,-5,15,-9,-4,10,17,None,-6,None,0,None,14,16,19]))
inorderTraversal(toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]))
```

# 出力

```python
-10 -3 0 5 9
2 3 4 5 6 7
-18 -17 -11 -4 -2 3 8 19 25
-10 -7 -4 -3 0 1 2 3 5 6 8 13 15 18 19
-9 -6 -5 -4 0 1 10 14 15 16 17 19
-10 -7 -4 -3 0 1 2 3 5 6 8 13 15 18 19
```
## 気づき

初手でこの辺りまで、要件定義できるようになってきた。

楽しい

```python
class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# 問題文の 引数（root） がブラックボックスの関数（toBinaryTree）になっているので、自力で作成する
# テストケースから
    # - 平衡二分探索木ではないと推測できる
    # - リストの先頭がルートで、レベル順二分木であると推測できるため、レベル順でノードを走査し二分木を実装する
def toBinaryTree(root):
    pass

# printInOrderを呼び出し、出力の後に改行処理をする（ラッピング）
def inOrderTraversal(root):
    pass

# 中順走査で出力する関数
def printInOrder(root):
    pass

# テストケース
inOrderTraversal(toBinaryTree([0,-10,5,None,-3,None,9]))
inOrderTraversal(toBinaryTree([5,3,6,2,4,None,7]))
inOrderTraversal(toBinaryTree([-2,-17,8,-18,-11,3,19,None,None,None,-4,None,None,None,25]))
inOrderTraversal(toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]))
inOrderTraversal(toBinaryTree([1,-5,15,-9,-4,10,17,None,-6,None,0,None,14,16,19]))
inOrderTraversal(toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]))
```
## まとめ

ブラックボックスを自力で再現する力がついてきた。細部では不明点も多いものの、パターン化しているものに関しては手が動くようになってきている。