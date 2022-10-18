from game_object import game_object
from geometry import vector2d
import pyglet
import os

window = pyglet.window.Window()
go = game_object.GameObject(img_path = "01.png",position =  vector2d.Vector2d( window.width//2, window.height//2))



@window.event
def on_draw():
    window.clear()
    go.draw()
pyglet.app.run()
