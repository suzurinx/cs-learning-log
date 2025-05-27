# 再帰処理
def keyExistRecursive(key, sbt):
    if sbt is None:
        return False
    if sbt.data == key:
        return True
    if key < sbt.data:
        return keyExistRecursive(key, sbt.left)
    return keyExistRecursive(key, sbt.right)


# イテレーター処理
def keyExistIterative(key, sbt):
    iterator = sbt
    while iterator:
        if iterator.data == key:
            return True
        if key < iterator.data:
            iterator = iterator.left
        else:
            iterator = iterator.right
    return False
