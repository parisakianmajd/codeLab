#Given a matrix of m * n elements (m rows, n columns),
# return all elements of the matrix in spiral order.
import itertools


def spiral(arr):
    result = []
    m = len(arr)
    n = len(arr[0])
    T = 0
    B = m -1
    L = 0
    R = n - 1
    direct = 0 # 0:L to R-- 1: T to D-- 2: R to L --3: D to T
    while T <= B and L <= R:
        if direct == 0:
            for i in xrange(L,R+1):
                result.append(arr[T][i])
            T += 1
        if direct == 1:
            for i in xrange(T, B+1):
                result.append(arr[i][R])
            R -= 1
        if direct == 2:
            for i in xrange(R, L-1, -1):
                result.append(arr[B][i])
            B -= 1
        if direct == 3:
            for i in xrange(B, T-1, -1):
                result.append(arr[i][L])
            L += 1
        direct = (direct + 1) % 4
    return result

# 1- print topRow
# 2- Transpose and flip upside-down (same as rotate 90 degrees counter-clockwise)
# repeat 1
def transpose_and_yield_top(arr):
    while arr:
        yield arr[0]
        arr = list(reversed(zip(*arr[1:])))



arr = [[ 1, 2, 3 ],\
       [ 4, 5, 6 ],\
       [ 7, 8, 9 ]]
arr2 = [[1, 2, 3],\
        [4, 5, 6]]
print spiral(arr)
print spiral (arr2)
print list(itertools.chain(*transpose_and_yield_top(arr)))
