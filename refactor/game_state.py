from random import randint
from board import Board
from player_new import Player
from controllable_player import ControllablePlayer
from game_object.game_object import GameObject
from time import sleep

from game_state_sprite import GameStateSprite
from window import Window


class GameState:
    def __init__(self) -> None:
        self.board: Board = Board(self)
        self.players: list[Player] = [
            ControllablePlayer(self, "Jogador principal"),
            Player(self, "Jogador 2"),
            Player(self, "Jogador 3"),
            Player(self, "Jogador 4"),
        ]
        self.fill_player_hands()
        self.turn: int = 0
        self.winner: Player = None
        self.accumulated_turn_skips: int = 0
        self.window = Window(
            height=1200, width=2000, fullscreen=True, title="Domino"
        )
        self.game_state_sprite = GameStateSprite(self.window)
        self.board.board_graphic = self.game_state_sprite._board_graphic
        self.choose_tile_index: int = -1

    def create_initial_sprites(self):
        self.create_player_hand_sprite()
        self.board.board_graphic.place_player_hand(
            self.my_player.hand_sprites, 20
        )

    def create_player_hand_sprite(self) -> None:
        player_hand = self.my_player.hand
        for available_tile in player_hand:
            tile_sprite: GameObject = (
                self.board.board_graphic.create_tile_sprite(
                    first_tile_value=available_tile[0],
                    second_tile_value=available_tile[1],
                    rotation=90,
                    game_state=self,
                )
            )
            self.my_player.hand_sprites.append(tile_sprite)
        self.window.game_resources = self.my_player.hand_sprites

    @property
    def ongoing(self):
        return not self.winner

    @property
    def my_player(self) -> ControllablePlayer:
        if not isinstance(
            self.players[0],
            ControllablePlayer,
        ):
            raise TypeError()

        return self.players[0]

    @property
    def current_player(self):
        return self.players[self.turn]

    @property
    def my_turn(self):
        return isinstance(self.current_player, ControllablePlayer)

    def fill_player_hands(self) -> None:
        tiles: list[list[int]] = []

        for i in range(0, 7):
            for j in range(i, 7):
                tiles.append([i, j]) if randint(0, 1) else tiles.append(
                    [j, i]
                )

        for i in range(0, len(self.players)):
            player = self.players[i]
            player.hand = []
            for j in range(0, 7):
                if len(tiles):
                    player.hand.append(tiles.pop(randint(0, len(tiles) - 1)))

    def end_game(self) -> None:
        current_winner: Player = None

        for player in self.players:
            print(f"{player.name}: {player.points}")
            if not current_winner or player.points < current_winner.points:
                current_winner = player

        self.winner = current_winner

    def next_turn(self) -> None:
        if self.accumulated_turn_skips >= len(self.players):
            print("")
            print("Fechou o jogo! Hora de contar os pontos")
            self.end_game()

        if self.winner:
            return None

        self.turn = (self.turn + 1) % len(self.players)
        sleep(0.1)

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
