# binarytree-postorder-travasal 問題の解法メモ

## 内容

- 平衡二分探索木の後順走査（post-order traversal）を実装
- 「左→右→ルート」の順にノードを巡回して出力

## 実装ポイント

- すでに前順・中順のパターンを学んだため、迷いなく実装できた
- 走査パターンごとの切り替えが、ほぼルーチン化した


## テスト

```python

balancedBST = BinarySearchTree([1,2,3,4,5,6,7,8,9,10,11])
balancedBST2 = BinarySearchTree([4,43,36,46,32,7,97,95,34,8,96,35,85,1010,232])
balancedBST.printSorted()
balancedBST2.printSorted()

```

## 出力

```python
2 1 5 4 3 8 7 11 10 9 6
4 8 7 34 36 35 32 46 95 85 97 1010 232 96 43
```

## 気づき

- 特に詰まった点や新しい気づきはなし
- コードもシンプルなので詳細解説は不要と判断
