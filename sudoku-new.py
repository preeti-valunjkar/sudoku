# This is a code for solving a given input for a sudoku game. It has been created using backtracking algorithm
# The sudoku digits are between 1-9 and 0 is considered an empty box in the grid


# Helper function 1
# Function is_Valid checks if the particular number is a valid number at position pos
# Returns True or False
def is_Valid(grid, num, pos):
    # Checking condition 1-
    # Check in rows
    for i in range(9):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    # Checking condition 2-
    # Check in columns
    for i in range(9):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # Checking condition 3-
    # Check in square containing pos
    square_row = (pos[0] // 3) * 3
    square_col = (pos[1] // 3) * 3

    for i in range(square_row, square_row + 3):
        for j in range(square_col, square_col + 3):
            if grid[i][j] == num and (i,j) != pos:
                return False

    return True


# Helper function 2
# Function find_next_empty finds the next position which contains a 0 (i.e, is empty)
# Returns the position where element stored is 0, else returns False
def find_next_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)  # row, col

    return None


# Main Function
# Function solve_sudoku_grid solves the given sudoku grid
# Returns either True (if the grid is solvable) or False (if the grid is unsolvable)
# Mutation to grid values
def solve_sudoku_grid(grid):
    find = find_next_empty(grid)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if is_Valid(grid, i, (row, col)):
            grid[row][col] = i

            if solve_sudoku_grid(grid):
                return True
            # Condition for backtracking
            grid[row][col] = 0

    return False


# Print Function
# Function print_board prints the given solved sudoku grid
# Prints to standard output
def print_board(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")


# Input Function
# Inputs values from the grid row-wise
# To properly input values, follow the following rules:
#   1. Enter each digit in a row with a space
#   2. Enter each subsequent row with a newline
# The input is designed such that it will take in exactly 9 rows from user but care needs to be takes for 9 columns
board=[]
for i in range(0,9):
    board.append([int(j) for j in input().split()])



print_board(board)
solve_sudoku_grid(board)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print_board(board)
