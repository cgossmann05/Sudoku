from game import check_if_correct
from solver import play_solver, find_empty
from boards import board, solved_board, empty_board, print_board





def play_game(bo, solved_bo):
    print("Welcome to Sudoku game!\n")
    print_board(bo)
    check_if_correct(bo, solved_bo)
    find = find_empty(bo)
    if not find:
        print("Congratulations! You completed the Sudoku")
        return True
        
    else:
        play_game(bo, solved_bo)



def choose_mode():
    mode = int(input("Enter \'1\' to play Sudoku with a premade board or enter \'2\' to solve a board: "))
    if mode == 1 or mode == 2:
        return mode
    else:
        choose_mode()

def full_game():
    bo = []
    print("\n")
    print("Welcome to my sudoku game, hope you enjoy it!\n")
    mode = choose_mode()
    if mode == 1:
        bo = board
        solved_bo = solved_board
        play_game(bo, solved_bo)
    elif mode == 2:
        bo = empty_board
        play_solver(bo)

full_game()