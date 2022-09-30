import pyglet
from game_object import GameObject
from Vector2d import Vector2d
window = pyglet.window.Window(800,500)

primeiro = gameObject = GameObject(Vector2d(window.width/2,window.height/2),"domino.jpg")


primeiro.scale = 0.5
primeiro.top_right = Vector2d(800,500)
primeiro.left = 800 - primeiro.width
primeiro.right = 800-primeiro.width
primeiro.bottom = 500-primeiro.height
primeiro.top = 500 - primeiro.height
@window.event
def on_draw():
    primeiro.draw()
pyglet.app.run()
