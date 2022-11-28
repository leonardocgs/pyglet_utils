import pyglet


from geometry import rectangle, vector2d


from time import sleep
from game_object.game_object import GameObject


class Window(pyglet.window.Window):
    def __init__(
        self,
        width=None,
        height=None,
        title=None,
        resizable=True,
        fullscreen=False,
    ) -> None:
        super().__init__(width, height, title, resizable, fullscreen)
        self.game_batch: pyglet.graphics.Batch = pyglet.graphics.Batch()
        self.game_resources: list[GameObject] = []

    @property
    def rect(self):
        half_width = self.width / 2
        half_height = self.height / 2
        return rectangle.Rectangle(
            vector2d.Vector2d(half_width, half_height),
            self.width,
            self.height,
        )

    @property
    def measurements(self):
        return {
            "width": self.width,
            "height": self.height,
            "top": self.top,
            "right": self.right,
            "bottom": self.bottom,
            "left": self.left,
        }

    @property
    def top(self):
        return self.rect.top

    @property
    def bottom(self):
        return self.rect.bottom

    @property
    def center(self):
        return self.rect.center

    @property
    def left(self):
        return self.rect.left

    @property
    def right(self):
        return self.rect.right

    def on_mouse_press(self, x, y, button, modifiers):
        for game_resources in self.game_resources:
            game_resources.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        for game_resources in self.game_resources:
            game_resources.on_mouse_release(x, y, button, modifiers)

    def on_draw(self):
        self.clear()
        self.game_batch.draw()
