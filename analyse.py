import boards
import solver
import time

def main():
    file = open("data.out", 'w')
    testCases = []

    for i in range(1000):
        startTime = time.time()
        if solver.solveSudoku(boards.board953.copy()):
            endTime = time.time()
        
        file.write(str(solver.iterations) + ";" + str(endTime - startTime) + '\n')

        file.flush()

    file.close()

main() 
print("Done!")