# A premade board taken from https://www.sudoku-online.org/ (Tuesday April the 5th, 2022)
board = [
    [0,8,0,0,0,6,4,0,0],
    [1,0,0,0,0,8,9,7,0],
    [0,0,0,0,3,0,0,0,5],
    [0,0,4,5,8,0,7,6,0],
    [0,0,7,0,0,0,0,4,8],
    [8,6,5,0,0,0,0,2,9],
    [0,3,0,0,0,0,0,0,7],
    [5,0,0,6,0,0,2,0,4],
    [2,7,0,0,0,0,6,9,3]
]

# The solution to the premade board from above
solved_board = [
    [7,8,9,1,5,6,4,3,2],
    [1,5,3,4,2,8,9,7,6],
    [6,4,2,9,3,7,1,8,5],
    [3,2,4,5,8,9,7,6,1],
    [9,1,7,3,6,2,5,4,8],
    [8,6,5,7,1,4,3,2,9],
    [4,3,6,2,9,1,8,5,7],
    [5,9,8,6,7,3,2,1,4],
    [2,7,1,8,4,5,6,9,3]
]

# An empty Sudoku board so the user can create one and let the program solve it
empty_board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]


# This function iterates through the board, printing it and also printing the separations of the areas of the game
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
        
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(str(bo[i][j]))
            else:
                print(str(bo[i][j]) + " ", end="")