from game_state import GameState
import pyglet


class GameMaestro:
    def __init__(self):
        self.game: GameState = GameState()

    def start_game(self):
        self.game.create_initial_sprites()
        pyglet.clock.schedule_interval(self.current_game, 1 / 60)
        pyglet.app.run()

    def current_game(self, time):

        is_first_move = True
        if self.game.my_turn and self.game.choose_tile_index > 0:

            player = self.game.my_player

            if player.can_play:
                print(self.game.choose_tile_index)

                chosen: int = self.game.choose_tile_index
                valid_orientations = self.game.board.valid_tile_orientations(
                    player.hand[chosen]
                )
                print(chosen)

                if len(valid_orientations):
                    front = (
                        valid_orientations[0]
                        if len(valid_orientations) == 1
                        or not len(self.game.board.state)
                        else bool(
                            int(
                                input(
                                    f"1 - jogar na frente, 0 - jogar atrás: "
                                )
                            )
                        )
                    )

                    print("--------------------")
                    print("")

                    played_tile = player.play_tile(
                        chosen, front, is_first_move
                    )

                    if played_tile:
                        is_first_move = False
                        player.pass_turn()
                    else:
                        print(f"UEPA! Você não pode jogar essa peça.")
                else:
                    print(f"UEPA! Você não pode jogar essa peça.")

            else:
                player.pass_turn(True)