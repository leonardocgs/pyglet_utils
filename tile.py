from pyglet.window.key import V

from game_object import GameObject
from RectGameObject import RectGameObject
from Vector2d import Vector2d


class Tile(GameObject):
    def __init__(
        self,
        position: "Vector2d",
        first_value,
        second_value,
        rotation=0,
        batch=None,
    ):
        self.img_path = (
            f"Dominoes/images/{first_value}{second_value}.png"
        )
        self.is_in_hand = False

        super().__init__(position, self.img_path, batch, rotation)
        self.first_value = first_value
        self.second_value = second_value

    def on_click(self):
        if self.is_in_hand:
            self.layer_rectangle = RectGameObject(
                Vector2d(self.x, self.y),
                self.width,
                self.height,
                rotation=self.rotation,
                batch=self.batch,
            )
