import pyglet

from game_object import GameObject
from Rectangle import Rectangle
from Vector2d import Vector2d


class Window(pyglet.window.Window):
    def __init__(
        self,
        gameBatches: list[pyglet.graphics.Batch],
        gameResources: list[GameObject],
        width=None,
        height=None,
        title=None,
        resizable=True,
        fullscreen=False,
    ):
        super().__init__(width, height, title, resizable, fullscreen)
        self.gameResources = gameResources
        self.gameBatches = gameBatches

    @property
    def rect(self):
        half_width = self.width / 2
        half_height = self.height / 2
        return Rectangle(
            Vector2d(half_width, half_height), self.width, self.height
        )

    @property
    def top(self):
        return self.rect.top

    @property
    def bottom(self):
        return self.rect.bottom

    @property
    def left(self):
        return self.rect.left

    @property
    def right(self):
        return self.rect.right

    def on_mouse_press(self, x, y, button, modifiers):
        for gameResource in self.gameResources:
            gameResource.on_mouse_press(x, y, button, modifiers)

    def on_draw(self):
        self.clear()
        for gameBatch in self.gameBatches:
            gameBatch.draw()
