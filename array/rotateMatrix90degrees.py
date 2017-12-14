
def rotate(A):
    A = A[::-1]
    # transpose the matrix
    for i in range(len(A)):
        for j in range(i, len(A)):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    return A



def rotate2(A):
    return (zip(*A[::-1]))



A = [[1, 2],[3, 4]]

print rotate(A)
A = [[1, 2],[3, 4]]

print rotate2(A)
