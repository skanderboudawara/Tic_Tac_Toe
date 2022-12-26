# Tic Tac Toe
import src.board as B
import src.const as C
from os import system

def clear_sys():
    """
    To clear the system
    'clear' for MacOs, Linux
    'cls' for Windows

    :param: None

    :returns: None
    """
    try:
        system('clear')
    except Exception:
        system('cls')

def launch_game():
    """
    The main game

    :param: None

    :returns: None
    """
    clear_sys()
    print(C.MENU_SCREEN)
    printed = False
    get_input = True
    while get_input:
        nb_players = input('Select 0, 1, 2 or 3: ')
        if nb_players.lower() == '0':
            exit
        elif nb_players.lower() == '3':
            if not printed:
                sc_board.print_score()
                printed = True
        get_input = nb_players.lower() not in ['0', '1', '2']
    TicTacBoard = B.TicTacToBoard(nb_players)
    TicTacBoard.init_choices()
    TicTacBoard.init_board_dict()
    TicTacBoard.pre_start_game()
    TicTacBoard.start_game()
    TicTacBoard.close_game()
    if (TicTacBoard.is_winner.startswith('PLAYER')) and sc_board.is_best_score(TicTacBoard.score):
        username = input('Type your username to register your score: ')
        sc_board.add_score(username, TicTacBoard.score)
        sc_board.print_score()


if __name__ == '__main__':
    sc_board = B.ScoreBoard()
    start = True
    while start:
        launch_game()
        get_input = True
        while get_input:
            restart_over = input(
                'Try again? (y/n): ')
            get_input = not (restart_over.upper().startswith(('Y', 'N')))
        if restart_over.upper() == 'N':
            start = not start
