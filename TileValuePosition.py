from enum import Enum


class TileValuePosition(Enum):
    TOP = "top"
    BOTTOM = "bottom"

    LEFT = "left"
    RIGHT = "right"

    def oposite(self):
        if self.name == "TOP":
            return TileValuePosition.BOTTOM
        elif self.name == "BOTTOM":
            return TileValuePosition.TOP
        elif self.name == "LEFT":
            return TileValuePosition.RIGHT
        elif self.name == "RIGHT":
            return TileValuePosition.LEFT
