# bst-predecessor 問題の解法メモ

## 内容

異なる整数値で構成される二分探索木（BST）の根ノード `root` と、BST内に存在する整数 `key` が与えられる  
`key` の先行ノード（predecessor）である部分木を返す関数 `predecessor` を作成する  

**先行ノードとは**  
ノード `N` の値を `x` としたとき、木の中に存在する `x` より小さい最大の値を持つノードを指す  
後続ノード（successor）との操作は対称的である

## 実装ポイント

- 入力される配列はBSTを構築するためのものであることが保証されている  
- 先行ノードは以下のように探索する：  
  - `targetNode` の左部分木が存在するなら、その部分木の最大値が先行ノード  
  - 左部分木がない場合は、ルートから再探索して、ターゲットより小さい値を候補として保存しながら進む  
- BSTの性質（左 < 根 < 右）を活用して効率的に探索する  

### 重要な注意点（and検索）

複数の条件を組み合わせて判定するときは、必ず範囲チェック（配列の長さ確認など）を先に書くこと。  
```python
if i < len(arr) and arr[i] is not None:
```
この順序を間違えると、範囲外アクセスでエラーが発生する可能性がある  

## テストケース

```python
print(printTree(predecessor(toBinaryTree([0,-10,5,None,-3,None,9]), 5)))
print(printTree(predecessor(toBinaryTree([5,3,6,2,4,None,7]), 5)))
print(printTree(predecessor(toBinaryTree([10,6,12,4,8,None,None,2]), 12)))
print(printTree(predecessor(toBinaryTree([10,6,12,4,8,None,None,2]), 2)))
print(printTree(predecessor(toBinaryTree([5,None,7]), 5)))
print(printTree(predecessor(toBinaryTree([-2,-17,8,-18,-11,3,19,None,None,None,-4,None,None,None,25]), 8)))
print(printTree(predecessor(toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]), 6)))
print(printTree(predecessor(toBinaryTree([1,-5,15,-9,-4,10,17,None,-6,None,0,None,14,16,19]), 10)))
```

## 出力
```python
[0, -10, 5, None, -3, None, 9]
[4]
[10, 6, 12, 4, 8, None, None, 2]
[]
[]
[3]
[5]
[1, -5, 15, -9, -4, 10, 17, None, -6, None, 0, None, 14, 16, 19]
```

## 気づき

ターゲットより小さい値を見つけたら predecessor に保存して、より大きい値を探しに右に行く  
大きい値や同じ値のときは左に行って小さい値を探く  
これが先行ノードを見つける探索の肝  

## まとめ

今回の問題では、BSTの性質を活用することで効率よく先行ノードを特定できる  
条件分岐や探索の順序を正しく設計することが重要である  
また、配列やデータの範囲チェックは必ず先に行い、プログラムの安定性を高める必要がある