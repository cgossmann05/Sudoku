from solver import print_board, find_empty

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
solved_board = [
    [7,8,5,4,3,9,1,2,6],
    [6,1,2,8,7,5,3,4,9],
    [4,9,3,6,2,1,5,7,8],
    [8,5,7,9,4,3,2,6,1],
    [2,6,1,7,5,8,9,3,4],
    [9,3,4,1,6,2,7,8,5],
    [5,7,8,3,9,4,6,1,2],
    [1,2,6,5,8,7,4,9,3],
    [3,4,9,2,1,6,8,5,7]
]

def choose_col(bo):
    col = int(input("\nPlease enter the number of the column, from 1 to 9, from left to right: "))
    if col < 1 or col > 9:
        choose_col(bo)
    else:
        col -= 1
        return col

def choose_row(bo):
    row = int(input("\nPlease enter the number of the row, from 1 to 9, from up to down: "))
    if row < 1 or row > 9 :
        choose_row(bo)
    else:
        row -= 1
        return row

def choose_val(bo):
    val = int(input("\nPlease enter the value you want to enter: "))
    if val < 1 or val > 9:
        choose_val(bo)
    else:
        return val

def define_pos_and_val(bo):
    col = choose_col(bo)
    row = choose_row(bo)
    val = choose_val(bo)
    if bo[row][col] == 0:
        return [col, row, val]
    else:
        print("\nThis box already has an answer.")
        define_pos_and_val(bo)

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
        print_board(board)
        check_if_correct(bo, solved_bo)

def play_game(bo, solved_bo):
    print_board(bo)
    check_if_correct(bo, solved_bo)
    find = find_empty(bo)
    if not find:
        print("Congratulations! You completed the Sudoku")
        return True
        
    else:
        play_game(bo, solved_bo)

play_game(board, solved_board)