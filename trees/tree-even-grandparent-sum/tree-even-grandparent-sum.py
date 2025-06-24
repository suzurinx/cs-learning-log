class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
"""
# レベル順（キュー）
def toBinaryTree(arrList):
    if not arrList:
        return None
    root = BinaryTree(arrList[0])
    queue = [root]
    i = 1
    while i < len(arrList):
        node = queue.pop(0)
        if arrList[i] is not None:
            node.left = BinaryTree(arrList[i])
            queue.append(node.left)
        i += 1
        if i < len(arrList) and arrList[i] is not None:
            node.right = BinaryTree(arrList[i])
            queue.append(node.right)
        i += 1
    return root
"""

# 再帰
def toBinaryTree(arrList):
    def helper(i):
        if i >= len(arrList) or arrList[i] is None:
            return None
        node = BinaryTree(arrList[i])
        node.left = helper(2 * i + 1)
        node.right = helper(2 * i + 2)
        return node
    return helper(0) if arrList else None

def totalEvenGrandparent(root):
    if root is None:
        return 0
    def dfs(node, parent=None, grandparent=None):
        if node is None:
            return 0
        total = 0
        if grandparent and grandparent.data % 2 == 0:
            total += node.data
        total += dfs(node.left, node, parent)
        total += dfs(node.right, node, parent)
        return total
    return dfs(root)

print(totalEvenGrandparent(toBinaryTree([8,9,11])))
print(totalEvenGrandparent(toBinaryTree([8,9,11,3,None,None,2])))
print(totalEvenGrandparent(toBinaryTree([57,33,77,9,40,61,92,7,14,35,46,59,63,78,96,None,None,None,23,None,37,None,47,None,None,None,76,None,84,None,99])))  # 267
print(totalEvenGrandparent(toBinaryTree([41,15,70,8,28,55,78,4,10,21,34,47,63,74,83,2,6,9,14,16,25,33,35,46,50,56,65,72,75,81,90,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,40,None,None,None,None,None,None,None,69,None,None,None,None,None,None,None,96])))
print(totalEvenGrandparent(toBinaryTree([52,33,72,17,39,63,85,10,25,35,44,58,69,80,98,5,12,18,27,34,36,40,48,53,59,66,70,73,82,89,99,None,None,None,16,None,22,None,28,None,None,None,37,None,43,None,49,None,None,None,60,None,68,None,71,None,79,None,83,None,94,None,99])))