from game_state import GameState

game = GameState()

print("Início do jogo")

while game.ongoing:
    print("")
    print(f"TABULEIRO: {game.board.state}")
    print("")

    if game.my_turn:
        player = game.my_player

        if player.can_play:
            print("----- SUA VEZ! -----")

            for other_player in [
            ControllablePlayer(self, "Você"),
            Player(self, "Jogador 2"),
            Player(self, "Jogador 3"),
            Player(self, "Jogador 4"),
        ]:
                tileAmountStr = ""

                for tile in other_player.hand:
                    tileAmountStr += "/"

                if other_player.controllable:
                    print(f"Você: {tileAmountStr}")
                else:
                    print(f"{other_player.name}: {tileAmountStr}")

            print("")
            print(player.hand)
            chosen = int(input(f"Escolha uma peça {player.valid_indexes}: "))
            valid_orientations = game.board.valid_tile_orientations(
                player.hand[chosen]
            )

            if len(valid_orientations):
                front = (
                    valid_orientations[0]
                    if len(valid_orientations) == 1
                    or not len(game.board.state)
                    else bool(
                        int(input(f"1 - jogar na frente, 0 - jogar atrás: "))
                    )
                )

                print("--------------------")
                print("")

                played_tile = player.play_tile(chosen, front)

                if played_tile:
                    player.pass_turn()
                else:
                    print(f"UEPA! Você não pode jogar essa peça.")
            else:
                print(f"UEPA! Você não pode jogar essa peça.")

        else:
            player.pass_turn(True)

print("")
print("FIM DE JOGO!!!")
print(f"{game.winner.name} venceu!")
