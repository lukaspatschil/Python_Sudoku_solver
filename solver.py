def solveSudoku(board):

def isValid(board, pos, n):
    # colom
    for i in range(len(board)):
        if board[pos[0]][i] == n:
            return False

    #row
    for i in range(len(board[pos[0]])):
        if board[i][pos[1]] == n:
            return False

    #square
    

def nextSpace(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)
    return False