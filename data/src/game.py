from data.src.bot import Bot
from data.src.player import Player
from data.src.board import TicTacToBoard
import data.src.const as C
from random import choice as random_choice
from re import sub as regex_replace
from os import system
import json


class ScoreBoard:
    """
    Class to Manage the score board
    """

    def __init__(self):
        with open(C.PATH_SCORE_BOARD, "r+") as f:
            try:
                self.score_board = json.load(f)
            except json.JSONDecodeError:
                with open(C.PATH_SCORE_BOARD, "w") as f2:
                    self.score_board = {}
                    json.dump(self.score_board, f2)

    def add_score(self, user_name, score):
        """
        Will add the lowest score to the board

        :param user_name: (str), the user name
        :param score: (float), the score he marked

        :returns: None
        """
        assert isinstance(user_name, str), "Wrong Type: User name must be a string"
        assert isinstance(score, int), "Wrong Type: score must be a integer"

        eval_score = self.is_best_score(score)
        if eval_score and isinstance(eval_score, bool):
            self.score_board[str(score)] = (user_name.upper())[:3]
        elif isinstance(eval_score, str):
            self.score_board.remove(self.is_high_score(score))
            self.score_board[score] = (user_name.upper())[:3]
        with open(C.PATH_SCORE_BOARD, "w") as f:
            json.dump(self.score_board, f)

    def is_best_score(self, score):
        """
        Will check if the score marked is the lowest score saved

        :param score: (float), the score to evaluate

        :returns: (bool or str), True or str if it's a good score else False
        """
        assert isinstance(score, int), "Wrong Type: score must be a integer"

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
                score_board = score_board.replace(
                    f"AAA{str(index+1)}", self.score_board[str(score)]
                ).replace(f"SCORE{str(index+1)}", str(score))
        score_board = regex_replace("(AAA|SCORE)[1-5]", "   ", score_board)
        print(score_board)


class Game(Bot, Player, TicTacToBoard):
    """
    Class to manage the full game

    :param nb_players: (int), define who is going to play
    """

    def __init__(self, nb_players):

        assert isinstance(nb_players, int), "nb_players must be an int"
        assert nb_players in [1, 2, 3], "nb_players must be in [1,2,3]"

        self.cols = ["1", "2", "3"]
        self.rows = ["A", "B", "C"]
        self.bot = None
        self.nb_players = nb_players
        self.is_winner = ""
        self.player1 = None
        self.player2 = None
        self.state = False
        self.current = ""
        self.step = 1
        self.score = 0
        self.choices = []
        self.board = {}
        super().__init__()

    def clear_sys(self):
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

    def evaluate_winner(self):
        """
        A function that will evaluate if there is a winner and who is it

        :param: None

        :returns: (bool), True if there is a winner else False
        """
        wining_bot = [self.bot] * 3
        wining_player1 = [self.player1] * 3
        wining_player2 = [self.player2] * 3
        board_values = self.get_board_values()
        for value in board_values:
            value = value if len(value) == 3 else value[1:]
            if value == wining_bot:
                self.is_winner = "BOT"
                break
            elif value == wining_player1:
                self.is_winner = "PLAYER 1"
                break
            elif value == wining_player2:
                self.is_winner = "PLAYER 2"
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
        res1 = [
            len([i for i in self.board[row] if i not in ["🔲", *self.rows]])
            for row in self.rows
        ]
        return res1 == [3] * 3

    def select_tic_or_toe(self):
        """
        Will init the game to select who start and to select a Tic or a Tac

        :param: None

        :returns: None
        """
        if self.nb_players in [1, 2]:
            if random_choice(["BOT", "PLAYER 1"]) == "BOT":
                self.bot = random_choice(["❌", "⭕️"])
                self.player1 = self.get_remaining_tic_or_toe(self.bot)
                self.current = "BOT"
            else:
                self.bot = self.get_player1_info()
        elif random_choice(["PLAYER 1", "PLAYER 2"]) == "PLAYER 1":
            print("\nPLAYER 1 You will go first\n")
            self.player2 = self.get_player1_info()
        else:
            print("\nPLAYER 2 You will go first\n")
            self.current = "PLAYER 2"
            self.player2 = self.get_player_input()
            self.player1 = self.get_remaining_tic_or_toe(self.player2)

        self.draw_board()

    def start_game(self):
        """
        The main game status

        :param: None

        :returns: None
        """
        self.select_tic_or_toe()
        while not self.state:
            self.current_turn()
        self.end_game_screen()

    def end_game_screen(self):
        """
        When closing the game by a winner or a draw print the score

        :param: None

        :returns: None
        """
        self.clear_sys()
        if self.is_winner in ["PLAYER 1", "PLAYER 2"]:
            print(
                C.PLAYER_WIN.replace("PLAYER", self.is_winner)
                .replace("0", str(self.step))
                .replace("999", str(self.score))
            )
        elif self.is_winner == "BOT":
            print(C.BOT_WIN.replace("0", str(self.step)))
        else:
            print(C.DRAW)

    def current_turn(self):
        """
        To Evaluate step and who should perform the action

        :param: None

        :returns: None
        """
        if self.nb_players in [1, 2]:
            if self.current == "BOT":
                bot_choice = self.get_bot_choice(self.get_board_values(), self.choices)
                self.state = any(self.execute_update(bot_choice, self.bot))
                self.current = "PLAYER 1"
            else:
                self.state = any(self.get_user_choice(self.player1))
                self.current = "BOT"
        elif self.current == "PLAYER 2":
            self.state = any(self.get_user_choice(self.player2))
            self.current = "PLAYER 1"
        else:
            self.state = any(self.get_user_choice(self.player1))
            self.current = "PLAYER 2"

        self.step += 1
