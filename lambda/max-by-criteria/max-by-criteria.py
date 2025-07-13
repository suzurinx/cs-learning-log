# 配列内の最大の文字列を返す
def maxByCriteria(function, array):
    maxArray = array[0]
    for c in array[1:]:
        if not function(maxArray, c):
            maxArray = c
    return maxArray

# s1 と s2 を受け取り、s1 の長さが s2 の長さ以上の場合に true、それ以外の時に false を返す関数
def compareLength(s1, s2):
    return len(s1) >= len(s2)
# s1 と s2 を受け取り、s1 の ASCII 値の合計が s2 の合計以上の場合に true、それ以外の時に false を返す関数
def compareAsciiTotal(s1, s2):
    return sum(ord(c) for c in s1) >= sum(ord(c) for c in s2)

print(maxByCriteria(compareLength, ["apple", "yumberry", "grape", "banana","mandarin"])) # mandarin
print(maxByCriteria(compareLength, ["zoomzoom", "choochoo", "beepbeep", "ahhhahhh"])) # ahhhahhh
print(maxByCriteria(compareAsciiTotal, ["apple", "yumberry", "grape", "banana","mandarin"])) # yumberry
print(maxByCriteria(compareAsciiTotal, ["zoom", "choochoo", "beepbeep", "ahhhahhh"])) # choochoo