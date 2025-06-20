class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

"""
# 二分木を作成する（再帰：内部関数型）
def toBinaryTree(arrList):
    if not arrList:
        return None
    def helper(i):
        if i >= len(arrList) or arrList[i] is None:
            return None
        node = BinaryTree(arrList[i])
        node.left = helper(2*i+1)
        node.right = helper(2*i+2)
        return node
    return helper(0)
"""

"""
# 二分木を作成する（再帰：ヘルパー型）
def toBinaryTree(arrList):
    if not arrList:
        return None
    return toBinaryTreeHelper(arrList, 0)

def toBinaryTreeHelper(arrList, i):
    if i >= len(arrList) or arrList[i] is None:
        return None
    node = BinaryTree(arrList[i])
    node.left = toBinaryTreeHelper(arrList, 2*i+1)
    node.right = toBinaryTreeHelper(arrList, 2*i+2)
    return node
"""

# 二分木を作成する（キュー）
# スタック（pop()） を利用した構築方法もあるが、テストケースはレベル順で構築することが前提になっていると推測
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


# 最新部にあるノードの合計値を求める
def deepestLeaves(root):
    if not root:
        return 0
    total = 0
    queue = [root]
    result = deepestLeavesHelper(queue)
    for node in result:
        total += node.data
    return total

# 最新部のノードを求める（再帰版）
def deepestLeavesHelper(queue):
    child = []
    for node in queue:
        if node.left:
            child.append(node.left)
        if node.right:
            child.append(node.right)
    if child:
        return deepestLeavesHelper(child)
    else:
        return queue

"""
# 最新部のノードを求める（ループ版）
def deepestLeavesHelper(queue):
    while queue:
        child = []
        for node in queue:
            if node.left:
                child.append(node.left)
            if node.right:
                child.append(node.right)
        if not child:
            return queue
        else:
            queue = child
"""

print(deepestLeaves(toBinaryTree([3,2,1,None,7,8])))
print(deepestLeaves(toBinaryTree([5,8,1,10,12,8,None,None,None,None,None,9,10])))
print(deepestLeaves(toBinaryTree([5,2,18,4,3])))
print(deepestLeaves(toBinaryTree([27,14,35,10,19,31,42])))
print(deepestLeaves(toBinaryTree([30,15,60,7,22,45,75,None,None,17,27])))
print(deepestLeaves(toBinaryTree([50,17,76,9,23,54,None,None,14,19,None,None,72])))
print(deepestLeaves(toBinaryTree([16,14,10,8,7,9,3,2,4,1])))
print(deepestLeaves(toBinaryTree([0,-10,5,None,-3,None,9])))