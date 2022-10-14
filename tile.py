from operator import pos

import pyglet

from game_object import GameObject
from RectGameObject import RectGameObject
from TileGameStatus import TileGameStatus
from TileValuePosition import TileValuePosition
from Vector2d import Vector2d


class TileValue:
    def __init__(self, value, position):
        self.value = value
        self.position = position

    def __eq__(self, another) -> bool:
        return self.value == another.value


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
        self.img_path = f"Dominoes/images/{first_value}{second_value}.png"
        self.another_tile_was_clicked = False
        self.is_clicked = False

        self.game_status = TileGameStatus.NOT_IN_THE_GAME
        super().__init__(position, self.img_path, batch, rotation)
        self.first_value = first_value
        self.second_value = second_value
        self.first_value_info = TileValue(
            self.first_value, self.first_value_position
        )
        self.second_value_info = TileValue(
            self.second_value, self.second_value_position
        )
        self.not_taken_values = [self.first_value_info, self.second_value_info]
        self._repeat_value_flag = False

        if self.first_value == self.second_value:
            self._repeat_value_flag = True
        self.layer_batch = layer_batch

    def on_click(self):
        if (
            self.game_status is TileGameStatus.HAND
            and not self.another_tile_was_clicked
        ):
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
        elif self.game_status is TileGameStatus.TABLE:
            self.is_clicked = True

    def on_unclick(self):
        if self.game_status is TileGameStatus.HAND and self.is_clicked:
            self._delete_layer()
            self.is_clicked = False
        elif self.game_status is TileGameStatus.TABLE:
            self.is_clicked = False

    def _delete_layer(self):
        self.layer_rectangle.delete()

    def correct_tile(
        self,
        value_tile,
    ):
        tile_index = self.not_taken_values.index(value_tile)
        if self.not_taken_values[tile_index].position is value_tile.position:
            self.set_rotation(180)

    def set_rotation(self, rotation):
        self.rotation = rotation
        self.first_value_info.position = self.first_value_position

        self.second_value_info.position = self.second_value_position

    def change_hand_tile_property_after_move(
        self, deleteValue, board_tile: "Tile"
    ):

        self.game_status = TileGameStatus.TABLE
        self._delete_layer()
        self.is_clicked = False
        self.correct_tile(deleteValue)
        self.change_position(board_tile, deleteValue)

        self.remove_available_value(deleteValue)

    def remove_available_value(self, deleteValue):
        self.not_taken_values.remove(deleteValue)

    def change_board_tile_property_after_move(self, deleteValue):
        self.remove_available_value(deleteValue)

    def __repr__(self) -> str:
        return str((self.first_value, self.second_value))

    def change_position(self, board_tile, deleteValue):
        tile_value_index = self.not_taken_values.index(deleteValue)
        tile_value_info = self.not_taken_values[tile_value_index]
        if tile_value_info.position is TileValuePosition.TOP:
            self.top_mid = board_tile.bottom_mid
        elif tile_value_info.position is TileValuePosition.BOTTOM:
            self.bottom_mid = board_tile.top_mid

    @property
    def first_value_position(self):
        if self.rotation == 0:
            return TileValuePosition.TOP
        elif self.rotation == 90:
            return TileValuePosition.RIGHT
        elif self.rotation == 180:
            return TileValuePosition.BOTTOM
        elif self.rotation == 270:
            return TileValuePosition.LEFT

    @property
    def second_value_position(self):
        if self.rotation == 0:
            return TileValuePosition.BOTTOM
        elif self.rotation == 90:
            return TileValuePosition.LEFT
        elif self.rotation == 180:
            return TileValuePosition.TOP
        elif self.rotation == 270:
            return TileValuePosition.RIGHT
