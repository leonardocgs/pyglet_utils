from player_new import Player
from typing import TYPE_CHECKING
from game_object.game_object import GameObject

if TYPE_CHECKING:
    from game_state import GameState


class ControllablePlayer(Player):
    def __init__(self, game: "GameState", name: str):
        self.hand_sprites: list[GameObject] = []
        super().__init__(game, name)

    def play_tile(
        self, index: int, front: bool = True, is_first_move: bool = False
    ):
        parent_play_tile = super().play_tile(index, front, is_first_move)
        if parent_play_tile:
            self.hand_sprites[index].delete()
            self.hand_sprites.pop(index)
        return parent_play_tile
