# bst-key-exists 問題の解法メモ

## 内容

BST内で、与えられた `key` より大きい中で最小のノードを探し、その部分木を返す

## 実装ポイント

部分木とは、木構造における、あるノードを根とする、そのノードから下にぶら下がる全てのノードであり、根を含む

問題では、`BST` と指定があるので、左 < 根 < 右 の順で木構造を構築する必要がある

今回は利用しなかったが、`BST` の実装方法が下記。このほかに `level-order` という手法がある

---

右側にあれば
→ その中の最小ノードが後続ノード

右側にない場合
→ ルートから再探索して、左へ進む時に一時的に後続候補として保存
→ 最終的にターゲットノードに到達したら、その保存したノードを返す

---

- `toBinaryTree`
  → レベルオーダー（配列）から木構造をそのまま構築する
  → テストケースがすでにBSTであることが保証されている場合、簡単に実装できるが、一般的なBST構築ではない

- `buildBST`（insertBSTを使う）
  → 配列の要素を一つずつBSTに挿入していくことで、確実にBSTを構築する
  → 配列が順序付けられていなくてもBSTが完成する

**insertBST関数**

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




## テストケース

```python
successor(toBinaryTree([5, 4, None]), 5)
successor(toBinaryTree([-2, -17, 8, -18, -11, 3, 19, None, None, None, -4, None, None, None, 25]), 8)
successor(toBinaryTree([3, -3, 13, -7, 1, 6, 18, -10, -4, 0, 2, 5, 8, 15, 19]), 6)
successor(toBinaryTree([3, -3, 13, -7, 1, 6, 18, -10, -4, 0, 2, 5, 8, 15, 19]), 3)
successor(toBinaryTree([1, -5, 15, -9, -4, 10, 17, None, -6, None, 0, None, 14, 16, 19]), 10)
successor(toBinaryTree([0, -10, 5, None, -3, None, 9]), -3)
```

## 出力

```
[]
[19, None, 25]
[8]
[5]
[14]
[0, -10, 5, None, -3, None, 9]
```
## 気づき

- 部分木を返す問題のため、後続ノードだけでなく、そのノードを根としたサブツリー全体を返す必要がある
- BSTの構築方法で使う関数を明確に区別することが理解を助ける

## まとめ

- toBinaryTree と buildBST の違いを理解し、問題に適したBST構築方法を選ぶことが必要である
- 後続ノードの探索ロジックは「右部分木の最小値」または「祖先の中で最小の値」を見つける2段階に分かれる