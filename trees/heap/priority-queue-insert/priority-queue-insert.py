import math


class HeapLibrary:
    @staticmethod
    def buildMaxHeap(arr):
        """配列全体を最大ヒープに変換する"""
        # 最後の親ノードのインデックスを取得
        lastParent = HeapLibrary.parent(len(arr) - 1)

        # 最後の親ノードから先頭に向かって maxHeapify を適用
        for i in range(lastParent, -1, -1):
            HeapLibrary.maxHeapify(arr, len(arr) - 1, i)

    @staticmethod
    def maxHeapify(arr, heapEnd, i):
        """部分木の根を i としたときに、ヒープ条件を満たすよう再構成する"""
        l = HeapLibrary.left(i)
        r = HeapLibrary.right(i)
        biggest = i

        if l <= heapEnd and arr[l] > arr[biggest]:
            biggest = l
        if r <= heapEnd and arr[r] > arr[biggest]:
            biggest = r

        if i != biggest:
            arr[i], arr[biggest] = arr[biggest], arr[i]
            HeapLibrary.maxHeapify(arr, heapEnd, biggest)

    # 以下はインデックス計算用のユーティリティメソッド
    @staticmethod
    def left(i):
        return i * 2 + 1

    @staticmethod
    def right(i):
        return i * 2 + 2

    @staticmethod
    def parent(i):
        return math.floor((i - 1) / 2)


class PriorityQueue:
    def __init__(self, arr):
        """最大ヒープを用いた優先度付きキューの初期化"""
        self.maxHeap = arr[:]
        HeapLibrary.buildMaxHeap(self.maxHeap)

    def top(self):
        """最大値（ヒープの先頭）を参照する"""
        return self.maxHeap[0]

    def pop(self):
        """最大値(ヒープの先頭)を取り出す"""
        maxValue = self.top()
        self.maxHeap[0] = self.maxHeap[-1]
        self.maxHeap.pop()
        HeapLibrary.maxHeapify(self.maxHeap, len(self.maxHeap) - 1, 0)
        return maxValue

    # 引数xは追加する要素
    def insert(self, x):
        """新しい値 x を最大ヒープに追加"""
        # ヒープ配列の最後にxを追加する
        self.maxHeap.append(x)
        # xのインデックスを渡す
        self._siftUp(len(self.maxHeap) - 1)

    def _siftUp(self, i):
        # 追加した要素の親を探す
        parent = HeapLibrary.parent(i)
        # 範囲指定で最低でもrootを示しておいてエラーを防止
        while parent >= 0 and self.maxHeap[parent] < self.maxHeap[i]:
            # 条件に合うときにスワップ
            self.maxHeap[parent], self.maxHeap[i] = self.maxHeap[i], self.maxHeap[parent]
            # インデックスを更新
            i = parent
            # 次の親ノードをロックオン
            parent = HeapLibrary.parent(i)

# テスト実行
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