class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def printInOrder(self):
        self.inOrderWalk(self)
        print("")

    def inOrderWalk(self, tRoot):
        if tRoot is not None:
            self.inOrderWalk(tRoot.left)
            print(str(tRoot.data), end=' ')
            self.inOrderWalk(tRoot.right)

# BSTとプロパティの詰め合わせ
class BinarySearchTree:
    def __init__(self, arrList):
        sortedList = sorted(arrList)
        self.root = BinarySearchTree.sortedArrayToBST(sortedList)

    # リストを取得し、BSTを作成する
    @staticmethod
    def sortedArrayToBST(array):
        def helper(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            left = helper(start, mid-1)
            right = helper(mid+1, end)
            root = BinaryTree(array[mid], left, right)
            return root
        return helper(0, len(array)-1)

    # BST内でkeyと一致するnodeを返す。見つからなければNoneを返す。
    def search(self, key):
        iterator = self.root
        while iterator is not None:
            if iterator.data == key:
                return iterator
            if iterator.data > key:
                iterator = iterator.left
            else:
                iterator = iterator.right
        return None

    # BST内にkeyが存在するか判定し、True/Falseで返す
    def keyExist(self, key):
        iterator = self.root
        while iterator is not None:
            if iterator.data == key:
                return True
            if iterator.data > key:
                iterator = iterator.left
            else:
                iterator = iterator.right
        return False

    # BST内から指定ノードの親を返す
    # -ルートからたどっていき、
    # -探したいnodeにたどり着くまで「親」を記録し続ける
	# -iterator is not nodeの間ループ → 最後にparentが直前の親ノードになる
    def findParent(self, node):
        iterator = self.root
        parent = None
        while iterator is not node:
            parent = iterator
            if iterator.data > node.data:
                iterator = iterator.left
            else:
                iterator = iterator.right
        return parent

    # nodeParent(親ノード)と子ノード、targetを引数にとり、ポインターを接続する
    def transplant(self, nodeParent, node, target):
        if nodeParent is None:
            self.root = target
        elif nodeParent.left == node:
            nodeParent.left = target
        else:
            nodeParent.right = target

    # 引数ノードの左側最深部ノードを返す
    def minimumNode(self, node):
        iterator = node
        while iterator and iterator.left:
            iterator = iterator.left
        return iterator

    # 引数ノードの後継ノードを見つけて返す
    def findSuccessor(self, node):
        targetNode = node
        if targetNode is None:
            return None
        if targetNode.right:
            return self.minimumNode(targetNode.right)
        successor = None
        iterator = self.root
        while iterator:
            if targetNode.data == iterator.data:
                return successor
            if targetNode.data < iterator.data and successor is None or iterator.data < successor.data:
                successor = iterator
            if targetNode.data < iterator.data:
                iterator = iterator.left
            else:
                iterator = iterator.right
        return successor


    # BST内で指定keyと一致するノードを削除する
    def deleteNode(self, key):
        if self.root is None:
            return
        # keyと一致するノードを探索し、変数nodeに格納する
        node = self.search(key)
        #BST内に指定keyがない場合は、何もせず現在のルートを返す(←状態を返すとも言う)
        if self.keyExist(key) == False:
            return self.root

        # 親ノードを変数parentに格納する
        parent = self.findParent(node)

        # case 1: 削除対象ノードが葉ノード
        if node.left is None and node.right is None:
            if parent.left.data == key:
                parent.left = None
            elif parent.right.data == key:
                parent.right = None

        # case 2: 削除対象ノードの左が空
        if node.left is None:
            self.transplant(parent, node, node.right)

        # case 3: 削除対象ノードの右が空
        elif node.right is None:
            self.transplant(parent, node, node.left)

        # case 4: 削除対象ノードが二つの子ノードを持っている
        else:
            # keyノードの後継ノードを格納する
            successor = self.findSuccessor(node)
            # keyノードの親ノードを格納する
            successorP = self.findParent(successor)

            if successor is not node.right:
                self.transplant(successorP, successor, successor.right)
                successor.right = node.right

            self.transplant(parent, node, successor)
            successor.left = node.left

    def printSorted(self):
        self.root.printInOrder()


# テスト
balancedBST = BinarySearchTree([4,43,36,46,32,7,97,95,34,8,96,35,85,1010,232])
balancedBST.printSorted()
balancedBST.deleteNode(43)
balancedBST.printSorted()
balancedBST.deleteNode(7)
balancedBST.printSorted()
balancedBST.deleteNode(4)
balancedBST.printSorted()
balancedBST.deleteNode(1010)

balancedBST.deleteNode(0)
balancedBST.printSorted()