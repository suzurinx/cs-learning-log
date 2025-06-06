class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


def sortedArrToBST(numberList):
    def helper(start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        left = helper(start, mid - 1)
        right = helper(mid + 1, end)
        return BinaryTree(numberList[mid], left, right)
    return helper(0, len(numberList) -1)

def inOrderTraversal(node):
    if node is None:
        return []
    return inOrderTraversal(node.left) + [node.data] + inOrderTraversal(node.right)

print(inOrderTraversal(sortedArrToBST([1,2,3])))
print(inOrderTraversal(sortedArrToBST([1,2,3,5,6,9,10])))
print(inOrderTraversal(sortedArrToBST([-1,0,3,10,13,19,22])))
print(inOrderTraversal(sortedArrToBST([1,3,4,5,8])))
print(inOrderTraversal(sortedArrToBST([1,4,6,10,11,14,15,20,22,25,50,61,68,72])))