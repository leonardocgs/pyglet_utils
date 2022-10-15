from operator import pos
from os import posix_fadvise
from pickle import TRUE

import pyglet

from game_object import GameObject
from Rectangle import Rectangle
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

    @property
    def available_position(self):
        if self.position == TileValuePosition.TOP:
            return ["top_mid", "left_top_quarter", "right_bottom_quarter"]
        elif self.position == TileValuePosition.BOTTOM:
            return [
                "bottom_mid",
                "right_bottom_quarter",
                "left_bottom_quarter",
            ]
        elif self.position == TileValuePosition.LEFT:
            return ["left_mid", "top_left_quarter", "bottom_left_quarter"]
        elif self.position == TileValuePosition.RIGHT:
            return ["right_mid", "top_right_quarter", "bottom_right_quarter"]


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
        self.not_taken_values = [
            self.first_value_info,
            self.second_value_info,
        ]
        self._repeat_value_flag = False

        if self.first_value == self.second_value:
            self._repeat_value_flag = True
        self.layer_batch = layer_batch
        self._test_rectangle = Rectangle(
            self.position, self.width, self.height, self.rotation
        )

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
        self._test_rectangle.rotation = rotation
        self.first_value_info.position = self.first_value_position

        self.second_value_info.position = self.second_value_position

    def change_hand_tile_property_after_move(
        self,
        deleteValue,
        board_tile: "Tile",
        window_measurements,
        board_tiles,
    ):

        self._delete_layer()
        self.change_position(
            board_tile, deleteValue, window_measurements, board_tiles
        )
        self.game_status = TileGameStatus.TABLE
        self.remove_available_value(deleteValue)
        self.is_clicked = False

    def remove_available_value(self, deleteValue):
        self.not_taken_values.remove(deleteValue)

    def change_board_tile_property_after_move(self, deleteValue):
        self.remove_available_value(deleteValue)

    def __repr__(self) -> str:
        return str((self.first_value, self.second_value))

    def checkes_if_overpass_bounds(self, window_measurements):
        if (
            self._test_rectangle.left
            < (window_measurements["left"] - self.width)
            or self.right > (window_measurements["right"] - self.width)
            or self._test_rectangle.top > window_measurements["top"] - 20
            or self._test_rectangle.bottom
            < window_measurements["bottom"] - 30
        ):
            return True
        return False

    def change_position(
        self,
        board_tile,
        board_tile_value_info,
        window_measurements,
        board_tiles,
    ):
        tile_value_index = self.not_taken_values.index(board_tile_value_info)
        tile_value_info = self.not_taken_values[tile_value_index]
        self.correct_tile(board_tile_value_info)
        is_possible_to_move = False
        colides = False

        rotation_value = 0
        if (
            tile_value_info.position is TileValuePosition.TOP
            or tile_value_info.position is TileValuePosition.BOTTOM
        ):
            rotation_value = 90
        elif (
            tile_value_info.position is TileValuePosition.LEFT
            or tile_value_info.position is TileValuePosition.RIGHT
        ):

            rotation_value = 0
        for available_position in tile_value_info.available_position:
            for (
                available_position_in_board_tile
            ) in board_tile_value_info.available_position:
                print(
                    available_position_in_board_tile,
                    available_position,
                )
                new_position = getattr(
                    board_tile, available_position_in_board_tile
                )
                setattr(
                    self._test_rectangle, available_position, new_position
                )
                for tile in board_tiles:
                    if tile.checks_if_another_object_colides(
                        self._test_rectangle
                    ):

                        colides = True
                        break
                if (
                    not self.checkes_if_overpass_bounds(window_measurements)
                    and not colides
                ):
                    is_possible_to_move = True
                    break
            if is_possible_to_move:
                ##self.position = self._test_rectangle.position
                self.x = self._test_rectangle.x
                self.y = self._test_rectangle.y
                return
                break
        if not is_possible_to_move:
            self._test_rectangle.x = self.x
            self._test_rectangle.y = self.y
            self.set_rotation(rotation_value)
            self.change_position(
                board_tile,
                board_tile_value_info,
                window_measurements,
                board_tiles,
            )

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
