# 問題名
対照的な二分木

## 問題内容
二分木がシンメトリーか評価する

## 実装ポイント
#### 実装の方針：**再帰**による左右の部分木のミラー構造チェック
#### 意識した制約・パフォーマンス：
- 高さ `h` に対して O(n) 時間・O(h) 空間（コールスタック使用）
- `None` は葉として追加しない前提の設計
#### 難所・分岐・構造上の注意点：
- `None` の扱いと左右の「対称な位置」にあるノードの比較
- False が出た時点で即 return される最適化再帰
- 「左.left vs 右.right」「左.right vs 右.left」の入れ替え呼び出しの設計に注意

## テストケース
```python
print(symmetricTree(toBinaryTree([10,25,25,33,45,45,33])))
print(symmetricTree(toBinaryTree([10,25,25,33,45,45,32])))
print(symmetricTree(toBinaryTree([1,2,2,3,4,4,3])))
print(symmetricTree(toBinaryTree([3,6,6,9,12,11,9])))
print(symmetricTree(toBinaryTree([])))
print(symmetricTree(toBinaryTree([1,9,9,15,19,19,15])))
print(symmetricTree(toBinaryTree([1,2,2,None,3,None,3])))
print(symmetricTree(toBinaryTree([3,6,6,9,12,12,9])))
print(symmetricTree(toBinaryTree([3,6,7,9,12,12,9])))
print(symmetricTree(toBinaryTree([1,2,2,2,None,2])))
print(symmetricTree(toBinaryTree([1,2,3])))
```

# 実行結果
```python
True
False
True
False
True
True
False
True
False
False
False
```

## 気づき
- False が出た時点で即終了できる再帰構造になっていることが印象的だった。
- None の扱い方次第で左右非対称と判定されるケースが出てくるため、**構造の前提（リストからの構築方法）**に注意が必要。
- **toBinaryTree() の実装方針（Noneを子に追加しない）**が今回の評価基準と合致していた。

## 再訪メモ
- 特に再帰呼び出しの構造（left.left と right.right の関係）を逆にしないように注意したい。
- toBinaryTree() の実装と symmetricTree() の対称チェックロジックが一体で意味をなしているため、片方だけを変更しない。
- 初見で「どう比較していくか」をイメージしにくかった。左右を内側と外側に向けて比較するという考え方を再確認しておきたい。

## 解いた日
2025-6-28
