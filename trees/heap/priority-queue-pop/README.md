# 問題名
優先度付きキュー pop

## 問題内容
配列で実装された最大ヒープをもとに、優先度付きキューを構築し、最大値（ルート）を取り出す pop() 関数を実装する。取り出したあともヒープ条件を維持したまま再構成する必要がある。

## 実装ポイント
#### 実装の方針：
- ループ + ヘルパー関数（maxHeapify）を使用した再帰構造
#### 意識した制約・パフォーマンス：
- 取り出し操作における時間計算量は O(log n)
- buildMaxHeap() による初期構築は O(n)
#### 難所・分岐・構造上の注意点：
- top() で最大値を取得してから、maxHeap[0] を maxHeap[-1] で上書き → pop() で末尾を削除 → maxHeapify() で再構成、の順序が重要
- maxHeapify() は、部分木だけをローカルに調整するため、全体をスキャンする必要はない

## テストケース
```python
pq = PriorityQueue([2, 3, 43, 2, 53, 6, 75, 10])
print(pq.pop())  # 75
print(pq.pop())  # 53
print(pq.pop())  # 43
print(pq.pop())  # 10
```

# 実行結果
```python
75
53
43
10
```

## 気づき
- pop() の中で maxHeap のルートを末尾で上書き → 削除 → 再構成という流れが自然に理解できるようになってきた。
- ライブラリを利用するイメージができるようになってきた。

## 解いた日
2025-7-4
