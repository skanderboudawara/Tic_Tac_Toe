import data.src.const as C
from re import sub as regex_replace


class TicTacToBoard:
    """
    Class to manage the full game
    """

    def __init__(self):
        for row in self.rows:
            self.choices.extend(row + col for col in self.cols)
        self.board = {row: [row, *(["🔲"] * 3)] for row in (self.rows)}
        self.board[" "] = [" ", *self.cols]

    def draw_board(self):
        """
        to print the dict board

        :param: None

        :returns: None
        """
        self.clear_sys()
        board = C.BOARD
        for row in self.rows:
            for col in self.cols:
                board = board.replace(f"{row}{col}", self.board.get(row)[int(col)])
        board = board.replace("0", str(self.step)).replace("PLAYER", self.current)
        board = regex_replace("[A-C][1-3]", "🔲", board)
        print(board)

    def get_board_values(self):
        """
        to get all possible board values

        :return: (list), list of all possible values
        """
        diagonal_wining_1 = [
            self.board[row][int(col)] for col, row in zip(self.cols, self.rows)
        ]
        diagonal_wining_2 = [
            self.board[row][int(col)] for col, row in zip(self.cols[::-1], self.rows)
        ]
        vertical_wining = [
            [self.board[row][int(col)] for row in self.rows] for col in self.cols
        ]
        horizontal_wining = [
            [self.board[row][int(col)] for col in self.cols] for row in self.rows
        ]

        return [
            *horizontal_wining,
            *vertical_wining,
            diagonal_wining_1,
            diagonal_wining_2,
        ]

    def update_board_dict(self, choice, who):
        """
        To update the dict board with the adequate choice

        :param choice: (str), the choice that has been made by user or computer
        :param who: (str), who made the choice '❌' or '⭕️'

        :returns: None
        """
        assert isinstance(who, str), "Wrong Type: who must be a string"
        assert isinstance(choice, str), "Wrong Type: choice must be a string"
        assert who in ["❌", "⭕️"], "Wrong Value: who must be in ['❌', '⭕️']"

        previous_row = self.board[choice[0]]
        previous_row[int(choice[1])] = who
        self.board[choice[0]] = previous_row

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
        assert (
            choice in self.choices
        ), f"Wrong Value: choice must be in {', '.join(self.choices)}"
        assert who in ["❌", "⭕️"], "Wrong Value: who must be in ['❌', '⭕️']"

        self.choices.remove(choice)
        self.update_board_dict(choice, who)
        self.draw_board()
        return (self.evaluate_winner(), self.evaluate_end_game())
