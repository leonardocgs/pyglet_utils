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

segundo.scale = 0.25
primeiro.scale = 0.25
segundo.rotation = 90 
primeiro.bottom_mid 
@window.event
def on_mouse_press(x, y, button, modifiers):
    text.on_mouse_press(x, y, button, modifiers)

    segundo.on_mouse_press(x, y, button, modifiers)

@window.event
def on_draw():
    segundo.draw()
    primeiro.draw()
pyglet.app.run()
