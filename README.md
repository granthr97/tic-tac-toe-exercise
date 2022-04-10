# Tic Tac Toe

## Overview
This is a simple Python implementation of Tic Tac Toe.

The `working_version` directory contains a completed, working version of Tic Tac Toe.

The `complete_me` directory contains an exact copy of `working_version`, with some code removed.
The goal here is to "fill in the blanks" by implementing empty methods in `working_version`.

## Setup
1. If you haven't already, `git clone` the `tic-tac-toe-exercise` project in the Terminal (Mac) or the Command Shell (Windows).
2. Navigate to the `tic-tac-toe-exercise` directory.
3. Run `git pull` to pull the latest version.
4. Run `git branch -B <your-username>` to create your own branch.
5. Run `git checkout <your-username>` to check out your branch.
6. (Optional) create and activate your virtual environment via `python -m venv venv` and `source venv/bin/activate`.
7. Run `pip install -r requirements.txt`.

Let me know if you have issues during any of these steps!

### Run the working version
Run `python working_version`.

### Run your version:
Run `python complete_me`.

### Run tests
Run `pytest working_version`.

## Development

Open up `complete_me` and implement all unimplemented methods.

- Begin with the `board.py` `Board` class and then complete the `game.py` `Game` class.
- Remember to run the tests! These help you determine when, where and why your code is breaking.
- Remember that arrays are 0-indexed. Each square here is in the format (row, column).

| --- | Column 0 | Column 1 | Column 2 |
| --- | --- | --- | --- |
| Row 0 | 0, 0| 0, 1| 0, 2 |
| Row 1 | 1, 0 | 1, 1 | 1, 2 |
| Row 2 | 2, 0 | 2, 1 | 2, 2 |

## Extra Reading
- Python design patterns
  - Python Classes and Objects: https://www.geeksforgeeks.org/python-classes-and-objects/
- Testing
  - pytest: https://docs.pytest.org/en/7.0.x/
  - unittest: https://docs.python.org/3/library/unittest.html
- Python UI
  - tkinter: https://docs.python.org/3/library/tkinter.html
