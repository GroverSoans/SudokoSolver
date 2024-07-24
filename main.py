def isValidMove(grid, row, col , num):
    #Check if num is already in row
    for x in range(9):
        if grid[row][x] == num:
            return False
    #Check if num is already in col
    for x in range(9):
        if grid[x][col] == num:
            return False
        
    cornerRow = row - row % 3
    cornerCol = col - col % 3

    #Check if num is already in 3x3 grid
    for x in range(3):
        for y in range(3):
            if grid[cornerRow + x][cornerCol + y] == num:
                return False
            
    return True


def solve(grid, row, col):

    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve(grid, row, col + 1)
    
    for num in range (1, 10):

        if isValidMove(grid, row, col, num):
            grid[row][col] = num
            if solve(grid, row, col +1):
                return True
            
        grid[row][col] = 0

    return False

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

#Prints solution if there is one
if solve(grid, 0, 0):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
else:
    print("No solution for this Sudoko")