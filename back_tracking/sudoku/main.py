import os
from Sudoku import Sudoku

if __name__ == "__main__":

    sudokus = []
    
    try:
        for f in os.listdir("./problems"):
            sudokus.append(Sudoku.constructor(f))        
    except FileNotFoundError:
        print("ERROR! There is no directory './problems' with all the sudokus")
        raise

    for s in sudokus:
        s.show()
        s.solve()
        s.show()
        print("=-"*15)
