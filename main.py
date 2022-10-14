import pyglet

from game import Game
from game_object import GameObject
from player import Player
from RectGameObject import RectGameObject
from tile import Tile
from Vector2d import Vector2d
from window import Window

if __name__ == "__main__":
    game = Game(1500)
    game.start_game()
    window = Window(
        gameBatches=game.batches,
        gameResources=game.game_tiles,
        width=1500,
        height=1500,
        title="Hello World",
    )
    pyglet.clock.schedule(game.update, 1 / 120)
    pyglet.app.run()
