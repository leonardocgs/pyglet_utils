import pyglet

from game_object import GameObject
from player import Player
from RectGameObject import RectGameObject
from tile import Tile
from Vector2d import Vector2d
from window import Window

tile2 = Tile(Vector2d(100, 100), 4, 4)
tile3 = Tile(Vector2d(200, 100), 5, 5)
lista = list()
lista.append(tile2)
lista.append(tile3)
player = Player([tile2, tile3])

if __name__ == "__main__":
    window = Window(
        [player.hand_batch],
        lista,
        width=800,
        height=600,
        title="Hello World",
    )
    pyglet.app.run()
