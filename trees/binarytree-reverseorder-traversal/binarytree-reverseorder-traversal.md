# binarytree-postorder-travasal 問題の解法メモ

## 内容

ソート済みの配列から平衡二分探索木（BST）を再帰的に構築し、逆順走査（reverse-order）でノードデータを出力する

## 実装ポイント

- 再帰処理のベースケース（`if start > end:`）を明確にすることで、**無限再帰のバグを防止**
- 走査アルゴリズム（左→右→ルート）は「関数の呼び出し順」を入れ替えるだけでOK
- **printとtraversalを分離**し、将来print以外の用途にも拡張しやすい設計にした
- クラス設計で、`BinaryTree`と`BinarySearchTree`の**責任分担**を意識

## テスト

```python

balancedBST = BinarySearchTree([1,2,3,4,5,6,7,8,9,10,11])
balancedBST2 = BinarySearchTree([4,43,36,46,32,7,97,95,34,8,96,35,85,1010,232])
balancedBST.printSorted()
balancedBST2.printSorted()

```

## 出力

```python

11 10 8 7 9 5 4 2 1 3 6
1010 97 232 95 46 85 96 36 34 35 8 4 7 32 43

```

## 気づき
- 走査アルゴリズム（前順・中順・後順）は処理順を入れ替えるだけなので、考え方をマスターすれば応用がきく
- クラスの設計・役割分担を意識することで、コードの拡張性・保守性が上がる
- Pythonのselfやメソッド呼び出し、再帰設計について、「わかっているつもり」だった基礎を再点検できた