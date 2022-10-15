import pyglet

from tile import Tile
from Vector2d import Vector2d

window = pyglet.window.Window()
## create two tiles with position 100,100 and 200,200

tile1 = Tile(Vector2d(100, 100), 1, 2)
tile2 = Tile(Vector2d(200, 200), 3, 4)
tile2.set_rotation(90)
tile2.top_right_quarter = tile1.bottom_mid
# draw the tiles
@window.event
def on_draw():
    window.clear()
    tile1.draw()
    tile2.draw()


# run the application
pyglet.app.run()
