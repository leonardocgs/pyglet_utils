from game_object import GameObject
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

        super().__init__(position, self.img_path, batch, rotation)
        self.first_value = first_value
        self.second_value = second_value
