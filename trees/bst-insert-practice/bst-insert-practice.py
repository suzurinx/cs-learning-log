class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # ラッパー関数
    # 改行するコントロール責任をこの関数に持たせる
    def printInOrder(self):
        self.inOrderWalk(self)
        print()

    # 中順でプリントする
    # データ型：str
    def inOrderWalk(self, root):
        if root is not None:
            self.inOrderWalk(root.left)
            print(str(root.data), end=" ")
            self.inOrderWalk(root.right)


class BinarySearchTree:
    # arrListを渡せば利用できるクラス設計にする
    def __init__(self, arrList):
        # インスタンスがrootだと便利なのでこれを実装する
        # インスタンスがない状態で実装するので、スタティックメソッドを利用する
        # 引数をソートした状態に調整する
        sortedArrayList = sorted(arrList)
        self.root = BinarySearchTree.sortedArrayToBST(sortedArrayList)

    @staticmethod
    def sortedArrayToBST(arrList):
        # バリテーション
        # [],0,Noneの入力を除外
        if not arrList:
            return None
        # endはインデックスと連動した数値にしたいので、len - 1で調整する
        return BinarySearchTree.sortedArrayToBSTHelper(arrList, 0, len(arrList) - 1)

    @staticmethod
    def sortedArrayToBSTHelper(arrList, start, end):
        # ベースケース
        # 子要素にできるものが何もない = 葉ノードに到達
        if start > end:
            return None
        # arrListの中央のインデックス要素を取得する
        mid = (start + end) // 2
        left = BinarySearchTree.sortedArrayToBSTHelper(arrList, start, mid - 1)
        right = BinarySearchTree.sortedArrayToBSTHelper(arrList, mid + 1, end)
        root = BinaryTree(arrList[mid], left, right)
        return root

    def insert(self, value):
        # ルートはインスタンス
        iterator = self.root
        # ノードがあるときにループを進める
        while iterator is not None:
            # バリューが同じノードデータを見つけたら、その時点でループを終える
            if iterator.data == value:
                return
            if iterator.data > value and iterator.left is None:
                iterator.left = BinaryTree(value)
                return
            elif iterator.data < value and iterator.right is None:
                iterator.right = BinaryTree(value)
                return
            iterator = iterator.left if iterator.data > value else iterator.right
    # returnを返すと関数が即時終了する
    # Noneが返されることになるが出力を代入して利用しないなら問題にならない。
    # insert関数は「状態を作る」ことが目的の関数だから、Noneを返す構造になっていても問題ない（これを利用しない）

    def printSorted(self):
        self.root.printInOrder()


# テストケース
balancedBST = BinarySearchTree([4,43,36,46,32,7,97,95,34,8,96,35,85,1010,232])
balancedBST.printSorted()
balancedBST.insert(5)
balancedBST.printSorted()
balancedBST.insert(47)
balancedBST.printSorted()
balancedBST.insert(0)
balancedBST.printSorted()