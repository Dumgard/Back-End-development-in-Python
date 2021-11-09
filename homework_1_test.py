import unittest
from collections import Iterable
from homework_1 import TicTacToe


class TestTicTacToe(unittest.TestCase):
    """
    Class for testing my TicTacToe game-class.
    """

    def test_write(self):
        game = TicTacToe()
        messages = [
            'board', 'greeting', 'input', 'winput', 'c',
            'stalemate', '1', '2', 'again', 'bye',
            'asd', 'something', '', 1, 3451, -12.51, None
        ]
        replies = [
            game,
            'Welcome to my Tic-Tac-Toe game! '
            'If you want to end the game at any point - please, '
            'enter "c" symbol ("c" from close).',
            f'Move of {"1st" if game.turn % 2 else "2nd"} '
            f'players {"(X)" if game.turn % 2 else "(O)"}.'
            f' \nPlease, enter number of cell you want to capture (from 1 to 9):\n ',
            'Please, enter the valid number '
            '(integer from 1 to 9) of cell that is not captured: \n',
            '\n Early termination of game. Bye!\n',
            '\nThis is a stalemate! :(\n',
            '\nThe 1st players won! Congratulations!\n',
            '\nThe 2nd players won! Congratulations!\n',
            'Want to try again? Enter "1" if so. '
            'Any other input will be considered as rejection.\n',
            'Ok! See you later!\n',
            None, None, None, None, None, None, None
        ]
        for mes, rep in zip(messages, replies):
            self.assertEqual(rep, game.write(cmd=False, message=mes))

    def test_read(self):
        game = TicTacToe()
        inputs = [
            ['8', '8', '3', '8', '3', '4', '8', '4', '8', '1', '8', '9', '2', '4', '3', '8'],
            ['4', '2', '6', '2', '2', '2', '8', '4', '8', '9', '9', '8', '6', '8', '6', '6',
             '7', '5', '8', '9', '9', '4', '2', '7', '2', '8'],
            ['4', '2', '6', '2', ' 2', '2', ' c ', '8 ', '4 ', '8', '9'],
            ['9', '8', '8', '1', '6', '7', '6', '5', '4 ', '1', '1', 'c', '2', '4', '3', '7'],
            ['asc', '2 123 5', 'asd ga d', '1 1', 'asd 1 13 f', '7', 'ash', 'c', '113', '1',
             '1', '2', '4', '3', '7'],
            ['asc', '2 123 5', 'asd ga d', '1 1', 'asd 1 13 f', '7', 'ash', '113', '1', '1',
             '8', '4', '9', 'c'],
        ]
        answers = inputs.copy()

        for inp, ans in zip(inputs, answers):
            game.steps = inp if not isinstance(inp, Iterable) else iter(inp)
            for a in ans:
                self.assertEqual(a, game.read())

    def test_reset(self):
        """
        Tests of TicTacToe.reset() method.
        """
        game_1 = TicTacToe()
        game_2 = TicTacToe()
        game_2.reset()
        self.assertEqual(game_1.board, game_2.board)
        self.assertEqual(game_1.turn, game_2.turn)

    def test_next_move(self):
        """
        Tests of TicTacToe.next_move() method.
        -1  - code of early exit
        -2  - code of wrong input
        """
        game = TicTacToe()
        moves = {
            ' 1': ('X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '),
            '2 ': ('X', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' '),
            '6  ': ('X', 'O', ' ', ' ', ' ', 'X', ' ', ' ', ' '),
            '    7': ('X', 'O', ' ', ' ', ' ', 'X', 'O', ' ', ' '),
            'c ': -1,
            'hhgf': -2,
            'C': -1,
            'h': -2,
            ' 1 ': -2,
            '  1 ': -2,
            ' 1   ': -2,
            ' 2 ': -2,
            ' 8 ': ('X', 'O', ' ', ' ', ' ', 'X', 'O', 'X', ' '),
            'asd ase 12 f a': -2,
        }
        for move, answer in moves.items():
            self.assertEqual(answer, game.next_move(move))

    def test_finished(self):
        """
        Tests of TicTacToe.finished() method.
        Boards should be legal as non of methods change self.board type or length.
        """
        game = TicTacToe()
        boards = [
            ['X', 'O', ' ', ' ', ' ', 'X', 'O', 'X', ' '],
            [' ' for _ in range(9)],
            ['O' for _ in range(9)],
            ['X' for _ in range(9)],
            ['X', 'X', 'X', 'O', 'O', 'O', ' ', ' ', ' '],
            ['X', 'X', 'X', 'X', 'O', 'O', 'O', ' ', ' '],
            ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'O', 'X', 'O', 'A', 'X', 'O'],
            ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O'],
        ]
        answers = [
            (False, 0),
            (False, 0),
            (True, -1),
            (True, 1),
            (True, 1),
            (True, 1),
            (True, 1),
            (True, 0),
            (True, 0),
        ]

        for board, ans in zip(boards, answers):
            game.board = board
            self.assertEqual(ans, game.finished())

    def test_start_game(self):
        """
        Tests of TicTacToe.start_game() method.
         1  - won first players,
        -1  - won second players,
         0  - stalemate
        """
        list_steps = [
            list(map(str, [1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1])),
            list(map(str, [1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1])),
            ['8', '8', '3', '8', '3', '4', '8', '4', '8', '1', '8', '9', '2', '4', '3', '8'],
            ['4', '2', '6', '2', '2', '2', '8', '4', '8', '9', '9', '8', '6', '8', '6', '6',
             '7', '5', '8', '9', '9', '4', '2', '7', '2', '8'],
            ['4', '2', '6', '2', '2', '2', 'c', '8', '4', '8', '9'],
            ['9', '8', '8', '1', '6', '7', '6', '5', '4', '1', '1', 'c', '2', '4', '3', '7'],
            ['9', '8', '8', '1', '6', '7', '6', '5', '4', '1', '1', '2', '4', '3', '7'],
            ['6', '1', '9', '5', '5', '3', '2', '8', '4', '7', '4', '7', '3', '8', '6', '7'],
            ['asc', '2 123 5', 'asd ga d', '1 1', 'asd 1 13 f', '7', 'ash', 'c', '113', '1',
             '1', '2', '4', '3', '7'],
            ['asc', '2 123 5', 'asd ga d', '1 1', 'asd 1 13 f', '7', 'ash', '113', '1', '1',
             '8', '4', '9', 'c'],
            list(map(str, [1, 2, 3, 5, 4, 7, 6, 9, 8]))
        ]
        answers = [
            [(('X', 'O', 'X', 'O', 'X', 'O', 'X', ' ', ' '), 1), (('X', 'O', 'X', 'O', 'X',
                                                                   'O', 'X', ' ', ' '), 1)],
            [(('X', 'O', 'X', 'O', 'X', 'O', 'X', ' ', ' '), 1)],
            [(('O', 'O', 'O', 'X', ' ', ' ', ' ', 'X', 'X'), -1)],
            [((' ', 'O', ' ', 'X', 'X', 'X', 'O', 'O', 'X'), 1)],
            [('C',)],
            [(('X', ' ', ' ', 'X', 'O', 'O', 'X', 'O', 'X'), 1), ('C',)],
            [(('X', ' ', ' ', 'X', 'O', 'O', 'X', 'O', 'X'), 1), (('X', 'O', 'O', 'X', ' ',
                                                                   ' ', 'X', ' ', ' '), 1)],
            [(('O', ' ', 'X', ' ', 'O', 'X', ' ', ' ', 'X'), 1)],
            [('C',)],
            [(('O', ' ', ' ', 'O', ' ', ' ', 'X', 'X', 'X'), 1)],
            [(('X', 'O', 'X', 'X', 'O', 'X', 'O', 'X', 'O'), 0)]
        ]

        game = TicTacToe()
        for steps, ans in zip(list_steps, list(map(tuple, answers))):
            game.reset()
            game.history = []
            res = game.start_game(cmd=False, steps=steps)
            self.assertEqual(ans, res)


if __name__ == '__main__':
    unittest.main()
