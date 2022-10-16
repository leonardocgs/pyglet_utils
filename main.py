import pyglet

from game import Game
from window import Window

if __name__ == "__main__":
    game_batch = pyglet.graphics.Batch()
    layer_batch = pyglet.graphics.Batch()
    batches = [game_batch, layer_batch]
    game = Game(game_batch, layer_batch)

    window = Window(
        gameBatches=batches,
        gameResources=game.game_tiles,
        width=1500,
        height=1500,
        title="Hello World",
    )
    game.window_measurements = window.measurements
    game.start_game()
    pyglet.clock.schedule(game.update, 1 / 60)
    pyglet.app.run()
