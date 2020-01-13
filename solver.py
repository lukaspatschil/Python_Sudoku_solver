def solveSudoku(board):
    if not pos = nextSpace(board):
        return True
    
    for i in range(1, 10):
        if isValid(board, pos, i):
            board[pos[0],pos[1]] = i

            if solveSudoku(board):
                return True
            
            board[pos[0]][pos[1]] = 0
        
    return False

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
    for i in range(pos[0] / 3, pos[0] / 3 + 3):
        for j in range(pos[1] / 3, pos[1] / 3 + 3):
            if board[i][j] == n:
                return False

    return True

def nextSpace(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)
    return False

def printBoard(board):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" | ",end="")

            if j == 8:
                print(bo[i][j], end="\n")
            else:
                print(str(bo[i][j]) + " ", end="")

def main():
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    if solveSudoku(board):
        printBoard(board)

main()
