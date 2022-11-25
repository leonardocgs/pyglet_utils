from random import randint
from time import sleep
from board import Board
from player_new import Player

import pyglet
from game_state_sprite import GameStateSprite
from window import Window
from player_new import Player


class GameState:
    def __init__(self):
        self.board: Board = Board()
        self.players: list[Player] = [
            Player(self, "Você", True),
            Player(self, "Jogador 2"),
            Player(self, "Jogador 3"),
            Player(self, "Jogador 4"),
        ]
        self.fill_player_hands()
        self.turn: int = 0
        self.winner: Player = None
        self.accumulated_turn_skips: int = 0
        self.window = Window(
            height=1200, width=1200, fullscreen=True, title="Domino"
        )
        self.game_state_sprite = GameStateSprite(self.window)

    def create_initial_sprites(self):
        self.game_state_sprite.create_player_hand_sprite(self.my_player)
        self.game_state_sprite.place_player_sprite()

    @property
    def ongoing(self):
        return not self.winner

    @property
    def my_player(self) -> Player:
        return self.players[0]

    @property
    def current_player(self):
        return self.players[self.turn]

    @property
    def my_turn(self):
        return self.current_player.controllable

    @property
    def choose_tile_index(self) -> int:
        return self.game_state_sprite.choose_tile_index

    def fill_player_hands(self):
        tiles: list[list[int]] = []

        for i in range(0, 7):
            for j in range(i, 7):
                tiles.append([i, j]) if randint(0, 1) else tiles.append([j, i])

        for i in range(0, len(self.players)):
            player = self.players[i]
            player.hand = []
            for j in range(0, 7):
                if len(tiles):
                    player.hand.append(tiles.pop(randint(0, len(tiles) - 1)))

    def end_game(self):
        current_winner: Player = None

        for player in self.players:
            print(f"{player.name}: {player.points}")
            if not current_winner or player.points < current_winner.points:
                current_winner = player

        self.winner = current_winner

    def next_turn(self):
        if self.accumulated_turn_skips >= len(self.players):
            print("")
            print("Fechou o jogo! Hora de contar os pontos")
            self.end_game()

        if self.winner:
            return None

        self.turn = (self.turn + 1) % len(self.players)
        sleep(0.5)

        if not self.my_turn:
            current_player: Player = self.current_player

            if current_player.can_play:
                chosen_tile_index = current_player.pick_index()
                is_tile_on_front = current_player.pick_orientation(
                    chosen_tile_index
                )
                chosen_tile = current_player.hand[chosen_tile_index]

                current_player.play_tile(chosen_tile_index, is_tile_on_front)

                if not len(current_player.hand):
                    self.winner = current_player
                    return chosen_tile

                current_player.pass_turn()
                return chosen_tile

            else:
                current_player.pass_turn(True)

        return None
