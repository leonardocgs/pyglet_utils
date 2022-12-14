from game_state import GameState
import pyglet
import random


class GameMaestro:
    def __init__(self) -> None:
        self.game: GameState = GameState()

    def start_game(self):
        self.game.create_initial_sprites()
        pyglet.clock.schedule_interval(self.current_game, 1 / 50)
        pyglet.app.run()

    def current_game(self, time) -> None:

        if self.game.ongoing:
            if self.game.my_turn and self.game.choose_tile_index >= 0:

                player = self.game.my_player

                if player.can_play:
                    print(self.game.choose_tile_index)

                    chosen: int = self.game.choose_tile_index
                    valid_orientations = (
                        self.game.board.valid_tile_orientations(
                            player.hand[chosen]
                        )
                    )

                    if len(valid_orientations):
                        front = (
                            valid_orientations[0]
                            if len(valid_orientations) == 1
                            or not len(self.game.board.state)
                            else bool(random.randrange(2))
                        )

                        print("--------------------")
                        print("")

                        played_tile = player.play_tile(chosen, front)

                        if played_tile:
                            player.pass_turn()
                        else:
                            print("UEPA! Você não pode jogar essa peça.")
                    else:
                        print("UEPA! Você não pode jogar essa peça.")

                else:
                    player.pass_turn(True)
        else:
            if self.game.winner is None:
                raise TypeError
            pyglet.text.Label(
                f"{self.game.winner.name} venceu!",
                font_name="Times New Roman",
                font_size=36,
                x=self.game.window.width // 2,
                y=self.game.window.width // 2,
                anchor_x="center",
                anchor_y="center",
                batch=self.game.window.game_batch,
            )
            # self.game.window.game_batch
            # print("FIM DE JOGO!!!")
            # print(f"{self.game.winner.name} venceu!")
