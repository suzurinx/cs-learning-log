# ノードを作成
class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# レベル順二分木を作成
# arrList: ルートがリストの先頭、左右は順次追加、Noneは子ノードなし
# キューを利用して順次ノードを割り当てる
# バリテーション：not arrListはNoneを返す
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

# 深さの定義：ルートは深さ？
# 深さは再帰で測る
# ベースケース：root is NoneはNoneを返す
def maximumDepth(root):
    if root is None:
        return -1
    leftDepth = maximumDepth(root.left)
    rightDepth = maximumDepth(root.right)
    return max(leftDepth, rightDepth) + 1

# テストケース

print(maximumDepth(toBinaryTree([0])))
print(maximumDepth(toBinaryTree([0,1,None])))
print(maximumDepth(toBinaryTree([0,-10,5,None,-3,None,9])))
print(maximumDepth(toBinaryTree([5,2,18,-4,3])))
print(maximumDepth(toBinaryTree([27,14,35,10,19,31,42])))
print(maximumDepth(toBinaryTree([30,15,60,7,22,45,75,None,None,17,27])))
print(maximumDepth(toBinaryTree([90,50,150,20,75,95,175,5,25,66,80,92,111,166,200])))
print(maximumDepth(toBinaryTree([50,17,76,9,23,54,None,None,14,19,None,None,72])))
print(maximumDepth(toBinaryTree([16,14,10,8,7,9,3,2,4,1])))
print(maximumDepth(toBinaryTree([30,15,60,7,22,45,75,1,None,17,27,None,None,None,None,-1])))