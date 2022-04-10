from enum import Enum
import tkinter as tk


class SquareState(Enum):
    """Possible states of a square: 'X', 'O', or empty."""
    X = 'X'
    O = 'O'
    EMPTY = ' '


class Square:
    """Represents a square on the tic-tac-toe board."""

    def __init__(self, row: int, column: int, board, state: SquareState = SquareState.EMPTY):
        self.row = row
        self.column = column
        self.board = board
        self._state = state
        self._initialize_button()

    def _initialize_button(self) -> None:
        """Initialize the button in the UI."""
        self.button = tk.Button(width=10, height=5, font=("arial", 40), text=self._state.value)
        self.button.bind(f"<Button-1>", self.user_click)
        self.button.grid(row=self.row, column=self.column)

    @property
    def state(self) -> SquareState:
        """Return the state of the square: 'X', 'O', or empty."""
        return self._state

    @state.setter
    def state(self, s: SquareState):
        """Set the state of the square ('X', 'O', or empty), and update the UI."""
        self._state = s
        self.button['text'] = s.value

    def user_click(self, event):
        """When the user clicks the square, update the square to an X and run the logic for AI's turn."""
        self.board.game.user_click(self)
