from data.src.game import ScoreBoard, Game
import data.src.const as C
import pytest
import json


def test_printing_high_score(capfd):
    ScoreB = ScoreBoard()
    ScoreB.score_board = {
        '100': 'SKA',
    }

    ScoreB.print_score()
    out, err = capfd.readouterr()

    scoreboard_to_print = '''
==========================================
            🎖️ Score Board 🎖️
==========================================
    RANK    |   USERNAME    |   SCORE

    #🥇            SKA          100
    #🥈                            
    #🥉                            
    #4                             
    #5                             


'''
    assert out == scoreboard_to_print


def test_add_score_board():
    sc_board = ScoreBoard()
    sc_board.add_score('skander', 200)
    assert sc_board.score_board == {'200': 'SKA'}, "Error"
    with open(C.PATH_SCORE_BOARD, 'r+') as f:
        assert {'200': 'SKA'} == json.load(f)

    with pytest.raises(AssertionError, match='^Wrong Type:'):
        sc_board.add_score(5, 200)
    with pytest.raises(AssertionError, match='^Wrong Type:'):
        sc_board.add_score('skander', 'A')


def test_is_best_score():
    sc_board = ScoreBoard()
    sc_board.score_board = {}
    assert sc_board.is_best_score(100)

    with pytest.raises(AssertionError, match='^Wrong Type:'):
        sc_board.add_score('skander', 'A')
    sc_board.score_board = {
        '100': 'SKA',
        '200': 'SKA',
        '300': 'SKA',
        '400': 'SKA',
        '500': 'SKA',
    }

    assert sc_board.is_best_score(50) == '100'
    assert not sc_board.is_best_score(600)


def test_init_choices():
    TicTacToe = Game(2)
    assert TicTacToe.choices == ['A1', 'A2',
                                 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']


def test_init_board_dict():
    TicTacToe = Game(2)
    expected_dict = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '🔲', '🔲', '🔲'],
        'B': ['B', '🔲', '🔲', '🔲'],
        'C': ['C', '🔲', '🔲', '🔲'],
    }

    assert expected_dict == TicTacToe.board


def test_evaluate_winner():
    TicTacToe = Game(1)
    TicTacToe.bot = '❌'
    TicTacToe.player1 = '⭕️'
    TicTacToe.board = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '🔲', '🔲', '🔲'],
        'B': ['B', '🔲', '🔲', '🔲'],
        'C': ['C', '🔲', '🔲', '🔲'],
    }

    assert not TicTacToe.evaluate_winner()

    TicTacToe.board = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '⭕️', '🔲', '🔲'],
        'B': ['B', '🔲', '🔲', '⭕️'],
        'C': ['C', '🔲', '🔲', '🔲'],
    }

    assert not TicTacToe.evaluate_winner()

    TicTacToe.board = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '❌', '❌', '❌'],
        'B': ['B', '🔲', '🔲', '🔲'],
        'C': ['C', '🔲', '🔲', '🔲'],
    }

    assert TicTacToe.evaluate_winner()
    assert TicTacToe.is_winner == 'BOT'

    TicTacToe.board = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '❌', '🔲', '🔲'],
        'B': ['B', '❌', '🔲', '🔲'],
        'C': ['C', '❌', '🔲', '🔲'],
    }

    assert TicTacToe.evaluate_winner()
    assert TicTacToe.is_winner == 'BOT'

    TicTacToe.board = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '🔲', '🔲', '❌'],
        'B': ['B', '🔲', '❌', '🔲'],
        'C': ['C', '❌', '🔲', '🔲'],
    }

    assert TicTacToe.evaluate_winner()
    assert TicTacToe.is_winner == 'BOT'

    TicTacToe.board = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '❌', '🔲', '🔲'],
        'B': ['B', '🔲', '❌', '🔲'],
        'C': ['C', '🔲', '🔲', '❌'],
    }

    assert TicTacToe.evaluate_winner()
    assert TicTacToe.is_winner == 'BOT'

    TicTacToe.board = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '⭕️', '🔲', '🔲'],
        'B': ['B', '🔲', '⭕️', '🔲'],
        'C': ['C', '🔲', '🔲', '⭕️'],
    }

    assert TicTacToe.evaluate_winner()
    assert TicTacToe.is_winner == 'PLAYER 1'

    TicTacToe = Game(2)
    TicTacToe.player2 = '❌'
    TicTacToe.player1 = '⭕️'

    TicTacToe.board = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '⭕️', '🔲', '🔲'],
        'B': ['B', '🔲', '⭕️', '🔲'],
        'C': ['C', '🔲', '🔲', '⭕️'],
    }

    assert TicTacToe.evaluate_winner()
    assert TicTacToe.is_winner == 'PLAYER 1'

    TicTacToe.board = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '❌', '🔲', '🔲'],
        'B': ['B', '🔲', '❌', '🔲'],
        'C': ['C', '🔲', '🔲', '❌'],
    }

    assert TicTacToe.evaluate_winner()
    assert TicTacToe.is_winner == 'PLAYER 2'


def test_evaluate_end_game():

    TicTacToe = Game(2)

    TicTacToe.board = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '🔲', '🔲', '🔲'],
        'B': ['B', '🔲', '🔲', '🔲'],
        'C': ['C', '🔲', '🔲', '🔲'],
    }

    assert not TicTacToe.evaluate_end_game()

    TicTacToe.board = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '⭕️', '🔲', '⭕️'],
        'B': ['B', '🔲', '🔲', '🔲'],
        'C': ['C', '🔲', '🔲', '🔲'],
    }

    assert not TicTacToe.evaluate_end_game()

    TicTacToe.board = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '⭕️', '❌', '⭕️'],
        'B': ['B', '❌', '⭕️', '❌'],
        'C': ['C', '❌', '⭕️', '❌'],
    }

    assert TicTacToe.evaluate_end_game()


def test_execute_update():

    TicTacToe = Game(2)
    TicTacToe.choices = ['A1', 'A2', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

    with pytest.raises(AssertionError, match='^Wrong Type:'):
        TicTacToe.execute_update(5, '❌')
    with pytest.raises(AssertionError, match='^Wrong Type:'):
        TicTacToe.execute_update('A1', 5)
    with pytest.raises(AssertionError, match='^Wrong Value:'):
        TicTacToe.execute_update('A3', '❌')
    with pytest.raises(AssertionError, match='^Wrong Value:'):
        TicTacToe.execute_update('A1', '5')

    TicTacToe.board = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '🔲', '🔲', '⭕️'],
        'B': ['B', '🔲', '🔲', '🔲'],
        'C': ['C', '🔲', '🔲', '🔲'],
    }

    expected_board = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '🔲', '🔲', '⭕️'],
        'B': ['B', '🔲', '❌', '🔲'],
        'C': ['C', '🔲', '🔲', '🔲'],
    }

    TicTacToe.execute_update('B2', '❌')

    assert TicTacToe.choices == ['A1', 'A2', 'B1', 'B3', 'C1', 'C2', 'C3']
    assert TicTacToe.board == expected_board

    TicTacToe.bot = '❌'
    TicTacToe.user = '⭕️'
    assert TicTacToe.execute_update('B3', '❌') == (False, False)


def test_update_board_dict():

    TicTacToe = Game(2)
    TicTacToe.choices = ['A1', 'A2', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

    with pytest.raises(AssertionError, match='^Wrong Type:'):
        TicTacToe.update_board_dict(5, '❌')
    with pytest.raises(AssertionError, match='^Wrong Type:'):
        TicTacToe.update_board_dict('A1', 5)
    with pytest.raises(AssertionError, match='^Wrong Value:'):
        TicTacToe.update_board_dict('A1', '5')

    TicTacToe.board = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '🔲', '🔲', '⭕️'],
        'B': ['B', '🔲', '🔲', '🔲'],
        'C': ['C', '🔲', '🔲', '🔲'],
    }

    expected_board = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '🔲', '🔲', '⭕️'],
        'B': ['B', '🔲', '❌', '🔲'],
        'C': ['C', '🔲', '🔲', '🔲'],
    }

    TicTacToe.update_board_dict('B2', '❌')

    assert TicTacToe.board == expected_board


def test_printing_board(capfd):
    TicTacToe = Game(1)
    TicTacToe.current = 'PLAYER 1'

    TicTacToe.draw_board()
    out, err = capfd.readouterr()

    board_to_print = '''

      ————————————————————
      |   | 1  |  2 |  3 |
      ————————————————————
      | A | 🔲 | 🔲 | 🔲 |
      ————————————————————
      | B | 🔲 | 🔲 | 🔲 |
      ————————————————————
      | C | 🔲 | 🔲 | 🔲 |
      ————————————————————

'''
    assert out == board_to_print

    TicTacToe.board = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '❌', '🔲', '🔲'],
        'B': ['B', '🔲', '🔲', '🔲'],
        'C': ['C', '🔲', '🔲', '🔲'],
    }
    TicTacToe.step = 19
    TicTacToe.current = 'BOT'
    TicTacToe.draw_board()
    out, err = capfd.readouterr()

    board_to_print = '''

      ————————————————————
      |   | 1  |  2 |  3 |
      ————————————————————
      | A | ❌ | 🔲 | 🔲 |
      ————————————————————
      | B | 🔲 | 🔲 | 🔲 |
      ————————————————————
      | C | 🔲 | 🔲 | 🔲 |
      ————————————————————

'''
    assert out == board_to_print
