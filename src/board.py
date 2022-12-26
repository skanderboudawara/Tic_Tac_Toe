
from random import choice as random_choice
from os import system
from time import time
import src.const as C
import re

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


class ScoreBoard():
    """
    Class to Manage the score board
    """

    def __init__(self):
        self.score_board = {}

    def add_score(self, user_name, score):
        """
        Will add the lowest score to the board

        :param user_name: (str), the user name
        :param score: (float), the score he marked

        :returns: None
        """
        assert isinstance(
            user_name, str), 'Wrong Type: User name must be a string'
        assert isinstance(score, int), 'Wrong Type: score must be a integer'

        eval_score = self.is_best_score(score)
        if eval_score and isinstance(eval_score, bool):
            self.score_board[str(score)] = (user_name.upper())[:3]
        elif isinstance(eval_score, str):
            self.score_board.remove(self.is_high_score(score))
            self.score_board[score] = (user_name.upper())[:3]

    def is_best_score(self, score):
        """
        Will check if the score marked is the lowest score saved

        :param score: (float), the score to evaluate

        :returns: (bool or str), True or str if it's a good score else False
        """
        assert isinstance(score, int), 'Wrong Type: score must be a integer'

        if self.score_board == {} or len(self.score_board.keys()) < 5:
            return True
        scores = [int(key) for key in self.score_board.keys()]
        scores.sort()
        return next((str(key) for key in scores if score < int(key)), False)

    def print_score(self):
        """
        To print all the top 5 scores

        :param: None

        :returns: None
        """
        if self.score_board == {}:
            score_board = C.SCORE_BOARD
        else:
            scores = [int(key) for key in self.score_board.keys()]
            scores.sort()
            score_board = C.SCORE_BOARD
            for index, score in enumerate(scores):
                print(index+1)
                score_board = (
                    score_board
                    .replace(f'AAA{str(index+1)}', self.score_board[str(score)])
                    .replace(f'SCORE{str(index+1)}', str(score))
                )
        score_board = re.sub("(AAA|SCORE)[1-5]", "   ", score_board)
        print(score_board)


class TicTacToBoard():
    """
    Class to manage the full game
    """

    def __init__(self, nb_players):

        assert isinstance(nb_players, str), "nb_players must be a string"

        self.cols = ['1', '2', '3']
        self.rows = ['A', 'B', 'C']
        self.pc = None
        self.nb_players = int(nb_players)
        self.is_winner = None
        self.player1 = None
        self.player2 = None
        self.state = False
        self.current = None
        self.step = 1
        self.score = 0

    def init_choices(self):
        """
        To init the necessary choices ['A1', 'A2', 'A3' ....]

        :param: None

        :returns: None
        """
        self.choices = []
        for row in self.rows:
            self.choices.extend(row+col for col in self.cols)

    def init_board_dict(self):
        """
        To init the dict board
            {
                ' ': [' ', '1', '2', '3'],
                'A': ['A', '🔲', '🔲', '🔲'],
                'B': ['B', '🔲', '🔲', '🔲'],
                'C': ['C', '🔲', '🔲', '🔲'],
            }

        :param: None

        :returns: None
        """
        self.board = {
            row: [row, *(['🔲'] * 3)]
            for row in (self.rows)
        }
        self.board[' '] = [' ', *self.cols]

    def draw_board(self):
        """
        to print the dict board

        :param: None

        :returns: None
        """
        clear_sys()
        board = C.BOARD
        for row in self.rows:
            for col in self.cols:
                board = board.replace(f'{row}{col}', self.board.get(row)[int(col)])
        board = re.sub("[A-C][1-3]", "🔲", board)
        print(board)

    def evaluate_winner(self):
        """
        A function that will evaluate if there is a winner and who is it

        :param: None

        :returns: (bool), True if there is a winner else False
        """
        wining_pc = [self.pc]*3
        wining_player1 = [self.player1]*3
        wining_player2 = [self.player2]*3
        diagonal_wining_1 = [
            self.board[row][int(col)] for col, row in zip(self.cols, self.rows)]
        diagonal_wining_2 = [self.board[row][int(col)] for col, row in zip(
            self.cols[::-1], self.rows)]
        horizontal_wining = [
            [self.board[row][int(col)] for row in self.rows] for col in self.cols]
        vertical_wining = [
            [self.board[row][int(col)] for col in self.cols] for row in self.rows]

        for value in [*horizontal_wining, *vertical_wining, diagonal_wining_1, diagonal_wining_2]:
            value = value if len(value) == 3 else value[1:]
            if value == wining_pc:
                self.is_winner = 'PC'
                break
            elif value == wining_player1:
                self.is_winner = 'PLAYER 1'
                break
            elif value == wining_player2:
                self.is_winner = 'PLAYER 2'
                break
        else:
            return False

        return True

    def evaluate_end_game(self):
        """
        Evaluate if the game has ended

        :param: None

        :returns: (bool), True all cases are filled, else false
        """
        res1 = [len([i for i in self.board[row] if i not in ['🔲', *self.rows]])
                for row in self.rows]
        return res1 == [3]*3

    def get_user_choice(self, user):
        """
        Will get the user input

        :param: None

        :returns: (tuple(bool)), evaluation of Winner and game finished
        """
        start = time()
        get_input = True
        print(
            C.SELECT_CHOICE
            .replace('PLAYER', self.current)
            .replace('TICTOE', user)
            .replace('ALL_CHOICE', ", ".join(self.choices))
        )
        while get_input:
            user_choice = input('Your choice: ')
            get_input = user_choice not in self.choices
        end = time() - start
        self.score = int(round(self.step * (self.score + end), 0))
        return self.execute_update(user_choice, user)

    def get_pc_choice(self):
        """
        Will randomly select a value

        :param: None

        :returns: (tuple(bool)), evaluation of Winner and game finished
        """
        pc_choice = random_choice(self.choices)
        return self.execute_update(pc_choice, self.pc)

    def execute_update(self, choice, who):
        """
        To execute the update Board and the update remaining choices
        + Evaluate the winner / game session

        :param choice: (str), the choice that has been made by user or computer
        :param who: (str), who made the choice '❌' or '⭕️'

        :returns: (tuple(bool)), evaluation of winner and end game
        """
        assert isinstance(choice, str), "Wrong Type: choice must be a string"
        assert isinstance(who, str), "Wrong Type: who must be a string"
        assert choice in self.choices, f"Wrong Value: choice must be in {', '.join(self.choices)}"
        assert who in ['❌', '⭕️'], "Wrong Value: who must be in ['❌', '⭕️']"

        self.choices.remove(choice)
        self.update_board_dict(choice, who)
        self.draw_board()
        return (self.evaluate_winner(), self.evaluate_end_game())

    def update_board_dict(self, choice, who):
        """
        To update the dict board with the adequate choice

        :param choice: (str), the choice that has been made by user or computer
        :param who: (str), who made the choice '❌' or '⭕️'

        :returns: None
        """
        assert isinstance(who, str), "Wrong Type: who must be a string"
        assert isinstance(choice, str), "Wrong Type: choice must be a string"
        assert who in ['❌', '⭕️'], "Wrong Value: who must be in ['❌', '⭕️']"

        previous_row = self.board[choice[0]]
        previous_row[int(choice[1])] = who
        self.board[choice[0]] = previous_row

    def get_player_input(self):
        """ 
        To get user input and convert it

        :param: None

        :returns: (str), the selected choice converted to ❌ or ⭕️
        """
        get_input = True
        while get_input:
            tic_or_toe = input(
                f'{self.current}, please select between "X", "O": ')
            get_input = tic_or_toe.upper() not in ['X', 'O']
        tic_or_toe = '❌' if tic_or_toe.upper() == 'X' else '⭕️'
        return tic_or_toe

    def get_remaining_tic_or_toe(self, choice):
        """
        if X is selected return O and vice versa

        :param choice: (str), X or O

        :return: (str), the remaining choice
        """
        return '❌' if choice == '⭕️' else '⭕️'

    def get_player1_info(self):
        """
        To get player 1 choice

        :param: None

        :returns: the remaining choice
        """
        self.current = 'PLAYER 1'
        self.player1 = self.get_player_input()
        return self.get_remaining_tic_or_toe(self.player1)

    def pre_start_game(self):
        """
        Will init the game to select who start and to select a Tic or a Tac

        :param: None

        :returns: None
        """
        if self.nb_players == 1:
            if random_choice(['PC', 'PLAYER 1']) == 'PC':
                self.pc = random_choice(['❌', '⭕️'])
                self.player1 = self.get_remaining_tic_or_toe(self.pc)
                self.current = 'PC'
            else:
                self.pc = self.get_player1_info()
        elif random_choice(['PLAYER 1', 'PLAYER 2']) == 'PLAYER 1':
            print('\nPLAYER 1 You will go first\n')
            self.player2 = self.get_player1_info()
        else:
            print('\nPLAYER 2 You will go first\n')
            self.current = 'PLAYER 2'
            self.player2 = self.get_player_input()
            self.player1 = self.get_remaining_tic_or_toe(self.player2)

        self.draw_board()

    def start_game(self):
        """
        The main game status

        :param: None

        :returns: None
        """
        while not self.state:
            self.current_turn()

    def close_game(self):
        """
        When closing the game by a winner or a draw print the score

        :param: None

        :returns: None
        """
        clear_sys()
        if self.is_winner in ['PLAYER 1', 'PLAYER 2']:
            print(
                C.PLAYER_WIN
                .replace('PLAYER', self.is_winner)
                .replace('0', str(self.step))
                .replace('999', str(self.score))
            )
        elif self.is_winner == 'PC':
            print(
                C.PC_WIN
                .replace(0, str(self.step))
            )
        else:
            print(C.DRAW)

    def current_turn(self):
        """
        To Evaluate step and who should perform the action

        :param: None

        :returns: None
        """
        if self.nb_players == 1:
            if self.current == 'PC':
                self.state = any(self.get_pc_choice())
                self.current = 'PLAYER 1'
            else:
                self.state = any(self.get_user_choice(self.player1))
                self.current = 'PC'
        elif self.current == 'PLAYER 2':
            self.state = any(self.get_user_choice(self.player2))
            self.current = 'PLAYER 1'
        else:
            self.state = any(self.get_user_choice(self.player1))
            self.current = 'PLAYER 2'

        self.step += 1
