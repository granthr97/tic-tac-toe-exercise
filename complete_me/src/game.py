from typing import Union
import time
import random
import tkinter
import threading
from enum import Enum

from .board import Board
from .square import Square, SquareState

AI_PAUSE_MILLISECOND_RANGE = range(250, 2000)


class GameState(Enum):
    """Enumerate the possible states of the game."""
    USER_TURN = 'YOUR TURN'
    AIS_TURN = "AI'S TURN"
    COMPLETED = "COMPLETED"


class Game:
    """
    Performs game logic including starting the UI, running AI moves, and evaluating the game state.
    TODO: After completing all methods in the Board class, complete draw() and winner().
    """

    def __init__(self, window: tkinter.Tk):
        self.window = window
        self.board = Board(self)
        self.state = GameState.USER_TURN

    def user_click(self, square: Square):
        """When the user clicks the square, update the square to an X and run the logic for AI's turn."""
        if square.state == SquareState.EMPTY and self.state == GameState.USER_TURN:
            square.state = SquareState.X
            self.window.update()
            self.evaluate_state()
            threading.Thread(target=self.ai_turn).start()

    def ai_turn(self) -> None:
        """Run AI's turn: evaluate the game state, wait, choose a square, and then evaluate the game state."""
        if self.state == GameState.AIS_TURN:
            time.sleep(random.choice(AI_PAUSE_MILLISECOND_RANGE) * 0.001)
            random_square = self.board.choose_unclaimed_square()
            random_square.state = SquareState.O
            self.evaluate_state()

    def evaluate_state(self) -> None:
        """Evaluate the game state: check if there is a win or a draw."""
        if self.winner or self.draw:
            self.state = GameState.COMPLETED
        elif self.state == GameState.USER_TURN:
            self.state = GameState.AIS_TURN
        else:
            self.state = GameState.USER_TURN

    @property
    def draw(self) -> bool:
        """Check if the game is a draw. TODO: complete me!"""
        pass

    @property
    def winner(self) -> Union[None, SquareState]:
        """Check if the game has been won. If so, return the winner. Otherwise, return None. TODO: complete me!"""
        pass

