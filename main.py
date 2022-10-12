import pyglet

from game_object import GameObject
from player import Player
from RectGameObject import RectGameObject
from tile import Tile
from Vector2d import Vector2d
from window import Window

tile2 = Tile(Vector2d(0, 100), 4, 4)
tile3 = Tile(Vector2d(0, 100), 5, 5)
tile4 = Tile(Vector2d(0, 100), 0, 5)
tile5 = Tile(Vector2d(0, 100), 0, 6)
tile6 = Tile(Vector2d(0, 100), 2, 6)
tile7 = Tile(Vector2d(0, 100), 3, 6)
lista = [tile2, tile3, tile4, tile5, tile6, tile7]

if __name__ == "__main__":
    player = Player(lista, 2000)
    window = Window(
        [player.hand_batch],
        lista,
        width=2000,
        height=2000,
        title="Hello World",
    )
    pyglet.app.run()
