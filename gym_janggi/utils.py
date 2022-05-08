import numpy as np
import random

import constants
from classes.board import Board
from classes.camp import Camp
from classes.formation import Formation
from classes.grid import Grid
from janggi_game import JanggiGame


def generate_random_game():
    camp = Camp(random.randint(0, 1))
    cho_formation = Formation(random.randint(1, 4))
    han_formation = Formation(random.randint(1, 4))
    return JanggiGame(camp, cho_formation, han_formation)


def grids_to_action(origin: Grid, dest: Grid):
    (origin_row, origin_col) = origin
    (dest_row, dest_col) = dest

    origin_row = 0 if origin_row == constants.MAX_ROW else origin_row
    dest_row = 0 if dest_row == constants.MAX_ROW else dest_row

    return origin_row * 1000 + origin_col * 100 + dest_row * 10 + dest_col


def action_to_grids(action: int):
    origin_row = action // 1000
    origin_col = action // 100 % 10
    dest_row = action // 10 % 10
    dest_col = action % 10

    origin = Grid(origin_row, origin_col)
    dest = Grid(dest_row, dest_col)
    return origin, dest


def board_to_obs(board: Board):
    int_board = [[None for i in range(constants.NUM_COLS+1)]
                 for j in range(constants.NUM_ROWS+1)]
    for row in range(constants.MIN_ROW, constants.MAX_ROW+1):
        for col in range(constants.MIN_COL, constants.MAX_COL+1):
            if board.get(row, col):
                try:
                    int_board[row][col] = int(board.get(row, col))
                except Exception as e:
                    print(f"{e} ({row},{col}) {board.get(row,col).camp}")
    return np.array(int_board)
