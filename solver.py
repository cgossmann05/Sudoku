from game import choose_col, choose_row, choose_val
from boards import print_board


# This function plays the solving mode of the game, where the user builds a table and then the program solves and prints it
def play_solver(bo):
    check_pos(bo)
    print("\n")
    print_board(bo)
    done = ask_if_finished()
    find = find_empty(bo)
    if done or not find:
        solve(bo)
        print("\nCongratulations! Here is your solved board.\n")
        print_board(bo)
        print("\n")
        return True
    else:
        play_solver(bo)


# This function asks the user if they are finished building the board to be solved by the program
def ask_if_finished():
    response = input("\nDo you want to solve the board now? Enter \"s\" to solve and \"c\" to continue building the board: ")
    if response == "s":
        return True
    elif response == "c":
        return False
    else:
        ask_if_finished()


# This function checks the position chosen, and if it's a valid position, it puts in in the board, otherwise it alerts is not a valid position
def check_pos(bo):
    row, col = choose_pos(bo)
    val = choose_val(bo)

    if valid(bo, val, [row, col]):
        bo[row][col] = val
    else:
        print("Not valid.")
        check_pos(bo)


# This function calls the functions of choosing the column and row, and returns the position
def choose_pos(bo):
    col = choose_col(bo)
    row = choose_row(bo)
    return [row, col]


# This function solves the board with regression, trying the first number possible, and if it's not possible it goes back with another number
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


# This function checks if the value entered is valid, checking if the number is already in the row, column or 3x3 box
def valid(bo, val, pos):
    
    # This checks the row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == val and pos[1] != i:
            return False
    
    # This checks the column
    for i in range(len(bo)):
        if bo[i][pos[1]] == val and pos[0] != i:
            return False
    
    # This checks the 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == val and (i, j) != pos:
                return False
    
    return True


# This function iterates through the board and returns the first empty position
def find_empty(bo):
    for row in range(len(bo)):
        for col in range(len(bo[0])):
            if bo[row][col] == 0:
                return (row, col)
    
    return None
