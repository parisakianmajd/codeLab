def isSafe(board, row, col, N):
     for i in range(col):
          if board[row][i] == 1:
               return False
     # Check upper diagonal on the left
     for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False
     # Check lower diagonal on the left
     for i,j in zip(range(row,N,1), range(col,-1,-1)):
         if board[i][j] == 1:
              return False
     return True
 
def solveNQUtil(board, col, N):
    if col >= N:
        return True
 
    # find a safe place for this queen and ensure if doesn't attack others
    for i in range(N):
        if isSafe(board, i, col, N):
            # If the current state is safe, place this queen in board[i][col]
            board[i][col] = 1
 
            # Check if this placement results in a safe state
            if solveNQUtil(board, col+1, N):
                return True
            # If placing the queen on board[i][col] is not safe remove it
            board[i][col] = 0
    return False
 

def solveNQ(N):
     board = [[0 for i in xrange(N)] for j in xrange(N)]
     
     if solveNQUtil(board, 0, N) == False:
        return False
     
     for b in board:
          print b
     return True
 
solveNQ(4)
 
