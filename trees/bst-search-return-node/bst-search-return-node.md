# bst-key-search 問題の解法メモ

## 内容
-level-orderで木構造を実装
-与えられたノード以下をlevel-orderで配列に変換

## 実装ポイント
-toBinaryTree(arr)
与えられた配列（arr）を順序通りに木構造に変換する。
queueを使って、親ノードから順に子ノードを順次接続していく（レベル順での木構造の構築）。

-treeSearch(root, key)
再帰ではなくqueueを使ったlevel-order探索。
親ノードから子ノードへ順に確認していく（深さ優先でなく幅優先探索のイメージ）。

-printTree(node)
与えられた部分木（または木全体）をlevel-orderでリスト化。
結果の末尾に連続するNoneを末尾調整して出力を整える。

## テストケース
tree1 = toBinaryTree([0, -10, 5, None, -3, None, 9])
print(printTree(treeSearch(tree1, 5)))
print(printTree(treeSearch(tree1, 20)))

tree2 = toBinaryTree([5, 3, 6, 2, 4, None, 7])
print(printTree(treeSearch(tree2, 3)))
print(printTree(treeSearch(tree2, 5)))
print(printTree(treeSearch(tree2, 15)))

## 出力
[5, None, 9]
[]
[3, 2, 4]
[5, 3, 6, 2, 4, None, 7]
[]

## 気づき
-BSTとSBTでは実装方法が違う
    -BST: 左＜親＜右のルールをもち木構造を構築するが、バランスは保証されない
    -SBT: ソート済み配列の中央から親ノードを作り木構造を構築する