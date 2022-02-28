
from boards import print_board
from game import choose_col, choose_row, choose_val


def play_solver(bo):
    print("Welcome to Sudoku solver!\n")
    print_board(bo)



def choose_pos(bo):
    col = choose_col(bo)
    row = choose_row(bo)
    val = choose_val(bo)
    return [col, row, val]



def solve(bo):

    find = find_empty(bo)
    if not find:
        return True
    else:
        row, column = find
    
    for i in range(1, 10):
        if valid(bo, i, (row, column)):
            bo[row][column] = i

            if solve(bo):
                return True
            
            bo[row][column] = 0
    
    return False



def valid(bo, num, pos):
    
    #check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    
    #check columns
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    
    #check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    
    return True


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # row, column
    
    return None
