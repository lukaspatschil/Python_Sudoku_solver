#solver.py
import time
import boards

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
    startTime = time.time()

    if solveSudoku(boards.unsolveableBoard):
        endTime = time.time()
        printBoard(boards.unsolveableBoard)

    print("Finished in: " + str(round(endTime - startTime, 3)) + " secounds")
    print("It took " + str(iterations) + " iterations to finish the job")

iterations = 0
main()
