#Given an integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.



def generateSpiralMatrix(A):
    arr = [[0 for i in xrange(A)] for j in xrange(A)]
    T = 0
    B = A - 1
    L = 0
    R = A - 1
    direct = 0 # 0:L to R-- 1: T to D-- 2: R to L --3: D to T
    num = 1
    while T <= B and L <= R:
        if direct == 0:
            for i in xrange(L,R+1):
                arr[T][i] = num
                num += 1
            T += 1
        if direct == 1:
            for i in xrange(T, B+1):
                arr[i][R] = num
                num += 1
            R -= 1
        if direct == 2:
            for i in xrange(R, L-1, -1):
                arr[B][i] = num
                num += 1
            B -= 1
        if direct == 3:
            for i in xrange(B, T-1, -1):
                arr[i][L] = num
                num += 1
            L += 1
        direct = (direct + 1) % 4
    return arr


print generateMatrix(3)
