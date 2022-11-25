import pyglet

from game_state_sprite import GameStateSprite
from window import Window

from game_state import GameState

if __name__ == "__main__":
    window = Window(height=1200, width=1200, fullscreen=True, title="Domino")
    game = GameState()
    game_state_sprite = GameStateSprite(window)
    game_state_sprite.create_player_hand_sprite(game.my_player)
    game_state_sprite.place_player_sprite()
    pyglet.app.run()
