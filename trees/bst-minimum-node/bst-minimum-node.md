# bst-minimum-node 問題の解法メモ

## 内容

二分探索木（BST）内に存在する最小値を持つノードを探索する

## 実装ポイント

BSTなので、左の最深部が最小値になる

## 出力

```python
minimumNode(toBinaryTree([]))
minimumNode(toBinaryTree([0,-10,5,None,-3,None,9]))
minimumNode(toBinaryTree([5,3,6,2,4,None,7]))
minimumNode(toBinaryTree([-2,-17,8,-18,-11,3,19,None,None,None,-4,None,None,None,25]))
minimumNode(toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]))
minimumNode(toBinaryTree([1,-5,15,-9,-4,10,17,None,-6,None,0,None,14,16,19]))
```
## 出力

```python
[]
-10
2
-18
-10
-9
```

## 気づき

- `not arr` は　`None` だけでなく空リストなどもカバーできる
- `is not None` は明示的に `None` だけを見たいときに利用する

## まとめ

BSTの最小値探索は左側にあることを確認して進める。
また、`not` と `is not None` の使い分けも意識して使えるようになった。