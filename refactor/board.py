class Board:
    def __init__(self):
        self.state: list[list[int]] = []

    def can_add_tile(self, tile: list[int], front: bool = True):
        if len(self.state):
            if front:
                last = self.state[len(self.state) - 1]
                if tile[0] == last[1]:
                    return 1
                elif tile[1] == last[1]:
                    return -1
                else:
                    return 0
            else:
                first = self.state[0]
                if tile[0] == first[0]:
                    return -1
                elif tile[1] == first[0]:
                    return 1
                else:
                    return 0
        else:
            return 1

    def valid_tile_orientations(self, tile: list[int]):
        list = []
        if self.can_add_tile(tile, True):
            list.append(True)
        if self.can_add_tile(tile, False):
            list.append(False)
        return list

    def add_tile(self, tile: list[int], front: bool = True):
        can_add = self.can_add_tile(tile, front)

        if can_add:
            flipped_tile = tile if can_add > 0 else tile[::-1]
            if front:
                self.state.append(flipped_tile)
            else:
                self.state.insert(0, flipped_tile)

        return can_add
