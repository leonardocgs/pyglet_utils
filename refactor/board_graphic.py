from window import Window
from game_object import game_object
from geometry import rectangle, vector2d
from geometry.vector2d import Vector2d

from tile.available_position import AvailablePosition
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_state import GameState


class BoardGraphic:
    def __init__(self, window: Window):
        self.window: Window = window
        self.tiles: list[game_object.GameObject] = []
        self.front_available_position: list[AvailablePosition] = [
            AvailablePosition.RIGHT_MID,
            AvailablePosition.TOP_MID,
            AvailablePosition.LEFT_MID,
            AvailablePosition.BOTTOM_MID,
        ]
        self.back_available_position: list[AvailablePosition] = [
            AvailablePosition.LEFT_MID,
            AvailablePosition.TOP_MID,
            AvailablePosition.RIGHT_MID,
            AvailablePosition.BOTTOM_MID,
        ]
        self.board_tile_deegree = [0, 90, 180, 270]
        self._front_index: int = 0
        self._back_index: int = 0
        self._is_first_move = True

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

    def get_tile_property_position(self, front: bool) -> AvailablePosition:
        if front:
            return self.front_available_position[self._front_index]
        else:
            return self.back_available_position[self._back_index]

    def insert_tile_into_array(
        self, tile: game_object.GameObject, front: bool
    ) -> None:
        if front:
            self.tiles.append(tile)
        else:
            self.tiles.insert(0, tile)

    def get_tile_sprite(self, front: bool) -> game_object.GameObject:
        if front:
            return self.tiles[len(self.tiles) - 1]
        else:
            return self.tiles[0]

    def place_on_board(
        self, tile_sprite: game_object.GameObject, front: bool = True
    ):
        if self._is_first_move:
            tile_sprite.position = self.window.center
            self._is_first_move = False
            self.tiles.append(tile_sprite)
        else:
            tile_available_position: AvailablePosition = (
                self.get_tile_property_position(front)
            )

            print(
                "Here we go ",
                tile_available_position.value,
                tile_available_position.oposite_position.value,
            )
            board_tile_sprite: game_object.GameObject = self.get_tile_sprite(
                front
            )
            board_tile_position: Vector2d = getattr(
                board_tile_sprite,
                tile_available_position.oposite_position.value,
            )

            setattr(
                tile_sprite,
                tile_available_position.value,
                board_tile_position,
            )
            self.insert_tile_into_array(tile_sprite, front)

    def create_tile_sprite(
        self,
        first_tile_value: int,
        second_tile_value: int,
        rotation: int,
        game_state: "GameState",
    ) -> game_object.GameObject:
        img_path: str = f"{first_tile_value}{second_tile_value}.png"
        tile_sprite = game_object.GameObject(
            Vector2d(0, 62.5),
            img_path=img_path,
            rotation=rotation,
            batch=self.window.game_batch,
            game_state=game_state,
        )
        return tile_sprite

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
