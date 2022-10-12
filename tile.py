from game_object import GameObject
from Vector2d import Vector2d


class tiles(GameObject):
    def __init__(
        self,
        position: "Vector2d",
        first_value,
        second_value,
        img_path: str,
        rotation=0,
        batch=None,
    ):
        super().__init__(position, img_path, batch, rotation)
        self.first_value = first_value
        self.second_value = second_value
