from random import randint
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_state import GameState


class Player:
    def __init__(self, game: "GameState", name: str):
        self.hand: list[list[int]] = []
        self.game: "GameState" = game
        self.name: str = name

    def play_tile(
        self, index: int, front: bool = True, is_first_move: bool = False
    ):
        tile = self.hand[index]

        if self.game.board.add_tile(tile, front):
            self.hand.pop(index)

            tile_orientation_str = "na frente" if front else "atrás"
            print(f"{self.name} jogou {tile_orientation_str}: {tile}")

            return tile
        else:
            print(
                f"{self.name} não pode jogar {tile_orientation_str}: {tile}"
            )

            return None

    def pass_turn(self, skipped: bool = False):
        if skipped:
            self.game.accumulated_turn_skips += 1
            print(f"{self.name} passou!")
        else:
            self.game.accumulated_turn_skips = 0

        self.game.next_turn()

    def pick_index(self):
        valid_indexes = self.valid_indexes
        return valid_indexes[randint(0, len(valid_indexes) - 1)]

    def pick_orientation(self, index: int):
        orientation = randint(0, 1) == 1

        if self.game.board.can_add_tile(self.hand[index], orientation):
            return orientation
        else:
            return not orientation

    @property
    def points(self):
        sum = 0
        for tile in self.hand:
            sum += tile[0] + tile[1]
        return sum

    @property
    def can_play(self):
        return len(self.valid_tiles)

    @property
    def valid_tiles(self) -> list[list[int]]:
        valid_tiles: list[list[int]] = []
        for tile in self.hand:
            if self.game.board.can_add_tile(
                tile, True
            ) or self.game.board.can_add_tile(tile, False):
                valid_tiles.append(tile)
        return valid_tiles

    @property
    def valid_indexes(self) -> list[int]:
        valid_indexes: list[int] = []
        index = 0
        for tile in self.hand:
            if self.game.board.can_add_tile(
                tile, True
            ) or self.game.board.can_add_tile(tile, False):
                valid_indexes.append(index)
            index += 1
        return valid_indexes
