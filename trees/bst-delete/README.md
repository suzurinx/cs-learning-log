# bst-delete 問題の解法メモ

## 内容
キーを受け取り、その値がキーと等しいノードを削除する
## 実装ポイント

## テストケース
```python
balancedBST = BinarySearchTree([4,43,36,46,32,7,97,95,34,8,96,35,85,1010,232])
balancedBST.printSorted()
balancedBST.deleteNode(43)
balancedBST.printSorted()
balancedBST.deleteNode(7)
balancedBST.printSorted()
balancedBST.deleteNode(4)
balancedBST.printSorted()
balancedBST.deleteNode(1010)

balancedBST.deleteNode(0)
balancedBST.printSorted()
```

## 出力
```python
4 7 8 32 34 35 36 43 46 85 95 96 97 232 1010 
4 7 8 32 34 35 36 46 85 95 96 97 232 1010 
4 8 32 34 35 36 46 85 95 96 97 232 1010 
8 32 34 35 36 46 85 95 96 97 232 1010 
8 32 34 35 36 46 85 95 96 97 232 
```

## 気づき
今は、まだ理解しきれていないため、この問題は後で見返す予定  
何度か手を動かしたら、自分の言葉でまとめる