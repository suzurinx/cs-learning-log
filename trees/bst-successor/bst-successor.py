class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# level-order で木構造を構築する
# (テストケースがすでにBSTであることを保証しているため実装が簡単な level-order を選択する)
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

        if i < len(arr) and arr[i] is not None:
            node.right = BinaryTree(arr[i])
            queue.append(node.right)
        i += 1

    return root


# 最小値を探す関数
# （SBTの構造なら、最左部のノードが最小値となる）
def minimumNode(root):
    iterator = root
    while iterator is not None and iterator.left is not None:
        iterator = iterator.left
    return iterator


# key と一致するノードを探索する
# key にもバリテーションをかける、かけないに関しては呼び出し側の責任で対応する
def findNode(root, key):
    iterator = root
    while iterator is not None:
        if iterator.data == key:
            return iterator
        if iterator.data > key:
            iterator = iterator.left
        else:
            iterator = iterator.right

    # 条件に一致しなかった場合には None を返すが、それは iterator を返すことでできる
    # が明示的にした方がわかりやすいので None を返すことにする
    return None


# メイン関数、後継者（サクセッサー）
def successor(root, key):
    # key と同じノードを探索して、targetNode と命名する
    targetNode = findNode(root, key)

    # targetNode がない場合は、Nodeを返す
    if targetNode is None:
        return None
    # targetNode の右側がある場合は、その部分木の最小値を返す
    if targetNode.right is not None:
        return minimumNode(targetNode.right)

    successor = None
    iterator = root
    while iterator is not None:
        if targetNode.data == iterator.data:
            return successor

        if targetNode.data < iterator.data:
            successor = iterator
            iterator = iterator.left
        else:
            iterator = iterator.right

    return successor


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

    # 末尾の None を削除して見た目を整える
    while result and result[-1] is None:
        result.pop()

    return result


# テストケース
print(printTree(successor(toBinaryTree([5, 4, None]), 5)))
print(
    printTree(
        successor(
            toBinaryTree(
                [
                    -2,
                    -17,
                    8,
                    -18,
                    -11,
                    3,
                    19,
                    None,
                    None,
                    None,
                    -4,
                    None,
                    None,
                    None,
                    25,
                ]
            ),
            8,
        )
    )
)
print(
    printTree(
        successor(
            toBinaryTree([3, -3, 13, -7, 1, 6, 18, -10, -4, 0, 2, 5, 8, 15, 19]), 6
        )
    )
)
print(
    printTree(
        successor(
            toBinaryTree([3, -3, 13, -7, 1, 6, 18, -10, -4, 0, 2, 5, 8, 15, 19]), 3
        )
    )
)
print(
    printTree(
        successor(
            toBinaryTree(
                [1, -5, 15, -9, -4, 10, 17, None, -6, None, 0, None, 14, 16, 19]
            ),
            10,
        )
    )
)
print(printTree(successor(toBinaryTree([0, -10, 5, None, -3, None, 9]), -3)))
