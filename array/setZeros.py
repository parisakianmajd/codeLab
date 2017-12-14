#Given an m x n matrix of 0s and 1s, if an element is 0, set its entire row and column to 0.
#Do it in place.

def setZeroes(A):
        n, m = len(A), len(A[0])

        c = False
        for i in range(n):
            if A[i][0] == 0:
                c = True
                break
            
        l = False
        for i in range(m):
            if A[0][i] == 0:
                l = True
                break
        
        for i in range(n):
            for j in range(m):
                if A[i][j] == 0:
                    A[0][j] = 2
                    A[i][0] = 2
        
        for i in xrange(1,n):
            for j in xrange(1,m):
                if A[i][0] == 2:
                    A[i][j] = 0
                elif A[0][j] == 2:
                    A[i][j] = 0    

        for i in range(n):
            if A[i][0] > 1 or c:
                A[i][0] = 0
        
        for i in range(m):
            if A[0][i] > 1 or l:
                A[0][i] = 0
        return A

    
A  = [[0,0],[1,1]]

print setZeroes(A)
