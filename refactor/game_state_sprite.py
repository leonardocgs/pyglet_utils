from window import Window

from geometry import vector2d
from board_graphic import BoardGraphic
from game_object import game_object


class GameStateSprite:
    def __init__(self, window: Window):
        self.window: Window = window
        self._board_graphic = BoardGraphic(window=self.window)
        self.choose_tile_index: int = -1

    def create_tile_sprite(
        self,
        first_tile_value: int,
        second_tile_value: int,
        rotation: int,
    ) -> game_object.GameObject:
        img_path: str = f"{first_tile_value}{second_tile_value}.png"
        tile_sprite = game_object.GameObject(
            vector2d.Vector2d(0, 62.5),
            img_path=img_path,
            rotation=rotation,
            batch=self.window.game_batch,
            game_state_sprite=self,
        )
        return tile_sprite

    def create_player_hand_sprite(self, player: Player):
        player_hand = player.hand
        player_hand_sprites: list[game_object.GameObject] = []
        for available_tile in player_hand:
            tile_sprite: game_object.GameObject = self.create_tile_sprite(
                first_tile_value=available_tile[0],
                second_tile_value=available_tile[1],
                rotation=90,
            )
            player_hand_sprites.append(tile_sprite)
        self.window.game_resources = player_hand_sprites
        self.player_hand_sprites: list[
            game_object.GameObject
        ] = player_hand_sprites

    def place_player_sprite(self):
        self._board_graphic.place_player_hand(self.player_hand_sprites, 10)
