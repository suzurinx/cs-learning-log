class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def printPostOrder(self):
        self.printPostTraversal()
        print()

    # 左 > 右 > ルートで走査する
    def printPostTraversal(self):
        if self.left:
            self.left.printPostTraversal()
        if self.right:
            self.right.printPostTraversal()
        print(str(self.data), end=" ")

class BinarySearchTree:
    def __init__(self, arrList):
        sortedList = sorted(arrList)
        self.root = BinarySearchTree.sortedArrayToBST(sortedList)

    @staticmethod
    def sortedArrayToBST(arrList):
        return BinarySearchTree.sortedArrayToBSTHelper(arrList, 0, len(arrList) -1)

    @staticmethod
    def sortedArrayToBSTHelper(arrList, start, end):
        # バリテーション
        if start > end:
            return None

        mid = (start + end) // 2
        left = BinarySearchTree.sortedArrayToBSTHelper(arrList, start, mid-1)
        right = BinarySearchTree.sortedArrayToBSTHelper(arrList, mid+1, end)
        root = BinaryTree(arrList[mid], left, right)

        return root

    def printSorted(self):
        self.root.printPostOrder()

# test
balancedBST = BinarySearchTree([1,2,3,4,5,6,7,8,9,10,11])
balancedBST2 = BinarySearchTree([4,43,36,46,32,7,97,95,34,8,96,35,85,1010,232])
balancedBST.printSorted()
balancedBST2.printSorted()