import pyglet

from game_object import GameObject
from Vector2d import Vector2d
from window import Window

primeiro = gameObject = GameObject(Vector2d(400, 300), "domino.jpg")

segundo = gameObject = GameObject(Vector2d(400, 300), "domino.jpg")


segundo.scale = 0.25
primeiro.scale = 0.25
segundo.rotation = 90
segundo.right_mid = primeiro.left_mid
game_objects = [primeiro, segundo]
if __name__ == "__main__":
    window = Window(
        game_objects, width=800, height=600, title="Hello World"
    )
    pyglet.app.run()
