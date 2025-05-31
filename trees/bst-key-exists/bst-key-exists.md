# bst-key-exists 問題の解法メモ

## 内容
level-orderで構築した二分木のルートからkeyを見つける

## 実装ポイント
- level-oderを利用して二分木を作成
- キューを利用して走査する


## テストケース
exists(toBinaryTree([0, -10, 5, None, -3, None, 9]), 5)
exists(toBinaryTree([0, -10, 5, None, -3, None, 18]), 20)
exists(toBinaryTree([5, 3, 6, 2, 4, None, 7]), 3)
exists(toBinaryTree([5, 3, 6, 2, 4, None, 7]), 5)
exists(toBinaryTree([5, 3, 6, 2, 4, None, 7]), 15)

## 出力
True, False

## 気づき
- キューを利用したsearchは、自力でメモリ領域を作りコールスタックできる状態にしているように見える

## まとめ
この問題で、レベルオーダー構築・探索を改めて確認し、再帰ではなくループとキューを利用する意義を整理できた