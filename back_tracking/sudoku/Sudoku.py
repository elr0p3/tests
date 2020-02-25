import re

class Sudoku:
    def __init__(self, grid : list, name=None):
        self.name = name
        self.grid = grid

    def show(self):
        print('\n', self.name, ": Solved" if not self.isFull(self.grid) else ": Not Solved", sep='')
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                print(self.grid[i][j], ' ', end='')
                if (j+1) % 3 == 0:
                    print("  ", end='')
            print()
            if (i+1) % 3 == 0:
                print()
        print()

    def solve(self):
        positions = self.isFull(self.grid)
        if not positions:
            return True
        else:
            x, y = positions
        
        for i in range(1, 10):
            if self.validNumber(i, x, y):
                self.grid[x][y] = i
                if self.solve():
                    return True
                self.grid[x][y] = 0

        return False

    def isFull(self, grid : list):
        for g in grid:
            if 0 in g:
                return (grid.index(g), g.index(0))
        return None

    def validNumber(self, val : int, x : int, y : int):
        # Check line
        if val in self.grid[x]:
            return False

        # Check column
        for i in range(len(self.grid)):
            if val == self.grid[i][y]:
                return False

        # Check Box
        section_y = y // 3  # Let get the box in which we are situated
        section_x = x // 3
        for i in range(section_x * 3, section_x * 3 + 3):
            for j in range(section_y * 3, section_y * 3 + 3):
                if self.grid[i][j] == val:
                    return False

        return True

    @classmethod
    def constructor(cls, filename : str):
        with open("./problems/" + filename) as f:
            name = re.sub(r"(Name:|\n)", '', f.readline(), flags=re.IGNORECASE)
            sdku = f.readlines()
            sudoku = []
            for s in sdku:
                line = re.findall(r"[0-9]", s)
                if line:
                    sudoku.append(list(map(int, line)))
            return cls(sudoku, name)
