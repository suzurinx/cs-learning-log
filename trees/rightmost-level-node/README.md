# 問題名
右側のノード

## 問題内容
二分木において、各階層の右端にあるノードの値をリストで返す。  
ノードは `BinaryTree` クラスで表現されており、各ノードに `left`, `right` 子が存在する。

## 実装ポイント
- 実装の方針：BFS（幅優先探索）でレベルごとに走査
- 意識した制約・パフォーマンス：
  - 各ノードに一度ずつしかアクセスしない（O(N)）
  - キューで階層制御し、インデックスで右端を検出
- 難所・分岐・構造上の注意点：
  - キューの中に異なる階層が混在する点
  - `levelSize - 1` で「右端のノード」を検出する工夫

## テストケース
```python
print(rightLevelNode(toBinaryTree([1,2])))
print(rightLevelNode(toBinaryTree([1,2,3,null,4,5,6])))
print(rightLevelNode(toBinaryTree([0,1,2,null,4,null,5])))
print(rightLevelNode(toBinaryTree([0,3,null,null,8])))
print(rightLevelNode(toBinaryTree([3,7,5,6,null,9,null])))
print(rightLevelNode(toBinaryTree([1,2,3,4,5,6,7,8,null,9,10,11,null,null,12,null,13])))
```

# 実行結果
```python
[1, 2]
[1, 3, 6]
[0, 2, 5]
[0, 3, 8]
[3, 5, 9]
[1, 3, 7, 12, 13]
```
## 気づき
- BFSのキューは「複数の階層が混在する」という特徴を持っており、levelSize を基準に毎階層ごとに処理を区切る必要がある。
- DFSでは横並びのノード比較がしづらいため、右端の判定には不向きだった。
- インデックス levelSize - 1 を使えば、各レベルの右端ノードを特定できる構造は再利用性が高い。

## 再訪メモ
- 「階層別の最小・最大ノードを取り出す」系の問題でも、同じBFS制御パターンが使える。
- queue の中身に対して「どの時点で何が入っているか」を意識すると、設計理解が深まる。
- toBinaryTree() が何をしているか不明な場合は、ノードを明示的に BinaryTree で構築することで構造を追いやすい。
## 解いた日
2025-06-24
