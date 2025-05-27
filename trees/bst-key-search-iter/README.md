# bst-key-search-iter 問題の解法メモ

## 内容
二分探索木（BST）から指定した key をイテレーターで取得する

## 実装ポイント
- 再帰を使って中間値をルートにし、左右に分割して バランスのとれたBSTを構築
    - 空配列や過剰分割にも対応するベースケース設計（`if end < start`）


## テストケース
balancedBST = sortedArrayToBST([1,2,3,4,5,6,7,8,9,10,11])
print(keyExist(6, balancedBST))
print(keyExist(10, balancedBST))
print(keyExist(45, balancedBST))

## 出力
True, False

## 気づき
- イテレーターを利用しても SBT を歩ける
- while 文での break の使い所