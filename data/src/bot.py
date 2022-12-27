from random import choice as random_choice
from time import sleep
import data.src.const as C
from collections import Counter


class Bot:
    """
    class to manage the Bot object
    """

    def evaluate_choice(self, index, index_winner):
        """
        To evaluate a potential winning position

        :param index: (int), index of the board value
        :param index_winner: (int), index where the winner can be

        :return: (str), position to win
        """
        if index == 6:
            return self.rows[index_winner] + self.cols[index_winner]
        if index == 7:
            return self.rows[index_winner] + self.cols[::-1][index_winner]
        elif index in [0, 1, 2]:
            return self.rows[index] + self.cols[index_winner]
        else:
            return self.rows[index_winner] + str(index - 2)

    def impossible_bot(self, who, board_values, choices):
        """
        to make a hard bot instead of random

        :param who: (str), the tic or toe
        :return: (str), return the winning position
        """
        wining_player = [who] * 3
        for index, value in enumerate(board_values):
            c = list((Counter(wining_player) & Counter(value)).elements())
            if len(c) == 2:
                for i, j in enumerate(value):
                    if j != who:
                        break
                choice = self.evaluate_choice(index, i)
                if choice in choices:
                    return choice

        return None

    def get_bot_choice(self, board_values, choices):
        """
        Will randomly select a value

        :param: None

        :returns: (tuple(bool)), evaluation of Winner and game finished
        """
        bot_choice = random_choice(choices)
        choice_text = random_choice(list(C.THINKING.keys()))
        print(C.THINKING[choice_text], end="")
        for _ in range(5):
            print(".", end="", flush=True)
            sleep(0.5)
        if self.nb_players == 2:
            bot_win = self.impossible_bot(self.bot, board_values, choices)
            player_win = self.impossible_bot(self.player1, board_values, choices)
            bot_choice = bot_win or bot_choice
            if player_win and not bot_win:
                bot_choice = player_win
        return bot_choice
