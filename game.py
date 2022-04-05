from boards import print_board


# This function asks the user to choose the column of the table to input a value
def choose_col(bo):
    col = int(input("\nPlease enter the number of the column, from 1 to 9, from left to right: "))
    if col < 1 or col > 9:
        choose_col(bo)
    else:
        col -= 1
        return col


# This function asks the user to choose the row of the table to input a value
def choose_row(bo):
    row = int(input("\nPlease enter the number of the row, from 1 to 9, from top to bottom: "))
    if row < 1 or row > 9 :
        choose_row(bo)
    else:
        row -= 1
        return row


# This function asks the user which value they want to enter
def choose_val(bo):
    val = int(input("\nPlease enter the value you want to enter: "))
    if val < 1 or val > 9:
        choose_val(bo)
    else:
        return val


# This function asks the column, row, and value the user wants to enter, and then checks if the position already has a value
def define_pos_and_val(bo):
    col = choose_col(bo)
    row = choose_row(bo)
    val = choose_val(bo)
    if bo[row][col] == 0:
        return [col, row, val]
    else:
        print("\nThis box already has a value.")
        define_pos_and_val(bo)


# This function compares the value in the position chose by the user to the value in the same position in the solved board
def check_if_correct(bo, solved_bo):
    lst = define_pos_and_val(bo)
    col = lst[0]
    row = lst[1]
    val = lst[2]
    if val == solved_bo[row][col]:
        print("\nCorrect!\n")
        bo[row][col] = val
        return True
    else:
        print("\nNot quite, try again:\n")
        print_board(bo)
        check_if_correct(bo, solved_bo)