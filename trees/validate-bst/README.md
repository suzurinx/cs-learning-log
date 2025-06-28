# 問題名
有効な二分木
二分木のrootが与えられるので、その二分木がBSTかを判定する。

## 問題内容
与えられた二分木が「二分探索木（BST）」の条件を満たしているか判定する。
#### BSTの定義：各ノードについて
- 左部分木の全てのノード値 < 親ノード
- 右部分木の全てのノード値 > 親ノード
- 左右の部分木もBSTであること

## 実装ポイント
#### 実装の方針
- 再帰型（min/max値を伝搬させて判定）
- in-order型（昇順リスト化→単純比較）

#### 意識した制約・パフォーマンス
- ノード値が重複しない
- 空木（None）はBSTとする
- in-order型は「値を全列挙」なのでO(N)のリストを保持
- min/max伝搬型は「親ノード情報を持ち回る」ため副作用がない

#### 難所・分岐・構造上の注意点
- ノードの比較範囲（親/祖先ノードの情報伝搬 or 隣接ノード比較）を誤ると誤判定になる
- in-orderではリストが正しい昇順になっているか、for文で全要素チェック
- min/max伝搬では、毎回引数として範囲を伝搬（再帰）
- 空木・葉ノードはベースケースでTrueを返すこと

## テストケース
```python
print(validateBST(toBinaryTree([0, None, -1])))           # False
print(validateBST(toBinaryTree([4, 1, 5])))               # True
print(validateBST(toBinaryTree([15, 10, 20, 8, 12, 16, 25])))  # True
print(validateBST(toBinaryTree([30, 15, 60, 7, 22, 45, 75, None, None, 17, 27]))) # True
print(validateBST(toBinaryTree([5, 1, 2, 3, 4])))         # False
print(validateBST(toBinaryTree([5, 1, 4, None, None, 3, 6])))  # False
print(validateBST(toBinaryTree([])))                      # True
print(validateBST(toBinaryTree([5, 3, 9, 1, 6, 8])))      # False
print(validateBST(toBinaryTree([1])))                     # True
print(validateBST(toBinaryTree([1, 2])))                  # False
```

# 実行結果
```python
False
True
True
True
False
False
True
False
True
False
```

## 気づき
- BST判定には「親/祖先ノードの値をどう伝搬するか」が本質
- in-orderリスト法は昇順かどうかを一度に判定できて直感的。ただし“BSTであること”が前提
- ラップ関数＋ヘルパー関数の構造で「APIとしてのシンプルさ」「実装内部の柔軟さ」両立
- 木構造⇔リストの相互変換（BFS・in-order）はCS学習の“幹”になる型
- 同じ機能でも“型”や“選択肢”のバリエーションを意識することが理解を深める

## 再訪メモ
- in-order型・min/max型どちらも再現できるか
- ノード値がすべて負の数/ゼロの場合でもベースケースが成立するかチェック
- 「再帰の引数」「伝搬する情報」が何か？を“自問”する習慣が今後も役立つ

## 解いた日
2025-06-28
