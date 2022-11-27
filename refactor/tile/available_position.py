from enum import Enum


class AvailablePosition(Enum):
    TOP_MID = "top_mid"
    TOP_RIGHT = "top_right"
    TOP_LEFT = "top_left"
    TOP_RIGHT_QUARTER = "top_right_quarter"
    TOP_LEFT_QUARTER = "top_left_quarter"
    BOTTOM_MID = "bottom_mid"
    BOTTOM_RIGHT = "bottom_right"
    BOTTOM_LEFT = "bottom_left"
    BOTTOM_RIGHT_QUARTER = "bottom_right_quarter"
    BOTTOM_LEFT_QUARTER = "bottom_left_quarter"
    RIGHT_MID = "right_mid"
    RIGHT_TOP_QUARTER = "right_top_quarter"
    RIGHT_BOTTOM_QUARTER = "right_bottom_quarter"
    LEFT_MID = "left_mid"
    LEFT_TOP_QUARTER = "left_top_quarter"
    LEFT_BOTTOM_QUARTER = "left_bottom_quarter"

    @property
    def oposite_position(self):
        if self is AvailablePosition.TOP_MID:
            return AvailablePosition.BOTTOM_MID
        elif self is AvailablePosition.BOTTOM_MID:
            return AvailablePosition.TOP_MID
        elif self is AvailablePosition.LEFT_MID:
            return AvailablePosition.RIGHT_MID
        elif self is AvailablePosition.RIGHT_MID:
            return AvailablePosition.LEFT_MID

    @property
    def transition_position(self):
        if self is AvailablePosition.TOP_MID:
            return AvailablePosition.BOTTOM_RIGHT_QUARTER
        elif self is AvailablePosition.BOTTOM_MID:
            return AvailablePosition.TOP_MID
        elif self is AvailablePosition.LEFT_MID:
            return AvailablePosition.RIGHT_MID
