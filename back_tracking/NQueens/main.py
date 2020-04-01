
class Table:

    def __init__(self, size : int):
        self.queen  = 1
        self.table  = []
        self.size   = size
        self.aux    = [0] * size
        for _ in range(size):
            self.table.append(self.aux.copy())


    def show(self) -> None:
        for i in range(self.size):
            for j in range(len(self.table[i])):
                print(self.table[i][j], ' ', end='')
            print()


    def isValid(self, row, col) -> bool:
        # Check the row in which we are situated
        if self.queen in self.table[row]:
            return False

        # Check all columns
        for i in range(len(self.table)):
            if self.queen == self.table[i][col]:
                return False

        # Check upper diagonal on left side 
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
            if self.table[i][j] == 1: 
                return False
  
        # Check lower diagonal on left side 
        for i, j in zip(range(row, self.size, 1), range(col, -1, -1)): 
            if self.table[i][j] == 1: 
                return False

        return True


    def setQueens(self, col = 0) -> bool:
        if col >= self.size:    # When we has arrived to the las column
            return True

        for i in range(size):
            if self.isValid(i, col):
                self.table[i][col] = self.queen
                
                if self.setQueens(col + 1):
                    return True

                self.table[i][col] = 0

        return False


if __name__ == "__main__":

    while True:
        try:
            size = int(input("Introduce the table dimetion: "))
            break
        except (ValueError, NameError):
            print("ERROR! The number inputed is not an integer")

    t = Table(size)
    t.setQueens()
    t.show()
