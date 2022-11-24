from window import Window
from . import tile


class GameStateSprite:
    def __init__(self, window: Window):
        self.window: Window = window
        self.front_available_position: list[tile.AvailablePosition] = [
            tile.AvailablePosition.RIGHT_MID,
            tile.AvailablePosition.TOP_MID,
            tile.AvailablePosition.LEFT_MID,
            tile.AvailablePosition.BOTTOM_MID,
        ]
        self.board_tile_deegree = [0, 90, 180, 270]
        self._front_index: int = 0
        self._back_index: int = 0
