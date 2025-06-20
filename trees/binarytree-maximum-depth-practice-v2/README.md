# binaryTree-maximum-depth-practice-v2 問題の解法メモ
## 内容
与えられた配列（レベル順でノード、Noneで葉の欠損を表現）から二分木を構築し、その木の最大の深さ（根ノードから最も遠い葉ノードまでの最長経路のノード数）を返す関数 maximumDepth を実装する  
末尾再帰で実装する

## 実装ポイント
### maximumDepth関数  
- 役割：入力のバリデーションおよび再帰ヘルパー関数の呼び出し  
- 仕様により、ノードが1つのときは深さ0となる必要があるため、再帰の初期値は `-1` に設定

### maximumDepthHelper関数  
- 役割：末尾再帰により左右の子ノードを探索し、最大の深さを返す  
- ベースケース：ノードが `None` のとき、現在の深さを返す  
- 再帰処理：左右の子に `depth + 1` を渡し、`max()` で深さを比較


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
- 深さの定義は「ノード数」ではなく「辺の数」となっていたため、depth = -1 を起点に調整
- バリデーションとロジックの責任を分離することで、実装がシンプルかつ明瞭になった
- 仕様をテストケースから読み取り、ロジック全体を逆算的に設計・修正できた

## まとめ
- 再帰のベースケースと起点の解釈がズレると、全体の出力もズレる
- toBinaryTree の構築方法と maximumDepth の設計が連動しており、構造的な整合性が求められる
- 初めは出力がズレたが、深さのカウント起点を1つずらす（-1）ことで、仕様との整合をきれいに解決できた
