from unittest.mock import MagicMock
from mockito import mock
import pytest
from ..src import Game, Board


class TestGame:

    @pytest.fixture()
    def window(self):
        return mock()

    @pytest.mark.parametrize("matrix,win", [
        ([['X', 'O', 'X'],
          ['O', 'X', 'O'],
          ['X', 'O', 'X']], True),

        ([['O', 'X', 'O'],
          ['O', 'O', 'X'],
          ['O', 'X', 'O']], True),

        ([[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' ']], False),

        ([['O', 'X', 'X'],
          ['X', 'O', 'X'],
          ['X', 'X', 'O']], True)
    ])
    def test_win(self, matrix, win):
        game = Game(self.window)
        game.board = Board.FromCharacterMatrix(game, matrix)
        assert bool(game.winner) == win

    @pytest.mark.parametrize("matrix,draw", [
        ([['X', 'O', 'X'],
          ['O', 'X', 'O'],
          ['X', 'O', 'X']], False),

        ([['O', 'X', 'O'],
          ['O', 'O', 'X'],
          ['O', 'X', 'O']], False),

        ([[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' ']], False),

        ([['X', 'O', ' '],
          ['O', 'X', 'O'],
          ['X', 'O', 'X']], False),

        ([['O', 'X', 'X'],
          ['X', 'X', 'X'],
          ['X', 'X', 'O']], False),

        ([['O', 'O', 'X'],
          ['X', 'X', 'O'],
          ['O', 'X', 'O']], True),
    ])
    def test_draw(self, matrix, draw):
        game = Game(self.window)
        game.board = Board.FromCharacterMatrix(game, matrix)
        assert game.draw == draw
