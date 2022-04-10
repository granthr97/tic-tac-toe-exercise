from unittest.mock import MagicMock
import pytest

from ..src import Board


class TestBoard:

    @pytest.fixture()
    def game(self):
        return MagicMock()

    @pytest.mark.parametrize("matrix", [
        [['X', 'O', 'X'],
         ['O', 'X', 'O'],
         ['X', 'O', 'X']],

        [['O', 'O', 'O'],
         ['O', 'O', 'O'],
         ['O', 'O', 'O']],

        [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']],

        [['X', 'X', 'X'],
         ['X', 'X', 'X'],
         ['X', 'X', 'X']]
    ])
    def test_squares(self, matrix):
        board = Board.FromCharacterMatrix(self.game, matrix)
        for square in board.squares:
            assert square.state.value == matrix[square.row][square.column]

    @pytest.mark.parametrize("matrix,expected_coordinates", [
        ([['X', 'O', 'X'],
         ['O', ' ', 'O'],
         ['X', 'O', 'X']], {(1, 1)}),

        ([['O', ' ', 'O'],
         ['O', 'O', 'O'],
         ['O', 'O', ' ']], {(0, 1), (2, 2)}),

        ([[' ', ' ', ' '],
         ['X', 'X', 'X'],
         ['X', 'X', 'X']], {(0, 0), (0, 1), (0, 2)}),

        ([['X', 'X', 'X'],
         ['X', 'X', 'X'],
         ['X', 'X', 'X']], set())
    ])
    def test_unclaimed_squares(self, matrix, expected_coordinates):
        board = Board.FromCharacterMatrix(self.game, matrix)
        unclaimed_squares = board.unclaimed_squares
        unclaimed_square_coordinates = {(square.row, square.column) for square in unclaimed_squares}
        assert unclaimed_square_coordinates == expected_coordinates

    @pytest.mark.parametrize("matrix,expected_columns", [
        ([['X', 'O', ' '],
         ['O', ' ', 'X'],
         ['X', 'O', 'X']],

         [['X', 'O', 'X'],
          ['O', ' ', 'O'],
          [' ', 'X', 'X']]),
    ])
    def test_columns(self, matrix, expected_columns):
        board = Board.FromCharacterMatrix(self.game, matrix)
        columns = board.columns
        for column in columns:
            for square in column:
                assert square.state.value == expected_columns[square.column][square.row]

    @pytest.mark.parametrize("matrix,expected_diagonal", [
        ([['X', 'O', ' '],
         ['O', ' ', 'X'],
         ['X', 'O', 'X']], ['X', ' ', 'X']),
        ([['X', 'O', ' '],
         ['O', 'O', 'X'],
         ['X', 'O', ' ']], ['X', 'O', ' '])
    ])
    def test_diagonal_1(self, matrix, expected_diagonal):
        board = Board.FromCharacterMatrix(self.game, matrix)
        diagonal = board.diagonal_1
        assert [square.state.value for square in diagonal] == expected_diagonal

    @pytest.mark.parametrize("matrix,expected_diagonal", [
        ([['X', 'O', ' '],
         ['O', ' ', 'X'],
         ['X', 'O', 'X']], [' ', ' ', 'X']),
        ([['X', 'O', ' '],
         ['O', 'O', 'X'],
         ['X', 'O', ' ']], [' ', 'O', 'X'])
    ])
    def test_diagonal_2(self, matrix, expected_diagonal):
        board = Board.FromCharacterMatrix(self.game, matrix)
        diagonal = board.diagonal_2
        assert [square.state.value for square in diagonal] == expected_diagonal

    @pytest.mark.parametrize("matrix,expected_lines", [
        ([['X', 'O', ' '],
          ['O', ' ', 'X'],
          ['X', 'O', 'X']],
         {
             ('X', 'O', ' '),
             ('O', ' ', 'X'),
             ('X', 'O', 'X'),
             ('X', 'O', 'X'),
             ('O', ' ', 'O'),
             (' ', 'X', 'X'),
             ('X', ' ', 'X'),
             (' ', ' ', 'X')
         }),
    ])
    def test_all_lines(self, matrix, expected_lines):
        board = Board.FromCharacterMatrix(self.game, matrix)
        all_lines = board.all_lines
        line_set = {tuple([square.state.value for square in line]) for line in all_lines}
        assert line_set == expected_lines


