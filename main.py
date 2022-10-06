import pyglet

from game_object import GameObject
from Text import Text
from Vector2d import Vector2d

window = pyglet.window.Window(800, 500)

primeiro = gameObject = GameObject(
    Vector2d(window.width / 2, window.height / 2), "domino.jpg"
)

segundo = gameObject = GameObject(
    Vector2d(window.width / 2, window.height / 2), "domino.jpg"
)
print(primeiro.right)

text = Text("teste", Vector2d(window.width / 2, window.height / 2))


@window.event
def on_mouse_press(x, y, button, modifiers):
    text.on_mouse_press(x, y, button, modifiers)


@window.event
def on_draw():
    text.draw()


pyglet.app.run()
