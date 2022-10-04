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
segundo.bottom_mid = Vector2d(350, 0)
print(segundo.x)
primeiro.left_mid = Vector2d(0, segundo.y)

primeiro.y = segundo.y
primeiro.rotation = 90
primeiro.center = Vector2d(400, 250)
segundo.center = Vector2d(100, 300)
primeiro.right_mid = Vector2d(segundo.x, segundo.y)
segundo.x = primeiro.x
primeiro.y = segundo.y
segundo.x = 400
segundo.y = 250
segundo.bottom_mid = Vector2d(segundo.width // 2, 0)
primeiro.bottom_right = Vector2d(800, 0)

print(primeiro.right)


@window.event
def on_draw():
    primeiro.draw()


pyglet.app.run()
