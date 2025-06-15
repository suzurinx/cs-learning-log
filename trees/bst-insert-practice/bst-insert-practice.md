# bst-insert-practice 問題の解法メモ

## 内容


## 実装ポイント
与えられた配列から平衡二分探索木（BST）を構築し、BSTに新しい値を効率的に挿入する。  

## テストケース
```python
balancedBST = BinarySearchTree([4,43,36,46,32,7,97,95,34,8,96,35,85,1010,232])
balancedBST.printSorted()
balancedBST.insert(5)
balancedBST.printSorted()
balancedBST.insert(47)
balancedBST.printSorted()
balancedBST.insert(0);
balancedBST.printSorted()
```

## 出力
```python
4 7 8 32 34 35 36 43 46 85 95 96 97 232 1010 
4 5 7 8 32 34 35 36 43 46 85 95 96 97 232 1010 
4 5 7 8 32 34 35 36 43 46 47 85 95 96 97 232 1010 
0 4 5 7 8 32 34 35 36 43 46 47 85 95 96 97 232 1010 
```

## 気づき
- BSTの挿入処理は単純に見えて、重複値の扱いを含めた条件整理が重要
- クラス設計で機能をまとめることで、管理や呼び出しが楽になる
- 再帰的に配列を分割しノードを作る設計は、木構造の理解に直結する
