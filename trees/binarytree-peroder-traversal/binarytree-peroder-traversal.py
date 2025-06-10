class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def printPreOrder(self):
        self.preOrderWalk(self)

    # 前順走査
    def preOrderWalk(self):
        print(str(self.data), end="")
        if self.left:
            self.left.preOrderWalk()
        if self.right:
            self.right.preOrderWalk()


class BinarySearchTree:
    def __init__(self, arrList):
        sortedList = sorted(arrList)
        self.root = BinarySearchTree.sortedArrayToBST(sortedList)

    @staticmethod
    def sortedArrayToBST(sortedList):
        # バリテーション
        # []や0を除外する
        if not sortedList:
            return None
        return BinarySearchTree.sortedArrayToBSTHelper(sortedList, 0, len(sortedList) -1)

    @staticmethod
    def sortedArrayToBSTHelper(arr, start, end):
        # ベースケース
        # 葉ノードの先のノードを返して終わり（実際にはない）
        if start > end:
            return None
        mid = (start + end) // 2
        left = BinarySearchTree.sortedArrayToBSTHelper(arr, start, mid-1)
        right = BinarySearchTree.sortedArrayToBSTHelper(arr, mid+1, end)
        root = BinaryTree(arr[mid], left, right)
        return root

    def printSorted(self):
        self.root.preOrderWalk()
        print()

# test
balancedBST = BinarySearchTree([1,2,3,4,5,6,7,8,9,10,11])
balancedBST2 = BinarySearchTree([4,43,36,46,32,7,97,95,34,8,96,35,85,1010,232])
balancedBST.printSorted()
balancedBST2.printSorted()
