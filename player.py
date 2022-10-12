import pyglet

from tile import Tile


class Player:
    def __init__(self, tiles_in_hand: list["Tile"]):
        self.tiles_in_hand = tiles_in_hand
        self.hand_batch = pyglet.graphics.Batch()
        for tile in self.tiles_in_hand:
            tile.batch = self.hand_batch
