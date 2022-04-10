from .square import Square, SquareState
from typing import List
import itertools
import random


class Board:
    """
    Models the board and its squares.
    TODO: Complete methods in top-to-bottom order.

    Note that initially, before any method implementation, squares can be accessed in the following way:
    >>  board = Board(game)
    >>  rows = board.rows
    >>  len(rows)
            3
    >>  len(rows[0])
            3
    >> rows[0][0].row, rows[0][0].column
            (0, 0)
    >> rows[0][0].state
            <SquareState.EMPTY: ' '>

    Be sure to reference the Square class in square.py.
    """

    def __init__(self, game, matrix: List[List[SquareState]] = None):
        self.game = game
        matrix = matrix or [[SquareState.EMPTY for column in range(3)] for row in range(3)]
        self.rows: List[List[Square]] = [
            [Square(row, column, self, matrix[row][column]) for column in range(3)]
            for row in range(3)
        ]

    @classmethod
    def FromCharacterMatrix(cls, game, matrix: List[List[str]]):
        map = {' ': SquareState.EMPTY, 'X': SquareState.X, 'O': SquareState.O}
        square_state_matrix: List[List[SquareState]] = [[map[c] for c in row] for row in matrix]
        return cls(game, square_state_matrix)

    @property
    def columns(self) -> List[List[Square]]:
        """Organize squares into columns. TODO: complete me!"""
        pass

    @property
    def squares(self) -> List[Square]:
        """Combine all rows into one list of squares. TODO: complete me!"""
        pass

    @property
    def unclaimed_squares(self) -> List[Square]:
        """Identify unclaimed squares. TODO: complete me!"""
        pass

    def choose_unclaimed_square(self) -> Square:
        """Choose a random unclaimed square. TODO: complete me!"""
        pass

    @property
    def diagonal_1(self) -> List[Square]:
        """The top-left to bottom-right diagonal. TODO: complete me!"""
        pass

    @property
    def diagonal_2(self) -> List[Square]:
        """The top-right to bottom-left diagonal. TODO: complete me!"""
        pass

    @property
    def all_lines(self) -> List[List[Square]]:
        """All possible 'lines' which could lead to a win, including rows, columns, and diagonals. TODO: complete me!"""
        pass
