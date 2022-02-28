from game import play_game
from solver import solve
from boards import board, solved_board, empty_board

def choose_mode():
    mode = int(input("Enter \'1\' to play Sudoku with a premade board or enter \'2\' to solve a board: "))
    if mode == 1 or mode == 2:
        return mode
    else:
        choose_mode()

def full_game():
    bo = []
    print("Welcome to my sudoku game, hope you enjoy it!\n")
    mode = choose_mode()
    if mode == 1:
        bo = board
        solved_bo = solved_board
        play_game(bo, solved_bo)