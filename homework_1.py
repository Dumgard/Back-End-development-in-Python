from collections.abc import Iterable


class TicTacToe:
    """
    My TicTacToe game-implementing class
    """
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.turn = 1

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

    def reset(self):
        """
        This method resets the board.
        :return:    None
        """
        self.board = [' ' for _ in range(9)]
        self.turn = 1

    def next_move(self, entry=None):
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
            entry = input(
                f'Move of {"1st" if self.turn % 2 else "2nd"} '
                f'player {"(X)" if self.turn % 2 else "(O)"}.'
                f' \nPlease, enter number of cell you want to capture (from 1 to 9):\n '
            ).strip()
            while True:
                if entry == 'c':
                    return -1
                if entry.isdigit() and int(entry) in (1, 2, 3, 4, 5, 6, 7, 8, 9) \
                        and self.board[int(entry) - 1] == ' ':
                    self.board[int(entry) - 1] = 'X' if self.turn % 2 else 'O'
                    break
                entry = input('Please, enter the valid number '
                              '(integer from 1 to 9) of cell that is not captured: \n').strip()
            self.turn += 1
            print(self)
            return 0
        entry = entry.strip()
        if entry.isdigit() and int(entry) in (1, 2, 3, 4, 5, 6, 7, 8, 9):
            # We want to ignore impossible move if it was not given via cmd-line
            # so we don't want to ask for valid move.
            # Also there is no need to print the board,
            # but it may be useful to return current board as tuple.
            if self.board[int(entry) - 1] == ' ':
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

    def start_game(self, steps=None):
        """
        This method implements the game mechanic in general.
        There is an opportunity to give "move" arg, which may contain single move
        as well as Iterable of moves. It is may be helpful in unit-testing.
        :return:
            1) Steps is None:       None
            2) Steps is not None:   list[
                    tuple(   tuple(resulting 'self.board' after finishing the game), int(win)   )
                ]
                                        (win -> 1 if won 1st, -1 if won 2nd, 0 if stalemate)
        """
        if steps is None:
            while True:
                print('Welcome to my Tic-Tac-Toe game! '
                      'If you want to end the game at any point - please, '
                      'enter "c" symbol ("c" from close).')
                print(self)
                condition = self.finished()
                while not condition[0]:
                    if self.next_move() is not None:
                        print('\n Early termination of game. Bye!\n')
                        return -1
                    condition = self.finished()
                if condition[1] == 0:
                    print('\nThis is a stalemate! :(\n')
                else:
                    print(f'\nThe {"1st" if condition[1] > 0 else "2nd"} player won! '
                          f'Congratulations!\n')
                try_again = input('Want to try again? Enter "1" if so. '
                                  'Any other input will be considered as rejection.\n')
                if try_again.isdigit() and int(try_again) == 1:
                    self.reset()
                    print(self)
                else:
                    print('Ok! See you later!\n')
                    break
        else:
            if not isinstance(steps, Iterable):
                return self.next_move(steps)
            answer = []
            condition = self.finished()
            for step in steps:
                step = step.strip()
                if step == 'c':
                    break
                # print(self.turn, '    asd    ', step)
                if answer and self.turn == 1:
                    # print(step)
                    if not step.isdigit() or int(step) != 1:
                        # print('here')
                        return answer
                if condition[0]:
                    answer.append((tuple(self.board), condition[1]))
                    self.reset()
                    if not step.isdigit() or int(step) != 1:
                        return answer
                    condition = self.finished()
                    continue
                if self.next_move(step) == -1:
                    answer.append(-1)
                    return answer
                condition = self.finished()
            if condition[0]:
                answer.append((tuple(self.board), condition[1]))
            return answer


if __name__ == "__main__":
    s = TicTacToe()
    s.start_game()
