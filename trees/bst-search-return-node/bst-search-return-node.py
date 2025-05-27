class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def toBinaryTree(arr):
    # ベースケース
    # if arr in None
    # 明示的にNoneを受け取る設計に向いている
    # not arrの利点
    # None / [] / '' / 0 などの「空っぽ系」全般に幅広く「空」のケースを防ぎたいとき
    if not arr:
        return None