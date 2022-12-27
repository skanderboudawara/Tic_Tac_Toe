# Tic Tac Toe
from data.src.game import Game, ScoreBoard
import data.src.const as C
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
        system("clear")
    except Exception:
        system("cls")


def launch_game():
    """
    The main game

    :param: None

    :returns: None
    """
    clear_sys()
    print(C.MENU_SCREEN)
    score_board_printed = False
    get_input = True
    while get_input:
        nb_players = input("Select 0, 1, 2, 3 or 4: ")
        if nb_players.lower() == "0":
            quit()
        elif nb_players.lower() == "4":
            if not score_board_printed:
                sc_board.print_score()
                score_board_printed = True
        get_input = nb_players.lower() not in ["0", "1", "2", "3"]
    game = Game(int(nb_players))
    game.start_game()
    if (game.is_winner.startswith("PLAYER")) and sc_board.is_best_score(game.score):
        username = input("Type your username to register your score: ")
        sc_board.add_score(username, game.score)
        sc_board.print_score()


if __name__ == "__main__":
    sc_board = ScoreBoard()
    start = True
    while start:
        launch_game()
        get_input = True
        while get_input:
            restart_over = input("Try again? (y/n): ")
            get_input = not (restart_over.upper().startswith(("Y", "N")))
        if restart_over.upper() == "N":
            quit()
