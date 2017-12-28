def solveSudoko(A):
    def findUnassigned():
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == '.':
                    return i , j
        return -1 , -1
    
    
    def isValid(row , col , num):
        for j in range(len(A)):
            if A[row][j] == str(num):
                return False
        
        for i in range(len(A)):
            if A[i][col] == str(num):
                return False
                
        diffrow = row%3
        diffcol = col%3
        for i in range(row-diffrow , row+3-diffrow):
            for j in range(col-diffcol , col+3-diffcol):
                if A[i][j] == str(num):
                    return False
        
        return True
        
        
    
    def helper(row , col):
        row , col = findUnassigned()
        if row == -1:
            return True
        else:
            for i in range(1 ,10):
                if isValid(row , col , i):
                    A[row][col] = str(i)
                    if helper(row , col):
                        return True
                    A[row][col] = '.'
            return False
    helper(0 , 0)


A = ['53..7....', '6..195...', '.98....6.', '8...6...3', '4..8.3..1', '7...2...6', '.6....28.', '...419..5', '....8..79']
A = map(list, A)
solveSudoko(A)
print  A
