import copy
import random

import pyglet

from player import Player
from tile import Tile
from TileGameStatus import TileGameStatus
from Vector2d import Vector2d


class Game:
    def __init__(
        self,
        game_batch,
        layer_batch,
        window_measurements=None,
    ):
        self.game_tiles: list[Tile] = []
        self.not_taken_tiles: list[Tile] = []
        self.board_tiles: list[Tile] = []
        self.player = Player()
        self.window_measurements = window_measurements
        self.game_batch = game_batch
        self.layer_batch = layer_batch

    def create_tiles(self):
        for first_number in range(0, 7):
            for second_number in range(first_number, 7):
                new_tile = Tile(Vector2d(0, 100), first_number, second_number)
                new_tile.left_mid = Vector2d(0, 100)
                new_tile.layer_batch = self.layer_batch
                self.game_tiles.append(new_tile)

        self.not_taken_tiles: list[Tile] = copy.copy(self.game_tiles)

    @property
    def is_hand_tile_selected(self):

        for tile in self.player.hand:
            if tile.is_clicked:
                return True
        return False

    @property
    def selected_hand_tile(self):
        for tile in self.player.hand:
            if tile.is_clicked:
                return tile

    @property
    def is_board_tile_selected(self):
        for tile in self.board_tiles:
            if tile.is_clicked:
                return True
        return False

    @property
    def selected_board_tile(self):
        for tile in self.board_tiles:
            if tile.is_clicked:
                return tile

    def player_move(self):
        if self.is_hand_tile_selected and self.is_board_tile_selected:
            select_hand_tile: "Tile" = self.selected_hand_tile
            selected_board_tile: "Tile" = self.selected_board_tile
            delete_item = None
            for values in selected_board_tile.not_taken_values:
                if (
                    select_hand_tile.first_value == values.value
                    or select_hand_tile.second_value == values.value
                ):
                    delete_item = values
                    select_hand_tile.change_hand_tile_property_after_move(
                        delete_item,
                        selected_board_tile,
                        self.window_measurements,
                        self.board_tiles,
                    )

                    selected_board_tile.change_board_tile_property_after_move(
                        delete_item
                    )
                    self.player.hand.remove(select_hand_tile)
                    self.board_tiles.append(select_hand_tile)
                    print(select_hand_tile.position)

                    break

    def give_a_player_random_tiles(self):
        random_numbers = random.sample(range(0, 28), 7)
        player_hand = []
        for number in random_numbers:
            player_hand.append(self.game_tiles[number])
            self.game_tiles[number].game_status = TileGameStatus.HAND
            self.not_taken_tiles.remove(self.game_tiles[number])
            self.game_tiles[number].batch = self.game_batch
        self.player.hand = player_hand

    def set_random_start_tile(self):

        random_number = random.randint(0, len(self.not_taken_tiles) - 1)
        start_tile = self.not_taken_tiles[random_number]
        start_tile.x = self.window_measurements["width"] / 2
        start_tile.y = self.window_measurements["height"] / 2
        start_tile.batch = self.game_batch
        start_tile.game_status = TileGameStatus.TABLE
        self.board_tiles.append(start_tile)
        self.not_taken_tiles.remove(start_tile)

    def start_game(self):
        self.create_tiles()
        self.give_a_player_random_tiles()
        self.hand_position(10)
        self.set_random_start_tile()

    def hand_position(self, gap):
        tile_width = self.player.hand[0].width
        total_width = tile_width * len(self.player.hand)
        gap_total = len(self.player.hand) - 1
        surround_width = (
            self.window_measurements["width"]
            - total_width
            - (gap_total * gap)
        ) / 2
        for index, tile in enumerate(self.player.hand):
            if index == 0:
                tile.left = -surround_width
            else:
                tile.left_mid = self.player.hand[index - 1].right_mid
                tile.left = -gap

    @property
    def batches(self):
        all_batches = [
            self.game_batch,
            self.layer_batch,
        ]
        return all_batches

    def set_another_tile_clicked_status(self):

        if self.is_hand_tile_selected:
            for tile in self.game_tiles:
                if tile is not self.selected_hand_tile:
                    tile.another_tile_was_clicked = True
        else:
            for tile in self.game_tiles:
                tile.another_tile_was_clicked = False

    def update(self, dt, x):
        self.set_another_tile_clicked_status()
        self.player_move()
