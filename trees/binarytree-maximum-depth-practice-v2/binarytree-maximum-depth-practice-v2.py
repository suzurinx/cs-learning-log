class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# 問題で与えられている関数
# テストケースで、toBinaryTree([30,15,60,7,22,45,75,null,null,17,27])が渡されている
# テストケースから、バランス二分木だと推測できる
# root:arrListの先頭要素
# 方法:キューを利用した実装
# 例外処理:配列がない場合の処理を実装
def maximumDepth(root):
    # バリテーション
    if not root:
        return None
    # root（arrList）が一つだった場合、ノード一つ＝高さ0
    return maximumDepthHelper(root, -1)


def maximumDepthHelper(root, depth):
    # ベースケース
    # root操作終了時にカウントしていた深さを返す
    if root is None:
        return depth
    left = maximumDepthHelper(root.left, depth+1)
    right = maximumDepthHelper(root.right, depth+1)
    return max(left, right)



# テストケースからこのラッピングされている関数があることがわかる
# 私の環境で動作するように自力で実装する
def toBinaryTree(arrList):
    # 例外処理
    if arrList is None:
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