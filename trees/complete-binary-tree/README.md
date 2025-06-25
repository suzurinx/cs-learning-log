# 問題名
完全二分木

## 問題内容
与えられた二分木を完全二分木か判定する。  
完全二分木：最下層以外の全階層がノードで埋まり、最下層のノードも左詰めになっているもの。  
入力のデータ型： binaryTree<integer> root  
出力のデータ型： bool  

## 実装ポイント
走査方針：
- BFS（幅優先探索、queue使用）  

実装の工夫：
- フラグ（foundNone）を立て、Noneを検出した以降にノードが現れた場合は即座に False を返す
- toBinaryTree()でリストから木構造をレベル順に構築

制約：
- 入力が空の場合（root is None）は True を返す（空の木も完全二分木とみなす）

注意点：
- 木構造内の None を見落とさない
- lst[i] だけでは 0 のノードを除外してしまうため、is not None で厳密に判定する

## テストケース
```python
isCompleteBinaryTree(toBinaryTree([0,1,2,3]))
isCompleteBinaryTree(toBinaryTree([0,1,2,3,4,5]))
isCompleteBinaryTree(toBinaryTree([0,1,2,4,5,None,7]))
isCompleteBinaryTree(toBinaryTree([0,1,3,4,None,7,8]))
isCompleteBinaryTree(toBinaryTree([0,1,2,3,None,6]))
isCompleteBinaryTree(toBinaryTree([97,10,77,32,40,70,32,96,27,10,12,90,73,100,86,None,96]))
isCompleteBinaryTree(toBinaryTree([11,7,75,9,59,83,60,46,6,12,26,28,26,91,98,83,7,None,31,66,77,23,None,100,40]))
isCompleteBinaryTree(toBinaryTree([38,67,22,52,0,29,43,41,55,97,82,33,85,5,80,3,94,46,0,32,88,59,59,38,64,83,78,47,13,41,89,90,17,36,53,56,1,8,36,92,8,None,78,33,81,86,None,10,6,31,27]))
```

# 実行結果
```python
True
True
False
False
False
False
False
False
```
## 気づき
- BFS＋フラグ管理のパターンは「“後に現れたノード”がルール違反かどうか」を検出する典型例
- lst[i] is not None を使わないと 0 の値がはじかれる（Python特有の罠）
- 完全二分木の判定ロジックは**「Noneを見つけてから、ノードが現れた瞬間False」**でシンプルに実現できる
## 再訪メモ
- toBinaryTree() の引数名や実装方針、is not None の理由を復習
- 「フラグ式」の設計感覚・どこでTrue/Falseが分岐するかの思考プロセス

## 解いた日
2025-06-25
