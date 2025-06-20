# deepest-leaves 問題の解法メモ

## 内容
二分木 root が与えられたとき、最深層（もっとも深いレベル）に存在する葉ノードの合計値を返す deepestLeaves という関数を実装する

## 実装ポイント
- 最深層の葉ノードのみを合計する必要がある
- 「最深層」を知るには、**階層ごとの走査（BFS, キュー利用）**が有効
- BFSによるレベル順探索を利用し、「今見ている階層の全ノード」を毎回queueに保持
- queueの中身を「child」という新しいリストで次の階層に引き継ぐ
- 最後の階層（childが空）でqueueに残るノード＝最深層のノードリストとなる
- そのリストの .data を合計して返す
- 再帰/ループいずれの方法も実装できる
- 二分木の生成も「キュー型」「再帰型（内部関数型/ヘルパー）」など複数のパターンで練習

## テストケース
```python
print(deepestLeaves(toBinaryTree([3,2,1,None,7,8])))
print(deepestLeaves(toBinaryTree([5,8,1,10,12,8,None,None,None,None,None,9,10])))
print(deepestLeaves(toBinaryTree([5,2,18,4,3])))
print(deepestLeaves(toBinaryTree([27,14,35,10,19,31,42])))
print(deepestLeaves(toBinaryTree([30,15,60,7,22,45,75,None,None,17,27])))
print(deepestLeaves(toBinaryTree([50,17,76,9,23,54,None,None,14,19,None,None,72])))
print(deepestLeaves(toBinaryTree([16,14,10,8,7,9,3,2,4,1])))
print(deepestLeaves(toBinaryTree([0,-10,5,None,-3,None,9])))
```
## 出力
```python
15
19
7
102
44
105
7
6
```
## 気づき
- 「最深層を意図的に集める」ためのBFS（レベル順探索）の使い方を理解・実装できた
- 状態遷移としてqueueを次の階層（child）に更新し続ける設計が新しかった
- 再帰とループの両方で「同じこと」を書ける感覚がついた
    → 再帰は構造の追跡・ループは手続きの積み重ね、それぞれの強みが分かった
- queue/stack、内部関数/ヘルパー関数など、木構造の主要な実装パターンを網羅できるようになった
- 木構造の処理は「何をもって階層やノードを抽出するか」の設計で難易度が変わる、と実感した
- if条件の順番や、再帰時の状態遷移の柔軟性も深く理解できた
