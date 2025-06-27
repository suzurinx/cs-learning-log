# 問題名
二分探索木への挿入

## 問題内容
異なる整数値で構成される二分探索木（BST）の根ノード root と整数 key が与えられるので、key を BST に挿入する。

## 実装ポイント
実装の方針
- BSTの挿入処理は「再帰」または「ループ」で実装可能。
- 今回はbstInsertは再帰、toBinaryTreeはBFS型で実装。

意識した制約・パフォーマンス
- 挿入時、既存のノードと比較しながら探索（左右に進む）。
- toBinaryTreeのBFS実装でNoneを適切にハンドリング。
- 末尾のNoneはリスト化時に圧縮・省略。

難所・分岐・構造上の注意点
- keyが既存ノードと一致した場合は挿入せずそのまま返すこと。
- 再帰で「子ノードの再帰結果」をそのまま代入することで自然に更新される。
- BFS型toBinaryTreeでは、インデックス・長さチェックが必須。
- binaryTreeToListで末尾のNoneを圧縮する処理。

## テストケース
```python
print(bstInsert(toBinaryTree([0,-10,5,None,-3,None,9]), 20))
print(bstInsert(toBinaryTree([0,-10,5,None,-3,None,9]), 2))
print(bstInsert(toBinaryTree([5,2,18,-4,3,None,None]), 3))
print(bstInsert(toBinaryTree([5,2,18,-4,3,None,None]), 10))
print(bstInsert(toBinaryTree([27,14,35,10,19,31,42]), 15))
print(bstInsert(toBinaryTree([27,14,35,10,19,31,42]), 23))
print(bstInsert(toBinaryTree([30,15,60,7,22,45,75,None,None,17,27]), 8))
print(bstInsert(toBinaryTree([90,50,150,20,75,95,175,5,25,66,80,92,111,166,200]), 79))
print(bstInsert(toBinaryTree([50,17,76,9,23,54,None,None,14,19,None,None,72]), 57))
print(bstInsert(toBinaryTree([16,14,10,8,7,9,3,2,4,1]), 35))
```

# 実行結果
```python
[0, -10, 5, None, -3, None, 9, None, None, None, 20]
[0, -10, 5, None, -3, 2, 9]
[5, 2, 18, -4, 3]
[5, 2, 18, -4, 3, 10]
[27, 14, 35, 10, 19, 31, 42, None, None, 15]
[27, 14, 35, 10, 19, 31, 42, None, None, None, 23]
[30, 15, 60, 7, 22, 45, 75, None, 8, 17, 27]
[90, 50, 150, 20, 75, 95, 175, 5, 25, 66, 80, 92, 111, 166, 200, None, None, None, None, None, None, 79]
[50, 17, 76, 9, 23, 54, None, None, 14, 19, None, None, 72, None, None, None, None, 57]
[16, 14, 10, 8, 7, 9, 3, 2, 4, 1, None, None, None, None, 35]
```
## 気づき
- リスト⇔木構造の変換（toBinaryTree, binaryTreeToList）は写経・模倣だけでなく、構造の意味・変換理由を理解しながら進めると深く身につく。
- 再帰・BFSなど型を意識しながら選択肢を検討することが大切。
- 木構造データでは末尾のNone除去が見た目・効率に影響する場合があると実感。

## 再訪メモ
- BFS型toBinaryTreeのiインデックスまわり、ミスしやすいので注意
- 今回はリスト→木→リストの変換なので、「型」ではなく「具体的なオブジェクトの流れ」で全体像をイメージすること

## 解いた日
2025-6-27
