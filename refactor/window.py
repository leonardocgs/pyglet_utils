import pyglet
from game_state import GameState


from game_object import game_object
from geometry import rectangle, vector2d


class Window(pyglet.window.Window):
    def __init__(
        self,
        game: GameState,
        width=None,
        height=None,
        title=None,
        resizable=True,
        fullscreen=False,
    ):
        super().__init__(width, height, title, resizable, fullscreen)
        self.game = game
        self.game_agents = []
        self.game_batch = pyglet

    def create_player_hand_sprites(self):
        for tile in self.game.my_player.hand:
            img_path = f"{tile[0]}{tile[1]}.png"
            tile_sprite = game_object.GameObject(
                img_path=img_path,
                position=vector2d.Vector2d(self.width // 2, self.height // 2),
            )

    def place_player_hand(self, gap):
        tile_width = self.player.hand[0].width
        total_width = tile_width * len(self.player.hand)
        gap_total = len(self.player.hand) - 1
        surround_width = (
            self.measurements["width"] - total_width - (gap_total * gap)
        ) / 2
        for index, tile in enumerate(self.player.hand):
            if index == 0:
                tile.left = -surround_width
            else:
                tile.left_mid = self.player.hand[index - 1].right_mid
                tile.left = -gap

    @property
    def rect(self):
        half_width = self.width / 2
        half_height = self.height / 2
        return rectangle.Rectangle(
            vector2d.Vector2d(half_width, half_height), self.width, self.height
        )
        try:
            pass
        except expression as identifier:
            pass

    @property
    def top(self):
        return self.rect.top

    @property
    def bottom(self):
        return self.rect.bottom

    @property
    def measurements(self):
        return {
            "width": self.width,
            "height": self.height,
            "top": self.top,
            "right": self.right,
            "bottom": self.bottom,
            "left": self.left,
        }

    @property
    def left(self):
        return self.rect.left

    @property
    def right(self):
        return self.rect.right

    def on_mouse_press(self, x, y, button, modifiers):
        for gameResource in self.gameResources:
            gameResource.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        for gameResource in self.gameResources:
            gameResource.on_mouse_release(x, y, button, modifiers)

    def on_draw(self):

        self.clear()
        for gameBatch in self.gameBatches:
            gameBatch.draw()
