# 問題名
階層走査

## 問題内容
二分木を階層ごとに左→右のリストで出力する

## 実装ポイント
- 実装の方針：BFS（キューを使って階層単位に走査）
- 意識した制約・パフォーマンス：リスト化にあたってNoneの末尾除去を含める
- 難所・分岐・構造上の注意点など：
  - ノードがNoneの場合でもキューに含まれる構造となるため、適切にスキップ（continue）処理が必要
  - 出力の末尾に残る不要なNoneを後処理で除去する工夫が必要

## テストケース
```python
print(levelOrderTraversal(toBinaryTree([0,-10,5,None,-3,None,9])))
print(levelOrderTraversal(toBinaryTree([5,2,18,-4,3])))
print(levelOrderTraversal(toBinaryTree([27,14,35,10,19,31,42])))
print(levelOrderTraversal(toBinaryTree([30,15,60,7,22,45,75,None,None,17,27])))
print(levelOrderTraversal(toBinaryTree([90,50,150,20,75,95,175,5,25,66,80,92,111,166,200])))
print(levelOrderTraversal(toBinaryTree([50,17,76,9,23,54,None,None,14,19,None,None,72])))
print(levelOrderTraversal(toBinaryTree([16,14,10,8,7,9,3,2,4,1])))
```

# 実行結果
```python
[0, -10, 5, None, -3, None, 9]
[5, 2, 18, -4, 3]
[27, 14, 35, 10, 19, 31, 42]
[30, 15, 60, 7, 22, 45, 75, None, None, 17, 27]
[90, 50, 150, 20, 75, 95, 175, 5, 25, 66, 80, 92, 111, 166, 200]
[50, 17, 76, 9, 23, 54, None, None, 14, 19, None, None, 72]
[16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
```
## 気づき
- BFSの構造は再利用可能な型として認識できるようになっていた
- `continue` による明確なスキップ処理が構造をフラットに保つのに効果的だった
- エラーの出力が読めれば、ほぼ自力実装も可能だったという実感があった
- 「ノードがNoneでもキューに入る」ことで発生する問題に初めて明確に向き合い、continueでの制御が構造上必要な理由を実感できた
- BFS的処理をどう「リスト化」に適応させるか、変換操作の抽象度（from木 to list）の捉え方が前より洗練された
- 実装前に「この問題はBFS型だな」と認識できた時点で、アルゴリズムの地力がついてきていると感じた

## 再訪メモ
- `continue`の使いどころの定着

## 解いた日
2025-06-28
