from pickle import FALSE
from game_state import GameState

game = GameState()
print(game.board.state)

game.board.add_tile([3, 6])
print(game.board.state)

game.board.add_tile([3, 6], False)
print(game.board.state)

game.board.add_tile([1, 6], False)
print(game.board.state)

game.board.add_tile([4, 4])
print(game.board.state)