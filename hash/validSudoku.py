#Determine if a Sudoku is valid
#The Sudoku board could be partially filled, where empty cells are filled with the character '.'

def isValidSudoku(A):
    Alist = [list(a) for a in A]
    
    for a in Alist:
        row = [e for e in a if e != '.']
        if len(row) != len(set(row)):
            return 0
    cols = zip(*Alist)
    for c in cols:
        column = [e for e in c if e != '.']
        if len(column) != len(set(column)):
            return 0

    def checkSquare(h, w, matrix):
        lst = matrix[h][w:w+3]
        lst += matrix[h + 1][w:w+3]
        lst += matrix[h + 2][w:w+3]
        lst = [c for c in lst if c != '.']
        if len(lst) == len(set(lst)):
            return 1
        return 0
    for x in xrange(0, len(A), 3):
        for y in xrange(0, len(A), 3):
            if not checkSquare(x, y, A):
                return 0
    return 1
       
        


A = [ "....5..1.", ".4.3.....", ".....3..1", "8......2.", "..2.7....", ".15......", ".....2...", ".2.9.....", "..4......" ]
print isValidSudoku(A)
