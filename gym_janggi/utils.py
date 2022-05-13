from typing import Tuple
import numpy as np
import random

from . import constants
from janggi import (
    Board,
    Camp,
    Formation,
    Location,
    JanggiGame
)


def generate_random_game():
    """Generate a random Janggi game."""
    camp = Camp(random.randint(0, 1))
    cho_formation = Formation(random.randint(1, 4))
    han_formation = Formation(random.randint(1, 4))
    return JanggiGame(camp, cho_formation, han_formation)


def locations_to_action(origin: Location, dest: Location) -> int:
    """
    Convert a pair of Locations into action that belongs to an action space.

    Args:
        origin (Location): Original piece location.
        dest (Location): Destination location for the piece.

    Returns:
        int: action that represents the move from origin to dest.
    """
    (origin_row, origin_col) = origin
    (dest_row, dest_col) = dest

    return origin_row * 1000 + origin_col * 100 + dest_row * 10 + dest_col


def action_to_locations(action: int) -> Tuple[Location, Location]:
    """
    Convert an integer action to a tuple of Locations

    Args:
        action (int): integer action that represents a piece move.

    Returns:
        Tuple[Location, Location]: Pair of Locations that represent a piece move.
    """
    origin_row = action // 1000
    origin_col = action // 100 % 10
    dest_row = action // 10 % 10
    dest_col = action % 10

    origin = Location(origin_row, origin_col)
    dest = Location(dest_row, dest_col)
    return origin, dest


def board_to_obs(board: Board) -> np.array:
    """
    Convert Board into observation space in format of numpy.array.

    Args:
        board (Board): Current board state.

    Returns:
        np.array: Integer array converted from Janggi board.
    """
    int_board = [[None for i in range(constants.NUM_COLS)]
                 for j in range(constants.NUM_ROWS)]
    for row in range(constants.MIN_ROW, constants.MAX_ROW+1):
        for col in range(constants.MIN_COL, constants.MAX_COL+1):
            if board.get(row, col) is not None:
                int_board[row][col] = int(board.get(row, col))
            else:
                int_board[row][col] = 0
    return np.array(int_board)
