class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# 二分探索木を構築する
def toBinaryTree(arrList):
    if not arrList:
        return None
    root = BinaryTree(arrList[0])
    queue = [root]
    i = 1
    while i < len(arrList):
        current = queue.pop(0)
        if arrList[i] is not None:
            current.left = BinaryTree(arrList[i])
            queue.append(current.left)
        i += 1
        if i < len(arrList) and arrList[i] is not None:
            current.right = BinaryTree(arrList[i])
            queue.append(current.right)
        i += 1
    return root

# 中順走査で要素を集める
# 副作用型
def inOrderTraversal(root, result):
    if root is None:
        return None
    inOrderTraversal(root.left, result)
    result.append(root.data)
    inOrderTraversal(root.right, result)

# 2つのリストに含まれる全ての整数を昇順でリストとして返す
def allElementsSorted(list1, list2):
    result1, result2 = [], []
    inOrderTraversal(list1, result1)
    inOrderTraversal(list2, result2)
    merged = []
    i = j = 0
    while i < len(result1) and j < len(result2):
        if result1[i] < result2[j]:
            merged.append(result1[i])
            i += 1
        else:
            merged.append(result2[j])
            j += 1
    merged.extend(result1[i:])
    merged.extend(result2[j:])
    return merged

# テストケース
print(allElementsSorted(toBinaryTree([9,8,11]), toBinaryTree([3,1,5])))
print(allElementsSorted(toBinaryTree([3,None,5]), toBinaryTree([2,1,6])))
print(allElementsSorted(toBinaryTree([73,11,90,None,24,79,93]), toBinaryTree([44,39,49,36,41,46,72,None,None,None,None,None,None,None,86])))
print(allElementsSorted(toBinaryTree([29,14,48,1,20,42,76,None,None,None,None,None,None,None,97]), toBinaryTree([46,21,85,7,27,73,98])))
print(allElementsSorted(toBinaryTree([22,19,54,4,21,28,56]), toBinaryTree([29,10,64,4,28,32,75,None,None,None,None,None,None,None,100])))