#solver.py
import time

def solveSudoku(board):
    global iterations
    pos = nextSpace(board)
    if not pos:
        return True
    
    row, col = pos

    for i in range(1, 10):
        if isValid(board, pos, i):
            board[row][col] = i
            iterations += 1

            if solveSudoku(board):
                return True
            
            board[row][col] = 0
        
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
    x = pos[1] // 3 * 3
    y = pos[0] // 3 * 3

    for i in range(y, y + 3):
        for j in range(x, x + 3):
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
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            for k in range((len(board) // 3)):
                print("- - -   ", end = "")
            print("", end = "\n")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end = "")

            if j == 8:
                print(board[i][j], end = "\n")
            else:
                print(str(board[i][j]) + " ", end = "")

def main():
    emptyBoard = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
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

    veryHardBoard = [
        [0, 0, 4, 0, 0, 0, 1, 8, 7],
        [0, 0, 0, 0, 0, 0, 5, 0, 3],
        [0, 8, 0, 0, 0, 9, 0, 0, 0],
        [0, 7, 0, 2, 0, 0, 0, 1, 0],
        [0, 3, 0, 0, 1, 0, 0, 2, 0],
        [0, 0, 0, 6, 0, 0, 8, 0, 0],
        [7, 9, 0, 0, 0, 0, 0, 6, 8],
        [0, 6, 3, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 4, 0, 0, 0, 9]
    ]

    board953 = [
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [8, 0, 9, 4, 6, 0, 7, 0, 2],
        [2, 0, 0, 0, 1, 8, 6, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 7, 0],
        [0, 0, 8, 0, 0, 0, 4, 0, 0],
        [0, 7, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 2, 9, 4, 0, 0, 0, 5],
        [4, 0, 6, 0, 3, 2, 8, 0, 7],
        [0, 0, 0, 0, 0, 0, 2, 0, 0]
    ]

    unsolveableBoard = [
        [0, 0, 0, 0, 0, 0, 2, 0, 1],
        [0, 9, 0, 0, 5, 0, 8, 6, 0],
        [6, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 2],
        [7, 0, 0, 0, 6, 0, 9, 8, 0],
        [0, 0, 6, 0, 9, 0, 7, 5, 0],
        [8, 5, 0, 4, 0, 0, 0, 0, 0],
        [9, 7, 0, 5, 0, 0, 0, 0, 0]
    ]

    startTime = time.time()

    if solveSudoku(unsolveableBoard):
        endTime = time.time()
        printBoard(unsolveableBoard)

    print("Finished in: " + str(round(endTime - startTime, 3)) + " secounds")
    print("It took " + str(iterations) + " iterations to finish the job")

iterations = 0
main()
