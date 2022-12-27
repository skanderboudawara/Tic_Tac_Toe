from time import time
import data.src.const as C


class Player:
    """
    Class to manage the player object
    """

    def get_user_choice(self, user):
        """
        Will get the user input

        :param: None

        :returns: (tuple(bool)), evaluation of Winner and game finished
        """
        start = time()
        get_input = True
        print(
            C.SELECT_CHOICE.replace("PLAYER", self.current)
            .replace("TICTOE", user)
            .replace("ALL_CHOICE", ", ".join(self.choices))
        )
        while get_input:
            user_choice = input("Your choice: ")
            get_input = user_choice not in self.choices
        end = time() - start
        self.score = int(round(self.step * (self.score + end), 0))
        return self.execute_update(user_choice, user)

    def get_player_input(self):
        """
        To get user input and convert it

        :param: None

        :returns: (str), the selected choice converted to ❌ or ⭕️
        """
        get_input = True
        while get_input:
            tic_or_toe = input(f'{self.current}, please select between "X", "O": ')
            get_input = tic_or_toe.upper() not in ["X", "O"]
        tic_or_toe = "❌" if tic_or_toe.upper() == "X" else "⭕️"
        return tic_or_toe

    def get_remaining_tic_or_toe(self, choice):
        """
        if X is selected return O and vice versa

        :param choice: (str), X or O

        :return: (str), the remaining choice
        """
        return "❌" if choice == "⭕️" else "⭕️"

    def get_player1_info(self):
        """
        To get player 1 choice

        :param: None

        :returns: the remaining choice
        """
        self.current = "PLAYER 1"
        self.player1 = self.get_player_input()
        return self.get_remaining_tic_or_toe(self.player1)
