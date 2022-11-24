from window import Window
from game_object import game_object
from geometry import rectangle, vector2d


class BoardGraphic:
    def __init__(self, window: Window):
        self.window: Window = window

    def create_tile_sprite(first_tile_value: int, second_tile_value: int):
        img_path: str = f"{first_tile_value}{second_tile_value}.png"
        tile_sprite = game_object(str)
