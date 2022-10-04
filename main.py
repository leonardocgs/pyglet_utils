import pyglet

from game_object import GameObject
from Vector2d import Vector2d

window = pyglet.window.Window(800, 500)

primeiro = gameObject = GameObject(
    Vector2d(window.width / 2, window.height / 2), "domino.jpg"
)

segundo = gameObject = GameObject(
    Vector2d(window.width / 2, window.height / 2), "domino.jpg"
)
primeiro.scale = 0.25
segundo.scale = 0.25
segundo.mid_bottom = Vector2d(segundo.x, 250)
segundo.mid_top = Vector2d(segundo.x, 250)
primeiro.rotation = 90
primeiro.mid_right = segundo.mid_left
print(segundo.left)
print(segundo.mid_bottom)


@window.event
def on_draw():
    segundo.draw()
    primeiro.draw()


pyglet.app.run()
