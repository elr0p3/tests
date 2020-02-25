import numpy as np

grid = [
    [5,3,0,  0,7,0,  0,0,0],
    [6,0,0,  1,9,5,  0,0,0],
    [0,9,8,  0,0,0,  0,6,0],
    
    [8,0,0,  0,6,0,  0,0,3],
    [4,0,0,  8,0,3,  0,0,1],
    [7,0,0,  0,2,0,  0,0,6],

    [0,6,0,  0,0,0,  2,8,0],
    [0,0,0,  4,1,9,  0,0,5],
    [0,0,0,  0,8,0,  0,7,9]
]

def solve(grid : list):
    positions = isFull(grid)
    if not positions:
        return True
    else:
        x, y = positions
    
    for i in range(1, 10):
        if validNumber(grid, i, x, y):
            grid[x][y] = i
            if solve(grid):
                return True
            grid[x][y] = 0

    return False

def isFull(grid : list):
    for g in grid:
        if 0 in g:
            return (grid.index(g), g.index(0))
    return None

def validNumber(grid : list, val : int, x : int, y : int):
    # Check line
    if val in grid[x]:
        return False

    # Check column
    for i in range(len(grid)):
        if val == grid[i][y]:
            return False

    # Check Box
    section_y = y // 3  # Let get the box in which we are situated
    section_x = x // 3
    for i in range(section_x * 3, section_x * 3 + 3):
        for j in range(section_y * 3, section_y * 3 + 3):
            if grid[i][j] == val:
                return False

    return True

if __name__ == "__main__":
    print(np.matrix(grid), '\n')
    solve(grid)
    print(np.matrix(grid))
