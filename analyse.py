import boards
import solver
import time

def main():
    file = open("data.out", 'w')

    for i in range(1000):
        startTime = time.time()
        if solver.solveSudoku(boards.board.copy()):
            endTime = time.time()
        
        file.write(str(solver.iterations) + ";" + str(round(endTime - startTime, 3)) + '\n')

    file.close()

main()
    