from game import choose_col, choose_row, choose_val
from boards import print_board



def play_solver(bo):
    print("Welcome to Sudoku solver!\n")
    print_board(bo)
    check_pos(bo)
    print("\n")
    done = ask_if_finished()
    find = find_empty(bo)
    if done or not find:
        solve(bo)
        print("Congratulations! Here is your solved board.\n")
        print_board(bo)
        print("\n")
        return True
    else:
        play_solver(bo)



def ask_if_finished():
    response = input("Do you want to solve the board now? Enter \"y\" for yes and \"c\" to continue building the board.\n")
    if response == "y":
        return True
    elif response == "c":
        return False
    else:
        ask_if_finished()



def check_pos(bo):
    row, col = choose_pos(bo)
    val = choose_val(bo)

    if valid(bo, val, [row, col]):
        bo[row][col] = val
    else:
        print("Not valid.")
        check_pos(bo)



def choose_pos(bo):
    col = choose_col(bo)
    row = choose_row(bo)
    return [row, col]



def solve(bo):

    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True
            
            bo[row][col] = 0
    
    return False



def valid(bo, val, pos):
    
    #check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == val and pos[1] != i:
            return False
    
    #check columns
    for i in range(len(bo)):
        if bo[i][pos[1]] == val and pos[0] != i:
            return False
    
    #check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == val and (i, j) != pos:
                return False
    
    return True


def find_empty(bo):
    for row in range(len(bo)):
        for col in range(len(bo[0])):
            if bo[row][col] == 0:
                return (row, col)
    
    return None
