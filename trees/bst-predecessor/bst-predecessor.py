class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# 木構造を作る関数
# level-order で構築する
def toBinaryTree(arr):
    if not arr:
        return None

    root = BinaryTree(arr[0])
    queue = [root]
    i = 1

    while i < len(arr):
        node = queue.pop(0)

        if arr[i] is not None:
            node.left = BinaryTree(arr[i])
            queue.append(node.left)
        i += 1

        # and 検索では、範囲を先に評価する
        if i < len(arr) and arr[i] is not None:
            node.right = BinaryTree(arr[i])
            queue.append(node.right)
        i += 1

    return root

# 最大値を探す関数
# (BSTなので、右側のノードが最大値なことが保証される)
# (iterator を利用せず root を利用してもOK。今回は意図的に利用した。)
def maximumNode(root):
    iterator = root
    while iterator and iterator.right:
        iterator = iterator.right
    return iterator


# key と一致するノードを求める関数
def findNode(root, key):
    if not root:
        return None

    iterator = root
    while iterator:
        if iterator.data == key:
            return iterator
        elif iterator.data < key:
            iterator = iterator.right
        else:
            iterator = iterator.left
    return None

# メイン関数
def predecessor(root, key):
    # キーと同じノードを探索して命名する
    targetNode = findNode(root, key)

    if targetNode is None:
        return None

    # targetNode の左側にノードがある場合には、その部分木の最大値を返す
    if targetNode.left is not None:
        return maximumNode(targetNode.left)

    # それ以外の場合はルートから検索する
    # predecessor(前任者)
    # イテレーターがターゲットノードにたどり着くまでの間に、ターゲットノードより小さな値を一時保存していく
    predecessor = None
    iterator = root

    while iterator is not None:
        if iterator.data == targetNode.data:
            return predecessor

        if iterator.data < targetNode.data:
            predecessor = iterator
            iterator = iterator.right
        else:
            iterator = iterator.left

    return predecessor

# 木構造のリスト表示する関数
def printTree(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.data)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    return result

print(printTree(predecessor(toBinaryTree([0,-10,5,None,-3,None,9]), 5)))
print(printTree(predecessor(toBinaryTree([5,3,6,2,4,None,7]), 5)))
print(printTree(predecessor(toBinaryTree([10,6,12,4,8,None,None,2]), 12)))
print(printTree(predecessor(toBinaryTree([10,6,12,4,8,None,None,2]), 2)))
print(printTree(predecessor(toBinaryTree([5,None,7]), 5)))
print(printTree(predecessor(toBinaryTree([-2,-17,8,-18,-11,3,19,None,None,None,-4,None,None,None,25]), 8)))
print(printTree(predecessor(toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]), 6)))
print(printTree(predecessor(toBinaryTree([1,-5,15,-9,-4,10,17,None,-6,None,0,None,14,16,19]), 10)))