import pyglet

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
        layer_batch=None,
    ):
        self.img_path = (
            f"Dominoes/images/{first_value}{second_value}.png"
        )
        self.is_in_hand = False
        self.another_tile_was_clicked = False
        self.is_clicked = False

        super().__init__(position, self.img_path, batch, rotation)
        self.first_value = first_value
        self.second_value = second_value
        self.layer_batch = layer_batch

    def on_click(self):
        if self.is_in_hand and not self.another_tile_was_clicked:
            self.layer_rectangle = RectGameObject(
                Vector2d(self.x + 5, self.y + 5),
                self.width - 10,
                self.height - 10,
                color=(255, 255, 0),
                rotation=self.rotation,
                batch=self.layer_batch,
                opacity=150,
            )
            self.is_clicked = True

    def on_unclick(self):
        if self.is_in_hand and not self.another_tile_was_clicked:
            self.layer_rectangle.delete()
            self.is_clicked = False

    def __repr__(self) -> str:
        return str((self.first_value, self.second_value))
