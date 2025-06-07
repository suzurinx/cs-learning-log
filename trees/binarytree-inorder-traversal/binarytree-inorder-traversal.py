class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    # 木構造を間順走査で出力する
    # 分けることもできるが今回はネストする
    def printInOder(self):
        def inOrderWalk(node):
            if node:
                inOrderWalk(node.left)
                print(str(node.data), end = " ")
                inOrderWalk(node.right)
        inOrderWalk(self)
        print()

class BinarySearchTree:
    def __init__(self, arrList):
        sortedList = sorted(arrList)
        self.root = BinarySearchTree.sortedArrayToBST(sortedList)

    @staticmethod
    def sortedArrayToBST(arr):
        def helper(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            left = helper(start, mid - 1)
            right = helper(mid + 1, end)
            root = BinaryTree(arr[mid], left, right)
            return root
        return helper(0, len(arr) - 1)


# テストケース
balancedBST = BinarySearchTree([1,2,3,4,5,6,7,8,9,10,11])
balancedBST2 = BinarySearchTree([4,43,36,46,32,7,97,95,34,8,96,35,85,1010,232])
balancedBST.root.printInOder()
balancedBST2.root.printInOder()
