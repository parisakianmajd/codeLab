#Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#  1 -> A
#  26 -> Z
#  28 -> AB

def numToCol(num):
    column = ""
    while num > 0:
        num, remainder = divmod(num - 1, 26)
        column = chr(ord('A') + remainder) + column
    return column

def colToNum(col):
    num = 0
    for c in col:
        num = num * 26 + (ord(c.upper()) - ord('A')) + 1
    return num


print numToCol(28)
print colToNum('AB')
