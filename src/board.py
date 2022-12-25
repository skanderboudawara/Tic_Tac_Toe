
import random
import os
import time


def clear_sys():
    """
    To clear the system
    'clear' for MacOs, Linux
    'cls' for Windows

    :param: None

    :returns: None
    """
    try:
        os.system('clear')
    except Exception:
        os.system('cls')


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
        assert isinstance(score, float), 'Wrong Type: score must be a integer'

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
        assert isinstance(score, float), 'Wrong Type: score must be a integer'

        if self.score_board == {} or len(self.score_board.keys()) < 5:
            return True
        scores = [float(key) for key in self.score_board.keys()]
        scores.sort()
        return next((str(key) for key in scores if score < float(key)), False)

    def print_score(self):
        """
        To print all the top 5 scores

        :param: None

        :returns: None
        """
        if self.score_board == {}:
            return
        scores = [float(key) for key in self.score_board.keys()]
        scores.sort()
        print("\nRANK     USERNAME     SCORE\n")
        for index, score in enumerate(scores):
            print(
                f'#{str(index+1)}         {self.score_board[str(score)]}        {str(score)}\n')


class TicTacToBoard():
    """
    Class to manage the full game
    """

    def __init__(self):
        self.cols = ['1', '2', '3']
        self.rows = ['A', 'B', 'C']
        self.pc = None
        self.user = None
        self.is_winner = None
        self.state = False
        self.current = None
        self.step = 1
        self.score = 0
        clear_sys()

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
        for row in ([' '] + self.rows):
            print('  '.join(self.board.get(row)) + '\n')

    def evaluate_winner(self):
        """
        A function that will evaluate if there is a winner and who is it

        :param: None

        :returns: (bool), True if there is a winner else False
        """
        wining_pc = [self.pc]*3
        wining_user = [self.user]*3
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
                return True
            elif value == wining_user:
                self.is_winner = 'YOU'
                return True

        return False

    def evaluate_end_game(self):
        """
        Evaluate if the game has ended

        :param: None

        :returns: (bool), True all cases are filled, else false
        """
        res1 = [len([i for i in self.board[row] if i not in ['🔲', *self.rows]])
                for row in self.rows]
        return res1 == [3, 3, 3]

    def get_user_choice(self):
        """
        Will get the user input

        :param: None

        :returns: (tuple(bool)), evaluation of Winner and game finished
        """
        start = time.time()
        get_input = True
        print(
            f'[Step {str(self.step)}] Select one of the following choices: {", ".join(self.choices)}: \n')
        while get_input:
            user_choice = input('Your choice: ')
            get_input = user_choice not in self.choices
        end = time.time() - start
        self.score = round(self.step * (self.score + end), 0)
        return self.execute_update(user_choice, self.user)

    def get_pc_choice(self):
        """
        Will randomly select a value

        :param: None

        :returns: (tuple(bool)), evaluation of Winner and game finished
        """
        pc_choice = random.choice(self.choices)
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
        assert isinstance(
            who, str), "Wrong Type: who must be a string"
        assert isinstance(choice, str), "Wrong Type: choice must be a string"
        assert who in [
            '❌', '⭕️'], "Wrong Value: who must be in ['❌', '⭕️']"
        previous_row = self.board[choice[0]]
        previous_row[int(choice[1])] = who
        self.board[choice[0]] = previous_row

    def pre_start_game(self):
        """
        Will init the game to select who start and to select a Tic or a Tac

        :param: None

        :returns: None
        """

        if random.choice(['PC', 'YOU']) == 'PC':
            self.pc = random.choice(['❌', '⭕️'])
            self.user = '❌' if self.pc == '⭕️' else '⭕️'
            self.current = 'PC'
        else:
            get_input = True
            while get_input:
                user_choice = input(
                    'You will go first, please select between "X", "O": ')
                get_input = user_choice.upper() not in ['X', 'O']
            self.user = '❌' if user_choice.upper() == 'X' else '⭕️'
            self.pc = '❌' if self.user == '⭕️' else '⭕️'
            self.current = 'YOU'
        self.draw_board()
        if self.current == 'PC':
            print(f'The computer will go first and have chosen {self.pc}')

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
        if self.is_winner == 'YOU':
            print('\n==========================================')
            print(
                f'\n  🏆 Congrats! The winner is You in {str(self.step)} steps with a score of {self.score}')
            print('\n==========================================')
        elif self.is_winner == 'PC':
            print('\n==========================================')
            print(f'\n  🥲 You lost in {str(self.step)} steps! ')
            print('\n==========================================')
        else:
            print('\n==========================================')
            print('\n  🥶 Draw! No winner ! ')
            print('\n==========================================')

    def current_turn(self):
        """
        To Evaluate step and who should perform the action

        :param: None

        :returns: None
        """
        if self.current == 'PC':
            self.state = any(self.get_pc_choice())
            self.current = 'YOU'
        else:
            self.state = any(self.get_user_choice())
            self.current = 'PC'

        self.step += 1
