import boards
import solver
import time

def main():
    file = open("data.out", 'w')

    for i in range(1000):
        newBoard = boards.board.copy()
        startTime = time.time()
        if solver.solveSudoku(newBoard):
            endTime = time.time()
        
        file.write(str(solver.iterations) + ";" + str(round(endTime - startTime, 3)) + '\n')

    file.close()

main()
    