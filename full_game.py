from game import check_if_correct
from solver import play_solver, find_empty
from boards import board, solved_board, empty_board, print_board


# This function plays the traditional Sudoku game, where there's a premade board and the user has to solve it
def play_game(bo, solved_bo):
    print_board(bo)
    check_if_correct(bo, solved_bo)
    find = find_empty(bo)
    if not find:
        print("Congratulations! You completed the Sudoku\n")
        return True
        
    else:
        play_game(bo, solved_bo)


# This function asks the user which mode of Sudoku they want to play
def choose_mode():
    mode = int(input("Enter \'1\' to play traditional Sudoku or enter \'2\' to enter a board and let the program solve it: "))
    if mode == 1 or mode == 2:
        return mode
    else:
        choose_mode()


# This function plays the full game, where the user can choose which mode to play and then the game is displayed
def full_game():
    bo = []
    print("\n")
    print("Welcome to my sudoku game, hope you enjoy it!\n")
    mode = choose_mode()
    if mode == 1:
        bo = board
        print("Welcome to Sudoku game!\n")
        solved_bo = solved_board
        play_game(bo, solved_bo)
    elif mode == 2:
        bo = empty_board
        print("Welcome to Sudoku solver!\n")
        print_board(bo)
        play_solver(bo)

full_game()