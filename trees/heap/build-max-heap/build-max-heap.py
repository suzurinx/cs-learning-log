def heapify(intArr, heapSize, i): # i:インデックス
    left = i * 2 + 1
    right = i * 2 + 2
    maxIndex = i
    if left < heapSize and intArr[left] > intArr[maxIndex]:
        maxIndex = left
    if right < heapSize and intArr[right] > intArr[maxIndex]:
        maxIndex = right
    if maxIndex != i:
        intArr[i], intArr[maxIndex]= intArr[maxIndex], intArr[i]
        heapify(intArr, heapSize, maxIndex)

def buildMaxHeap(intArr):
    heapSize = len(intArr)
    for i in range((heapSize - 2) // 2, -1 , -1):
        heapify(intArr, heapSize, i)
    return intArr

# テスト実行
print(buildMaxHeap([1,2,3]))
print(buildMaxHeap([-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]))
print(buildMaxHeap([7,8,2,3,1,4,3,2]))
print(buildMaxHeap([8,4,13,10,18]))
print(buildMaxHeap([3,100,201,56,8,591,985,291]))
print(buildMaxHeap([879,487,98,397,610,150,474,977,404,478,623,554,306]))