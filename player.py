import pyglet

from tile import Tile
from window import Window


class Player:
    def __init__(self, tiles_in_hand: list["Tile"], window_width):
        self.hand = tiles_in_hand
        self.hand_batch = pyglet.graphics.Batch()
        for tile in self.hand:
            tile.batch = self.hand_batch

        self._window_width = window_width
        self._hand_position(50)

    def _hand_position(self, gap):
        tile_width = self.hand[0].width
        total_width = tile_width * len(self.hand)
        gap_total = len(self.hand) - 1
        surround_width = (
            self._window_width - total_width - (gap_total * gap)
        ) / 2
        for index, tile in enumerate(self.hand):
            if index == 0:
                tile.left = -surround_width
            else:
                tile.left_mid = self.hand[index - 1].right_mid
                tile.left = -gap
