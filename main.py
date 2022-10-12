import pyglet

from game_object import GameObject
from RectGameObject import RectGameObject
from Vector2d import Vector2d
from window import Window

primeiro = gameObject = GameObject(Vector2d(400, 300), "domino.jpg")

segundo = gameObject = GameObject(Vector2d(400, 300), "domino.jpg")


segundo.scale = 0.25
primeiro.scale = 0.25
segundo.rotation = 90
retangulo = RectGameObject(
    primeiro.position,
    primeiro.width,
    primeiro.height,
    rotation=primeiro.rotation,
    color=(255, 255, 0),
)
retangulo._rectangle_shape.opacity = 100
segundo.right_mid = primeiro.left_mid
game_objects = [primeiro, segundo]
game_objects.append(retangulo)
if __name__ == "__main__":
    window = Window(
        game_objects, width=800, height=600, title="Hello World"
    )
    pyglet.app.run()
