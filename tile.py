import copy

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
        self.first_value_info = TileValue(self.first_value, self.first_value_position)
        self.second_value_info = TileValue(self.second_value, self.second_value_position)
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
        if self.game_status is TileGameStatus.HAND and not self.another_tile_was_clicked:
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

    def correct_tile(self, value_tile):

        requested_value = self.return_request_available_value(value_tile)
        if requested_value.position is value_tile.position:
            self.set_rotation(90)

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
        self.change_position(board_tile, deleteValue, window_measurements, board_tiles)
        self.game_status = TileGameStatus.TABLE
        self.is_clicked = False

    def remove_available_value(self, deleteValue):
        self.not_taken_values.remove(deleteValue)

    def change_board_tile_property_after_move(self, deleteValue):
        self.remove_available_value(deleteValue)

    def __repr__(self) -> str:
        return str((self.first_value, self.second_value))

    def checkes_if_overpass_bounds(self, window_measurements):
        if (
            self._test_rectangle.left < (window_measurements["left"])
            or self.right > (window_measurements["right"])
            or self._test_rectangle.top > window_measurements["top"]
            or self._test_rectangle.bottom < window_measurements["bottom"] + self.height
        ):
            return True
        return False

    def return_request_available_value(self, another_value):
        for value in self.not_taken_values:
            if value.value == another_value.value:
                return value

    def return_request_available_value_index(self, another_value):
        for index, value in enumerate(self.not_taken_values):
            if value.value == another_value:
                return index

    def change_position(
        self,
        board_tile,
        board_tile_value_info,
        window_measurements,
        board_tiles,
    ):
        self_tile_value_info = self.return_request_available_value(board_tile_value_info)
        self.correct_tile(board_tile_value_info)

        for (
            self_tile_value_info_available_position
        ) in self_tile_value_info.available_position:
            for (
                board_tile_value_info_available_position
            ) in board_tile_value_info.available_position:
                copy_board_tiles = copy.copy(board_tiles)
                copy_board_tiles.remove(board_tile)
                rect_position_to_move = getattr(
                    board_tile, board_tile_value_info_available_position
                )
                setattr(
                    self._test_rectangle,
                    self_tile_value_info_available_position,
                    rect_position_to_move,
                )
                if self.checkes_if_overpass_bounds(window_measurements):
                    break
                if (
                    not self.checks_if_test_rectangle_collids_with_a_object_inside_list(
                        board_tiles
                    )
                    and not self.checkes_if_overpass_bounds(window_measurements)
                    and not self.checks_if_test_rectangle_collids_with_a_object_inside_list_including_all_points(
                        copy_board_tiles
                    )
                ):
                    self.x = self._test_rectangle.x
                    self.y = self._test_rectangle.y
                    return

        self.set_rotation(self.rotation + 90)
        self.change_position(
            board_tile, board_tile_value_info, window_measurements, board_tiles
        )

    def reset_test_rectangle(self):
        self._test_rectangle.x = self.x
        self._test_rectangle.y = self.y
        self._test_rectangle.rotation = self.rotation

    def checks_if_test_rectangle_collids_with_a_object_inside_list(
        self,
        list_of_objects,
    ):
        for object in list_of_objects:
            if self._test_rectangle.checks_if_another_object_colides(object):
                return True
        return False

    def checks_if_test_rectangle_collids_with_a_object_inside_list_including_all_points(
        self,
        list_of_objects,
    ):
        for object in list_of_objects:
            if self._test_rectangle.checks_if_another_object_colides_including_all_points(
                object
            ):
                return True
        return False

    def remove_available_value(self, deleteValue):
        for value_info in self.not_taken_values:
            if value_info.value == deleteValue.value:
                self.not_taken_values.remove(value_info)

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
