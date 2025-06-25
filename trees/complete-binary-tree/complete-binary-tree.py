# 完全二分木：
# 最下層以外の階層のノードが詰まっており、再下層のノードは左側に詰まっている二分木

from collections import deque

class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

# レベル順で二分木を実装
def toBinaryTree(lst):
    if not lst:
        return None
    root = BinaryTree(lst[0])
    # dequeをインポートして効率化
    queue = deque()
    queue.append(root)
    i = 1
    while queue:
        node = queue.popleft()
        if i < len(lst) and lst[i] is not None: # list[i]だけでは、list[i] is not None と同じ意味にはならない
            node.left = BinaryTree(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = BinaryTree(lst[i])
            queue.append(node.right)
        i += 1
    return root

# フラグを利用して、状態遷移時に出力できるようにする
def isCompleteBinaryTree(root):
    # 空チェック：もしもrootがNoneならTrueを返す（完全二分木の定義上OK）
    if not root:
        return True
    # queue準備
    queue = deque()
    queue.append(root)
    # フラグ初期化
    foundNone = False
    # BFSループ
    while queue:
        node = queue.popleft()
        # Trueを返す
        if node is None:
            foundNone =True
        else:
            if foundNone:
                return False
            queue.append(node.left)
            queue.append(node.right)
    return True

# テストケース
print(isCompleteBinaryTree(toBinaryTree([0,1,2,3])))
print(isCompleteBinaryTree(toBinaryTree([0,1,2,3,4,5])))
print(isCompleteBinaryTree(toBinaryTree([0,1,2,4,5,None,7])))
print(isCompleteBinaryTree(toBinaryTree([0,1,3,4,None,7,8])))
print(isCompleteBinaryTree(toBinaryTree([0,1,2,3,None,6])))
print(isCompleteBinaryTree(toBinaryTree([97,10,77,32,40,70,32,96,27,10,12,90,73,100,86,None,96])))
print(isCompleteBinaryTree(toBinaryTree([11,7,75,9,59,83,60,46,6,12,26,28,26,91,98,83,7,None,31,66,77,23,None,100,40])))
print(isCompleteBinaryTree(toBinaryTree([38,67,22,52,0,29,43,41,55,97,82,33,85,5,80,3,94,46,0,32,88,59,59,38,64,83,78,47,13,41,89,90,17,36,53,56,1,8,36,92,8,None,78,33,81,86,None,10,6,31,27])))