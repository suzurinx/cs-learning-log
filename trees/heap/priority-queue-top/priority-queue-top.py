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
        """最大値（ヒープの先頭）を取得"""
        return self.maxHeap[0]


# テスト実行
pq1 = PriorityQueue([2, 3, 43, 2, 53, 6, 75, 10])
print(pq1.top())  # 75

pq2 = PriorityQueue([3, 12, 0, 2, 9, 1, 65, 32])
print(pq2.top())  # 65

pq3 = PriorityQueue([1, 2, 3, 4, 8, 2, 1, 9, 7, 3, 4])
print(pq3.top())  # 9