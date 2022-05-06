from .janggi_game import JanggiGame
import classes.constant as constant
from classes.grid import Grid
from classes.piece import Piece


def gridsToAction(origin: Grid, dest: Grid):
    (originRow, originCol) = origin
    (destRow, destCol) = dest

    originRow = 0 if originRow == constant.MAX_ROW else originRow
    destRow = 0 if destRow == constant.MAX_ROW else destRow

    return originRow * 1000 + originCol * 100 + destRow * 10 + destCol


def actionToGrids(action: int):
    originRow = action // 1000
    originCol = action // 100 % 10
    destRow = action // 10 % 10
    destCol = action % 10

    origin = Grid(originRow, originCol)
    dest = Grid(destRow, destCol)
    return origin, dest
