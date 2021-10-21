# pylint: disable=missing-module-docstring
from collections.abc import Iterable


class TicTacToe:
    """
    My TicTacToe game-implementing class
    """

    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.turn = 1
        self.history = []
        self.steps = None

    def __str__(self):
        spaces_1 = '{a}    |{b}    |{c}    \n'
        spaces_2 = '_____|_____|_____\n'
        board_string_representation = spaces_1.format(a=1, b=2, c=3)
        for key in range(1, 10):
            val = self.board[key - 1]
            if key % 3:
                board_string_representation += f'  {val}  |'
            else:
                board_string_representation += f'  {val}  \n'
                if key < 7:
                    board_string_representation += spaces_2 + \
                                                   spaces_1.format(a=key + 1, b=key + 2, c=key + 3)
        return board_string_representation + spaces_1.format(a=' ', b=' ', c=' ')

    def write(self, cmd=True, message=None):
        """
        :param cmd:
            True if we should write in cmd, else False. This parameter
            is for compatibility with start_game method.
        :param message:
            'board'     -   print board
            'greeting'  -   to greet the players
            'input'     -   prompt to enter a move
            'winput'    -   wrong input
            'c'         -   early exit
            'stalemate' -   game ending with stalemate
            '1'         -   first player won
            '2'         -   second player won
            'again'     -   invitation to try again
            'bye'       -   if user rejected to try again
        """
        replies = {
            'board': self,
            'greeting': 'Welcome to my Tic-Tac-Toe game! '
                        'If you want to end the game at any point - please, '
                        'enter "c" symbol ("c" from close).',
            'input': f'Move of {"1st" if self.turn % 2 else "2nd"} '
                     f'player {"(X)" if self.turn % 2 else "(O)"}.'
                     f' \nPlease, enter number of cell you want to capture (from 1 to 9):\n ',
            'winput': 'Please, enter the valid number '
                      '(integer from 1 to 9) of cell that is not captured: \n',
            'c': '\n Early termination of game. Bye!\n',
            'stalemate': '\nThis is a stalemate! :(\n',
            '1': '\nThe 1st player won! Congratulations!\n',
            '2': '\nThe 2nd player won! Congratulations!\n',
            'again': 'Want to try again? Enter "1" if so. '
                     'Any other input will be considered as rejection.\n',
            'bye': 'Ok! See you later!\n'
        }
        if message in replies:
            if cmd:
                print(replies[message])
                return None
            return replies[message]
        return None

    def read(self):
        """
        This function reads next move
        :return:
        """
        if self.steps is None:
            return input().strip().lower()
        if isinstance(self.steps, Iterable):
            return next(self.steps)
        temp = self.steps.copy()
        self.steps = None
        return temp

    def reset(self):
        """
        This method resets the board.
        :return:    None
        """
        self.board = [' ' for _ in range(9)]
        self.turn = 1

    def next_move(self, entry):
        """
        This method implements the 'make your move'-functional.
        There is an opportunity to give "move" arg, which may contain single move,
        and it is really helpful in unit-testing.
         0  - code of regular shutdown of the function
        -1  - code of early exit
        -2  - code of wrong input
        :return:
            1) Move is None:        None
            2) Move is not None:    tuple(self.board)
        """
        if entry is None:
            return -1
        entry = entry.strip().lower()
        if entry.isdigit() and int(entry) in (1, 2, 3, 4, 5, 6, 7, 8, 9) \
                and self.board[int(entry) - 1] == ' ':
            self.board[int(entry) - 1] = 'X' if self.turn % 2 else 'O'
            self.turn += 1
            return tuple(self.board)
        if entry == 'c':
            return -1
        return -2

    def finished(self):
        """
        This method checks if the game is finished.
        :return:
            If game is finished and:
                1) It is a stalemate:   returns (true, 0)
                2) 1st player won:      returns (true, 1)
                3) 2nd player won:      returns (true, -1)
            Else:
                                        returns (false, 0)
        """
        lines = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),    # Horizontal lines
            (0, 3, 6), (1, 4, 7), (2, 5, 8),    # Vertical lines
            (0, 4, 8), (2, 4, 6)                # Diagonal lines
        )
        for line in lines:
            line_sum = 0
            for idx in line:
                if self.board[idx] == 'X':
                    line_sum += 1
                elif self.board[idx] == 'O':
                    line_sum -= 1
            if line_sum == 3:
                return True, 1
            if line_sum == -3:
                return True, -1
        if ' ' in self.board:
            return False, 0
        return True, 0

    def start_game(self, cmd=True, steps=None):
        """
        This method implements the game mechanic in general.
        There is an opportunity to give "move" arg, which may contain single move
        as well as Iterable of moves. It is may be helpful in unit-testing.
        :return:

        """
        self.steps = steps if not isinstance(steps, Iterable) else iter(steps)
        self.write(cmd, 'greeting')
        try:
            while True:
                self.write(cmd, 'board')
                self.write(cmd, 'input')
                condition = self.finished()
                while not condition[0]:
                    step = self.read()
                    res = self.next_move(step)
                    if res == -2:
                        self.write(cmd, 'winput')
                        continue
                    if res == -1:
                        self.write(cmd, 'c')
                        self.history.append(('C',))
                        return tuple(self.history)
                    condition = self.finished()
                    self.write(cmd, 'board')
                    self.write(cmd, 'input')
                self.history.append((tuple(self.board), condition[1]))
                self.write(cmd,
                           'stalemate' if condition[1] == 0 else ('1' if condition[1] > 0 else '2'))
                self.write(cmd, 'again')
                try_again = self.read().strip()
                if try_again.isdigit() and int(try_again) == 1:
                    self.reset()
                else:
                    self.write(cmd, 'bye')
                    return tuple(self.history)
        except StopIteration:
            return tuple(self.history)


if __name__ == "__main__":
    s = TicTacToe()
    s.start_game()
