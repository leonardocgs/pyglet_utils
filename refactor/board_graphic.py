from window import Window
import pyglet
from game_object import game_object
from geometry import rectangle, vector2d


class BoardGraphic:
    def __init__(self, window: Window):
        self.window: Window = window

    def create_tile_sprite(
        self,
        first_tile_value: int,
        second_tile_value: int,
        rotation: int,
        batch: pyglet.graphics.Batch,
        game_state_sprite,
    ) -> game_object.GameObject:
        img_path: str = f"{first_tile_value}{second_tile_value}.png"
        tile_sprite = game_object.GameObject(
            vector2d.Vector2d(0, 62.5),
            img_path=img_path,
            rotation=rotation,
            batch=batch,
            game_state_sprite=game_state_sprite,
        )
        return tile_sprite

    def checks_if_overpass_bounds(
        self, new_position: vector2d.Vector2d, rotation: int
    ) -> bool:
        test_rectangle = rectangle.Rectangle(
            new_position, 125, 65, rotation=rotation
        )
        if (
            test_rectangle.right > self.window.right - 200
            or test_rectangle.left < self.window.left + 200
            or test_rectangle.top > self.window.top - 200
            or test_rectangle.bottom < self.window.bottom + 200
        ):
            return True
        return False

    def place_player_hand(
        self, player_sprites: list[game_object.GameObject], gap
    ):
        tile_width: float | int = player_sprites[0].height
        total_width = tile_width * len(player_sprites)
        gap_total = len(player_sprites) - 1
        surround_width = (
            self.window.width - total_width - (gap_total * gap)
        ) / 2
        for index, tile in enumerate(player_sprites):
            if index == 0:
                tile.left = -surround_width
            else:
                tile.left_mid = player_sprites[index - 1].right_mid
                tile.left = -gap
