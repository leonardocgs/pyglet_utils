from window import Window
from tile.available_position import AvailablePosition
from player_new import Player

from board_graphic import BoardGraphic
from game_object import game_object


class GameStateSprite:
    def __init__(self, window: Window):
        self.window: Window = window
        self.front_available_position: list[AvailablePosition] = [
            AvailablePosition.RIGHT_MID,
            AvailablePosition.TOP_MID,
            AvailablePosition.LEFT_MID,
            AvailablePosition.BOTTOM_MID,
        ]
        self.board_tile_deegree = [0, 90, 180, 270]
        self._front_index: int = 0
        self._back_index: int = 0
        self._board_graphic = BoardGraphic(window=self.window)

    def create_player_hand_sprite(self, player: Player):
        player_hand = player.hand
        player_hand_sprites: list[game_object.GameObject] = []
        for available_tile in player_hand:
            tile_sprite: game_object.GameObject = (
                self._board_graphic.create_tile_sprite(
                    first_tile_value=available_tile[0],
                    second_tile_value=available_tile[1],
                    rotation=90,
                    batch=self.window.game_batch,
                )
            )
            player_hand_sprites.append(tile_sprite)
        self.player_hand_sprites: list[
            game_object.GameObject
        ] = player_hand_sprites

    def place_player_sprite(self):
        self._board_graphic.place_player_hand(self.player_hand_sprites, 10)
