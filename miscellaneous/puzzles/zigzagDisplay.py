#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

#P.......A........H.......N
#..A..P....L....S....I...I....G
#....Y.........I........R
#And then read line by line: PAHNAPLSIIGYIR

def zigzag(word, n):
    if n < 1:
        return
    if n == 1:
        return word
    result = [''] * n
    binNum = 0
    direct = 1
    for a in word:
        result[binNum]+=a
        binNum += direct
        if binNum == 0 or binNum == n-1:
            direct = -direct
    return "".join(result)
    

A = "PAYPALISHIRIBG"
print zigzag(A, 3)
