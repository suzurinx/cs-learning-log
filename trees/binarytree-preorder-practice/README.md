# binarytree-preorder-travasal 問題の解法メモ

## 内容

配列で与えられた値から**レベル順二分木**を構築し、**前順走査**でノードを出力する

## 実装ポイント

- 入力の配列は`None`を含むことで「葉のない枝」も表現できるので、**キューを利用したレベル順構築**で`toBinaryTree`関数を実装
- 走査本体は再帰（preOrder: ルート → 左 → 右）で、各ノードの値をprint出力
- 「print結果が全て繋がる」問題を避けるため、**ラッパー関数**を利用して改行処理を分離
- Noneチェックは`is not None`で、「0、空文字も値あり」として木に加える処理だが、問題文の中で「整数の配列」という説明があるため、`not arrList`を採用しなかった。
- ラッパー関数の利用により、改行をコントロールする

## テスト

```python

preOrderTraversal(toBinaryTree([0,-10,5,None,-3,None,9]))
preOrderTraversal(toBinaryTree([5,3,6,2,4,None,7]))
preOrderTraversal(toBinaryTree([-2,-17,8,-18,-11,3,19,None,None,None,-4,None,None,None,25]))
preOrderTraversal(toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]))
preOrderTraversal(toBinaryTree([1,-5,15,-9,-4,10,17,None,-6,None,0,None,14,16,19]))
preOrderTraversal(toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]))

```

## 出力

```python

0 -10 -3 5 9
5 3 2 4 6 7
-2 -17 -18 -11 -4 8 3 19 25
3 -3 -7 -10 -4 1 0 2 13 6 5 8 18 15 19
1 -5 -9 -6 -4 0 15 10 14 17 16 19
3 -3 -7 -10 -4 1 0 2 13 6 5 8 18 15 19

```

## 気づき

- ラッパー関数（preOrderTraversal）：改行やエラーチェックなど、“前後の処理”を担当する
- ヘルパー関数（preOrderTraversalHelper）：木構造の“中身の再帰処理”だけを担当
- 再帰で`return`が不要なのは、`print`で値を出すだけで戻り値が不要なため

## まとめ

- ラッパー関数の利用により、出力のコントロールがしやすくなる
