# bst-all-elements-sorted 問題の解法メモ

## 内容
- 2つの二分探索木に含まれる全ての整数を昇順にソートしてリストとして返す関数 allElementsSorted を実装する
- 入力は各木を配列で与え、toBinaryTree で二分探索木に変換してから処理する

## 実装ポイント
- 各二分探索木を**中順走査（in-order traversal）**で値をリスト化する
    → BSTの場合、中順走査で得られる値は必ず昇順になる
- 2つの「ソート済みリスト」をマージ処理で1つのリストに統合する（いわゆるマージソートの統合パートと同じ考え方）
- それぞれの走査・マージ処理は再帰とループ、副作用型の書き方など複数の方法があるが、今回は副作用型（外部リストに値をappend）のパターンも学習
- None を含むリストも処理できるよう、木構造生成時のバリデーション・チェックを意識

## テストケース
```python
print(allElementsSorted(toBinaryTree([9,8,11]), toBinaryTree([3,1,5])))
print(allElementsSorted(toBinaryTree([3,None,5]), toBinaryTree([2,1,6])))
print(allElementsSorted(toBinaryTree([73,11,90,None,24,79,93]), toBinaryTree([44,39,49,36,41,46,72,None,None,None,None,None,None,None,86])))
print(allElementsSorted(toBinaryTree([29,14,48,1,20,42,76,None,None,None,None,None,None,None,97]), toBinaryTree([46,21,85,7,27,73,98])))
print(allElementsSorted(toBinaryTree([22,19,54,4,21,28,56]), toBinaryTree([29,10,64,4,28,32,75,None,None,None,None,None,None,None,100])))
```

## 出力
```python
[1, 3, 5, 8, 9, 11]
[1, 2, 3, 5, 6]
[11, 24, 36, 39, 41, 44, 46, 49, 72, 73, 79, 86, 90, 93]
[1, 7, 14, 20, 21, 27, 29, 42, 46, 48, 73, 76, 85, 97, 98]
[4, 4, 10, 19, 21, 22, 28, 28, 29, 32, 54, 56, 64, 75, 100]
```

## 気づき
- 二分探索木の中順走査（in-order traversal）は昇順に値を取り出せる王道パターン
- 副作用型・ピュア関数型、それぞれのメリット・癖がわかってきた
- 問題の出力仕様と木構造の作り方を読み違えないように注意が必要