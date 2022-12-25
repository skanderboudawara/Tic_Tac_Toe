import board as B
import pytest


def test_add_score_board():
    sc_board = B.ScoreBoard()
    sc_board.add_score('skander', 200.0)
    assert sc_board.score_board == {'200.0': 'SKA'}, "Error"

    with pytest.raises(AssertionError, match='^Wrong Type:'):
        sc_board.add_score(5, 200.0)
    with pytest.raises(AssertionError, match='^Wrong Type:'):
        sc_board.add_score('skander', 'A')


def test_is_best_score():
    sc_board = B.ScoreBoard()
    sc_board.score_board = {}
    assert sc_board.is_best_score(100.0)

    with pytest.raises(AssertionError, match='^Wrong Type:'):
        sc_board.add_score('skander', 'A')
    sc_board.score_board = {
        '100.0': 'SKA',
        '200.0': 'SKA',
        '300.0': 'SKA',
        '400.0': 'SKA',
        '500.0': 'SKA',
    }

    assert sc_board.is_best_score(50.0) == '100.0'
    assert not sc_board.is_best_score(600.0)


def test_init_choices():
    TicTacToe = B.TicTacToBoard()
    TicTacToe.init_choices()

    assert TicTacToe.choices == ['A1', 'A2',
                                 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']


def test_init_board_dict():
    TicTacToe = B.TicTacToBoard()
    TicTacToe.init_board_dict()

    expected_dict = {
        ' ': [' ', '1', '2', '3'],
        'A': ['A', '🔲', '🔲', '🔲'],
        'B': ['B', '🔲', '🔲', '🔲'],
        'C': ['C', '🔲', '🔲', '🔲'],
    }

    assert expected_dict == TicTacToe.board


def test_evaluate_winner():
    TicTacToe = B.TicTacToBoard()
    TicTacToe.pc = '❌'
    TicTacToe.user = '⭕️'

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
    assert TicTacToe.is_winner == 'YOU'


def test_evaluate_end_game():

    TicTacToe = B.TicTacToBoard()

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

    TicTacToe = B.TicTacToBoard()
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

    TicTacToe = B.TicTacToBoard()
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
