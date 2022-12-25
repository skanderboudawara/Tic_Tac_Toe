# Tic Tac Toe
import src.board as B


def launch_game():
    """
    The main game

    :param: None

    :returns: None
    """
    print('\n==========================================')
    print('\n  👾 Weclcome to the Tic Tac Toe Board  👾 ')
    print('\n==========================================')
    sc_board.print_score()
    get_input = True
    while get_input:
        user_choice = input('Type start to start the game: ')
        get_input = user_choice.lower() != 'start'
    TicTacBoard = B.TicTacToBoard()
    TicTacBoard.init_choices()
    TicTacBoard.init_board_dict()
    TicTacBoard.pre_start_game()
    TicTacBoard.start_game()
    TicTacBoard.close_game()
    if (TicTacBoard.is_winner == 'YOU') and sc_board.is_best_score(TicTacBoard.score):
        user_choice = input('Type your username to register your score: ')
        sc_board.add_score(user_choice, TicTacBoard.score)
        sc_board.print_score()


if __name__ == '__main__':
    sc_board = B.ScoreBoard()
    start = True
    while start:
        launch_game()
        get_input = True
        while get_input:
            user_choice = input(
                'Try again? (y/n): ')
            get_input = not (user_choice.upper().startswith(('Y', 'N')))
        print(user_choice)
        if user_choice.upper() == 'N':
            start = not start
