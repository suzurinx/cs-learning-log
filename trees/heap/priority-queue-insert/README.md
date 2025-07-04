# 問題名
優先度付きキュー insert

## 問題内容
最大ヒープを利用して、insert / pop / top 操作が可能な優先度付きキューを実装する。  
内部的には、配列でヒープ構造を保持し、insert 時は下から上へ、pop 時は上から下へ再構成を行う。

## 実装ポイント
#### 実装の方針：
- 配列によるヒープ表現＋再帰的 maxHeapify
#### 意識した制約・パフォーマンス：
- insert・pop いずれも O(log N)
- ユーティリティ関数（親・子のインデックス）でロジックを簡潔化
#### 難所・分岐・構造上の注意点など：
- maxHeapify は pop時だけでなく、build時にも必要
- _siftUp では、親ノードと比較して上にあげていく
- 境界条件（親が存在しないとき＝root）を while parent >= 0 で安全に処理

## テストケース
```python
pq = PriorityQueue([2,3,43,2,53,6,75,10])
print(pq.maxHeap)
pq.insert(5)
print(pq.maxHeap)
pq.insert(5)
print(pq.maxHeap)
pq.insert(79)
print(pq.maxHeap)
pq.pop()
print(pq.maxHeap)
```

# 実行結果
```python
[75, 53, 43, 10, 3, 6, 2, 2]
[75, 53, 43, 10, 5, 6, 2, 2, 3]
[75, 53, 43, 10, 5, 6, 2, 2, 3, 5]
[79, 75, 43, 10, 53, 6, 2, 2, 3, 5, 5]
[75, 53, 43, 10, 5, 6, 2, 2, 3, 5]
```
## 気づき
- 関数ごとにエッジケースを切り分けておくと、呼び出し元で余計な心配をしなくて済む。
- maxHeapify は、呼び出す関数の前提条件を保証する存在でもある。
- 「絶対に起きない」入力を除外できるなら、その分設計が楽になる。
- とはいえ、それを見極めずに省略するのは危険。
- self.maxHeap[parent], self.maxHeap[i] = self.maxHeap[i], self.maxHeap[parent] のスワップ構文が自然に書けるようになった。

## 再訪メモ
- _siftUp で親とスワップしていくとき、インデックス更新の順序を再確認。
- 「なぜ maxHeapify を insert 時に使わず、siftUp を使うか？」を設計視点で答えられるように。

## 解いた日
2025-07-04
