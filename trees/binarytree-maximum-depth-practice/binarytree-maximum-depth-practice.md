# binaryTree-maximum-depth-practice 問題の解法メモ
## 内容
与えられた配列（レベル順でノード、Noneで葉の欠損を表現）から二分木を構築し、その木の最大の深さ（根ノードから最も遠い葉ノードまでの最長経路のノード数）を返す関数 maximumDepth を実装する

## 実装ポイント
### toBinaryTree関数
- 配列の先頭がルート、それ以降は左→右の順にノードを割り当てていく
- queue を使ってレベル順にノードを追加
- None の値は「子ノードを持たない」＝葉の終端を意味する

### maximumDepth関数
- ベースケース：root is None の場合 -1 を返す
	- これは「葉ノードの深さを0」「親ノードはそこから+1」というカウント方式に合わせたもの（テストケース基準）
- 再帰的に左右の部分木の深さを計算し、最大値を+1して返す
	- leftDepth = maximumDepth(root.left)
	- rightDepth = maximumDepth(root.right)
	- return max(leftDepth, rightDepth) + 1
- こうすることで「ルートのみ＝深さ0」「1段下に子がいる＝深さ1」…と自然に深さが計算できる

## テストケース
```python
maximumDepth(toBinaryTree([0]))
maximumDepth(toBinaryTree([0,1,None]))
maximumDepth(toBinaryTree([0,-10,5,None,-3,None,9]))
maximumDepth(toBinaryTree([5,2,18,-4,3]))
maximumDepth(toBinaryTree([27,14,35,10,19,31,42]))
maximumDepth(toBinaryTree([30,15,60,7,22,45,75,None,None,17,27]))
maximumDepth(toBinaryTree([90,50,150,20,75,95,175,5,25,66,80,92,111,166,200]))
maximumDepth(toBinaryTree([50,17,76,9,23,54,None,None,14,19,None,None,72]))
maximumDepth(toBinaryTree([16,14,10,8,7,9,3,2,4,1]))
maximumDepth(toBinaryTree([30,15,60,7,22,45,75,1,None,17,27,None,None,None,None,-1]))
```
# 出力

```python
0
1
2
2
2
3
3
3
3
4
```
## 気づき
- 深さの定義は「根ノード=0」からスタート
    - 「葉ノード = 0」から数えるパターンもあるが、テストケースに合わせて定義を合わせることが大切
- ベースケースが設計の肝
    - root is None で -1 を返すことで、再帰の「積み上げ」カウントに自然に対応できる
    - 応用で「根を1からスタート」にしたければ、ベースケースを0にして+1を調整するだけ
- 木構造×再帰は、ロジックの設計とテストケースの出力形式を必ず合わせて実装することが大切
- 出力がおかしい時は、「どこで＋1 or -1 しているか」を紙に書き出してトレースすると直せる
## まとめ
- 二分木の深さ計算は、**「再帰のベースケース設定」と「+1する位置」**がすべて
