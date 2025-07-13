# 自然数の配列と、配列の各要素に特定の処理を実行するコールバック関数
def customArray(function, array):
    for value in array:
        print(function(value))

# 整数nを受け取って、3乗する関数
def cube(n):
    return n ** 3

# 整数nを受け取って、全ての桁数を合計して返す関数
def splitAndAdd(n):
    if n < 10:
        return n
    return splitAndAdd(n // 10) + n % 10

# テスト実行
customArray(cube, [3, 11, 24, 31])
# 27
# 1331
# 13824
# 29791

customArray(splitAndAdd, [3, 11, 24, 31])
# 3
# 2
# 6
# 4