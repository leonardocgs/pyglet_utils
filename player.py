import pyglet

from tile import Tile
from window import Window


class Player:
    def __init__(self):
        self._hand: list[Tile] = []

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, given_hand):
        self._hand = given_hand
