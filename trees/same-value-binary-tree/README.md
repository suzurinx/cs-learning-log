# some-value-binary-tree 問題の解法メモ

## 内容
- 与えられた二分木のすべてのノードが同じ値を持つかどうかを判定する
- すべてのノードが同じ値であれば True、そうでなければ False を返す

## 実装ポイント
- 二分木の全ノードを網羅的に比較する必要がある
- 再帰（ラップ型・ネスト型）、キュー（BFS）、スタック（DFS）など複数の方法で実装可能
- **ベースケース（空の木）**には True を返す（仕様上、空木は“同じ値”とみなす）
- 配列から木構造を作る toBinaryTree も実装（インデックス範囲外アクセスに注意）
- キューやスタックを使う場合は、探索順序より「全ノードを比較」することが本質（順序自体は結果に影響しない）

## テストケース
```python
print(treeWithTheSameValue(toBinaryTree([0])))
print(treeWithTheSameValue(toBinaryTree([0,1,2])))
print(treeWithTheSameValue(toBinaryTree([0,0,0,0,0,None,0])))
print(treeWithTheSameValue(toBinaryTree([1,1,1,7,1])))
```
## 出力
```python
True
False
True
False
```
## 気づき
- 同じ処理でも複数の型（再帰、BFS、DFS）で書き分け可能
- 再帰型はシンプルで分かりやすい
- キューやスタックを使うと反復的に実装できる
- toBinaryTree 実装時は、i < len(arrList) などインデックスの安全性に要注意
- 「空木はTrue」とする仕様は一般的だが、問題に応じて設計を見直す必要もある
- 木構造の“型”を意識して書き分けることで、実装力が大幅に向上した