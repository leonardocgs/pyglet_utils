import copy
import random

import pyglet

from player import Player
from tile import Tile
from TileGameStatus import TileGameStatus
from Vector2d import Vector2d


class Game:
    def __init__(self, window_width):
        self.game_tiles = []
        self.not_taken_tiles = []
        self.board_tiles = []
        self.player = Player()
        self.game_batch = pyglet.graphics.Batch()
        self.layer_batch = pyglet.graphics.Batch()
        self._window_width = window_width

    def create_tiles(self):
        for first_number in range(0, 7):
            for second_number in range(first_number, 7):
                new_tile = Tile(
                    Vector2d(0, 100), first_number, second_number
                )
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
            select_hand_tile = self.selected_hand_tile
            selected_board_tile = self.selected_board_tile
            if (
                select_hand_tile.first_value
                in selected_board_tile.values
                or select_hand_tile.second_value
                in selected_board_tile.values
            ):

                select_hand_tile.bottom_mid = (
                    selected_board_tile.top_mid
                )
                select_hand_tile.on_unclick()
                self.player.hand.remove(select_hand_tile)
                select_hand_tile.game_status = TileGameStatus.TABLE
                self.board_tiles.append(select_hand_tile)

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

        random_number = random.randint(
            0, len(self.not_taken_tiles) - 1
        )
        start_tile = self.not_taken_tiles[random_number]
        start_tile.x = 400
        start_tile.y = 400
        start_tile.batch = self.game_batch
        start_tile.game_status = TileGameStatus.TABLE
        self.board_tiles.append(start_tile)
        self.not_taken_tiles.remove(start_tile)

    def start_game(self):
        self.create_tiles()
        self.give_a_player_random_tiles()
        self.set_random_start_tile()
        self.hand_position(10)

    def hand_position(self, gap):
        tile_width = self.player.hand[0].width
        total_width = tile_width * len(self.player.hand)
        gap_total = len(self.player.hand) - 1
        surround_width = (
            self._window_width - total_width - (gap_total * gap)
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
