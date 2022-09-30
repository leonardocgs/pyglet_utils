import pyglet
from game_object import GameObject
from Vector2d import Vector2d
window = pyglet.window.Window(800,500)

primeiro = gameObject = GameObject(Vector2d(window.width/2,window.height/2),"domino.jpg")

segundo = gameObject = GameObject(Vector2d(window.width/2,window.height/2),"domino.jpg")
primeiro.scale = 0.25
segundo.scale = 0.25
segundo.rotation = 90
segundo.mid_bottom = primeiro.mid_top
@window.event
def on_draw():
    primeiro.draw()
    segundo.draw()
pyglet.app.run()
