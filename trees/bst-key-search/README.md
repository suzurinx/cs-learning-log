# bst-key-search 問題の解法メモ

## 内容
二分探索木（BST）から指定した key を取得する

## 実装ポイント
- 再帰を使って中間値をルートにし、左右に分割して BST を構築
    - 空配列や過剰分割にも対応するベースケース設計（`if end < start`）


## テストケース
balancedBST = sortedArrayToBST([1,2,3,4,5,6,7,8,9,10,11])
print(keyExist(6, balancedBST))
print(keyExist(10, balancedBST))
print(keyExist(45, balancedBST))

## 出力
True, False

## 気づき
- 中順走査（in-order traversal）は、リストの合成を使って再帰的に表現できる
- key探索は、BSTを順にたどりながら、ベースケースで探索を止める構造になっている