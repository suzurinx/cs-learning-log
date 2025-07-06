# インデックスiの要素起点で最大ヒープを構築
def heapify(intArr, heapSize, i):
    # インデックス
    left = i * 2 + 1 # 左の子ノード
    right = i * 2 + 2 # 右の子ノード
    largest = i # 最大値のあるノード

    # largestの方が小さい場合、インデックスを入れ替える
    if left < heapSize and intArr[left] > intArr[largest]:
        largest = left
    if right < heapSize and intArr[right] > intArr[largest]:
        largest = right
    # スワップ(largestに変更がある場合に実行)
    if largest != i:
        intArr[largest], intArr[i] = intArr[i], intArr[largest]
        # 子ノードが変わっているため、ここを起点に最大ヒープを再帰的に実行
        heapify(intArr, heapSize, largest)

# 最大ヒープを構築
def buildMaxHeapify(intArr, heapSize):
    for i in range((heapSize // 2 - 1), -1, -1):
        heapify(intArr, heapSize, i)

def heapsort(intArr):
    n = len(intArr)
    buildMaxHeapify(intArr, n)
    for lastIndex in range(n - 1, 0, -1):
        intArr[lastIndex], intArr[0] = intArr[0], intArr[lastIndex]
        heapify(intArr, lastIndex)

# TODO:インデックスの扱いと範囲の扱いで混乱しているため中断中 ヒープで設計的な違和感（インデックス vs サイズ）に苦戦。
# 設計意図を明確にできるように後で整理する（2025-07-06 現在は混乱中）

