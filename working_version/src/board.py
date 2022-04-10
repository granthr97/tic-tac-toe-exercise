from .square import Square, SquareState
from typing import List
import itertools
import random


class Board:
    """Models the board and its squares."""

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
        """Organize squares into columns."""
        return [[self.rows[i][n] for i in range(3)] for n in range(3)]

    @property
    def squares(self) -> List[Square]:
        """Combine all rows into one list of squares."""
        return list(itertools.chain(*self.rows))

    @property
    def unclaimed_squares(self) -> List[Square]:
        """Identify unclaimed squares."""
        return [square for square in self.squares if square.state == SquareState.EMPTY]

    def choose_unclaimed_square(self) -> Square:
        """Choose a random unclaimed square."""
        return random.choice(self.unclaimed_squares)

    @property
    def diagonal_1(self) -> List[Square]:
        """The top-left to bottom-right diagonal."""
        return [self.rows[i][i] for i in range(3)]

    @property
    def diagonal_2(self) -> List[Square]:
        """The top-right to bottom-left diagonal."""
        return [self.rows[i][2 - i] for i in range(3)]

    @property
    def all_lines(self) -> List[List[Square]]:
        """All possible 'lines' which could lead to a win, including rows, columns, and diagonals."""
        return list(itertools.chain(self.rows, self.columns, [self.diagonal_1, self.diagonal_2]))
