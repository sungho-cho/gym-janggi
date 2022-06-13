from typing import Tuple
import numpy as np

from gym_janggi.constants import (
    MIN_ROW, MAX_ROW, MIN_COL, MAX_COL,
    NUM_ROWS, NUM_COLS,
)
from janggi import (
    Board,
    Location,
)


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


def board_to_float_array(board: Board) -> np.array:
    """
    Convert Board into float numpy.array.

    Args:
        board (Board): Current board state.

    Returns:
        np.array: Float array converted from Janggi board.
    """
    float_board = np.full((NUM_ROWS, NUM_COLS), 0.0, dtype="float32")
    for row in range(MIN_ROW, MAX_ROW+1):
        for col in range(MIN_COL, MAX_COL+1):
            if board.get(row, col) is not None:
                float_board[row][col] = float(board.get(row, col))
            else:
                float_board[row][col] = 0.0
    return float_board
