# Count all possible paths from top left to bottom right of a mXn matrix
# from each cell you can either move only to right or down

# recursive
def uniquePaths_recur(A, B):
    if A == 1 or B == 1:
        return 1
    return uniquePaths_recur(A-1, B) + uniquePaths_recur(A, B-1)
#DP
def uniquePaths(A, B):
    count = [[1 for x in range(B)] for y in range(A)]

    for i in range(A):
        count[i][0] = 1
   
    for j in range(B):
        count[0][j] = 1

    for i in range(1, A):
        for j in range(1,B):             
            count[i][j] = count[i-1][j] + count[i][j-1]
    return count[-1][-1]

print uniquePaths(2,2)
