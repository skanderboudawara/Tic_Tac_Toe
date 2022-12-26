import board as B
import pytest


def test_add_score_board():
    sc_board = B.ScoreBoard()
    sc_board.add_score('skander', 200)
    assert sc_board.score_board == {'200': 'SKA'}, "Error"

    with pytest.raises(AssertionError, match='^Wrong Type:'):
        sc_board.add_score(5, 200)
    with pytest.raises(AssertionError, match='^Wrong Type:'):
        sc_board.add_score('skander', 'A')


def test_is_best_score():
    sc_board = B.ScoreBoard()
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
    TicTacToe = B.TicTacToBoard('2')
    TicTacToe.init_choices()

    assert TicTacToe.choices == ['A1', 'A2',
                                 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']


def test_init_board_dict():
    TicTacToe = B.TicTacToBoard('2')
    TicTacToe.init_board_dict()

    expected_dict = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '🔲', '🔲', '🔲'],
        'B': ['B', '🔲', '🔲', '🔲'],
        'C': ['C', '🔲', '🔲', '🔲'],
    }

    assert expected_dict == TicTacToe.board


def test_evaluate_winner():
    TicTacToe = B.TicTacToBoard('1')
    TicTacToe.pc = '❌'
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
    assert TicTacToe.is_winner == 'PC'

    TicTacToe.board = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '❌', '🔲', '🔲'],
        'B': ['B', '❌', '🔲', '🔲'],
        'C': ['C', '❌', '🔲', '🔲'],
    }

    assert TicTacToe.evaluate_winner()
    assert TicTacToe.is_winner == 'PC'

    TicTacToe.board = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '🔲', '🔲', '❌'],
        'B': ['B', '🔲', '❌', '🔲'],
        'C': ['C', '❌', '🔲', '🔲'],
    }

    assert TicTacToe.evaluate_winner()
    assert TicTacToe.is_winner == 'PC'

    TicTacToe.board = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '❌', '🔲', '🔲'],
        'B': ['B', '🔲', '❌', '🔲'],
        'C': ['C', '🔲', '🔲', '❌'],
    }

    assert TicTacToe.evaluate_winner()
    assert TicTacToe.is_winner == 'PC'

    TicTacToe.board = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '⭕️', '🔲', '🔲'],
        'B': ['B', '🔲', '⭕️', '🔲'],
        'C': ['C', '🔲', '🔲', '⭕️'],
    }

    assert TicTacToe.evaluate_winner()
    assert TicTacToe.is_winner == 'PLAYER 1'

    TicTacToe = B.TicTacToBoard('2')
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

    TicTacToe = B.TicTacToBoard('2')

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

    TicTacToe = B.TicTacToBoard('2')
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

    TicTacToe.pc = '❌'
    TicTacToe.user = '⭕️'
    assert TicTacToe.execute_update('B3', '❌') == (False, False)


def test_update_board_dict():

    TicTacToe = B.TicTacToBoard('2')
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
    TicTacToe = B.TicTacToBoard('2')
    TicTacToe.init_board_dict()

    expected_dict = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '🔲', '🔲', '🔲'],
        'B': ['B', '🔲', '🔲', '🔲'],
        'C': ['C', '🔲', '🔲', '🔲'],
    }

    TicTacToe.draw_board()
    out, err = capfd.readouterr()
    assert out == "   1  2  3\n\nA  🔲  🔲  🔲\n\nB  🔲  🔲  🔲\n\nC  🔲  🔲  🔲\n\n"

    TicTacToe.board = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '❌', '🔲', '🔲'],
        'B': ['B', '🔲', '🔲', '🔲'],
        'C': ['C', '🔲', '🔲', '🔲'],
    }

    TicTacToe.draw_board()
    out, err = capfd.readouterr()
    assert out == "   1  2  3\n\nA  ❌  🔲  🔲\n\nB  🔲  🔲  🔲\n\nC  🔲  🔲  🔲\n\n"


def test_printing_high_score(capfd):
    ScoreB = B.ScoreBoard()
    ScoreB.score_board = {
        '100': 'SKA',
    }

    ScoreB.print_score()
    out, err = capfd.readouterr()
    assert out == "\nRANK     USERNAME     SCORE\n\n#1         SKA        100\n\n"
