from classes import constants
from classes.grid import Grid


def grids_to_action(origin: Grid, dest: Grid):
    (origin_row, origin_col) = origin
    (dest_row, dest_col) = dest

    origin_row = 0 if origin_row == constants.max_row else origin_row
    dest_row = 0 if dest_row == constants.max_row else dest_row

    return origin_row * 1000 + origin_col * 100 + dest_row * 10 + dest_col


def action_to_grids(action: int):
    origin_row = action // 1000
    origin_col = action // 100 % 10
    dest_row = action // 10 % 10
    dest_col = action % 10

    origin = Grid(origin_row, origin_col)
    dest = Grid(dest_row, dest_col)
    return origin, dest
