import copy

from Vector2d import Vector2d


class Rectangle:
    def __init__(
        self, middle_point: "Vector2d", width, height, rotation=0
    ):

        self._width = width
        self._height = height
        self._center = middle_point
        self.rotation = rotation

    @property
    def center(self):
        return self._center

    @property
    def left_mid(self):
        return copy.copy(self._midleft)

    @property
    def right_mid(self):
        return copy.copy(self._mid_right)

    @property
    def top_mid(self):
        return copy.copy(self._midtop)

    @property
    def mid_bottom(self):
        return copy.copy(self._midbottom)

    @property
    def top_left(self):
        return copy.copy(self._topleft)

    @property
    def top_right(self):
        return copy.copy(self._topright)

    @property
    def bottom_left(self):
        return copy.copy(self._bottomleft)

    @property
    def bottom_right(self):
        return copy.copy(self._bottomright)

    @property
    def rotation(self):
        return self._rotation

    @property
    def x(self):
        return self._center.x

    @property
    def y(self):
        return self._center.y

    @property
    def left(self):
        return self.left_mid.x

    @property
    def right(self):
        return self.right_mid.x

    @property
    def top(self):
        return self.top_mid.y

    @property
    def bottom(self):
        return self.mid_bottom.y

    @property
    def position(self):
        return self.center

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @position.setter
    def position(self, vector_position: "Vector2d"):
        self._center = vector_position

    @center.setter
    def center(self, new_center: "Vector2d"):
        if isinstance(new_center, Vector2d):
            self._center = new_center
            self.__compute_points()

    @left_mid.setter
    def left_mid(self, new_left_mid: "Vector2d"):
        if isinstance(new_left_mid, Vector2d):
            vector_to_add = new_left_mid.distance_vector(
                self._midleft
            )
            self._center += vector_to_add
            self.__compute_points()

    @right_mid.setter
    def right_mid(self, new_right_mid: "Vector2d"):
        if isinstance(new_right_mid, Vector2d):
            vector_to_add = new_right_mid.distance_vector(
                self._mid_right
            )
            self._center += vector_to_add
            self.__compute_points()

    @top_mid.setter
    def top_mid(self, new_top_mid: "Vector2d"):
        if isinstance(new_top_mid, Vector2d):
            vector_to_add = new_top_mid.distance_vector(self._midtop)
            self._center += vector_to_add
            self.__compute_points()

    @mid_bottom.setter
    def mid_bottom(self, new_mid_bottom: "Vector2d"):
        if isinstance(new_mid_bottom, Vector2d):
            vector_to_add = new_mid_bottom.distance_vector(
                self._midbottom
            )
            self._center += vector_to_add
            self.__compute_points()

    @top_left.setter
    def top_left(self, top_left: "Vector2d"):
        if isinstance(top_left, Vector2d):
            vector_to_add = top_left.distance_vector(self._topleft)
            self._center += vector_to_add
            self.__compute_points()

    @top_right.setter
    def top_right(self, top_right: "Vector2d"):
        if isinstance(top_right, Vector2d):
            vector_to_add = top_right.distance_vector(self._topright)
            self._center += vector_to_add
            self.__compute_points()

    @bottom_left.setter
    def bottom_left(self, bottom_left: "Vector2d"):
        if isinstance(bottom_left, Vector2d):
            vector_to_add = bottom_left.distance_vector(
                self._bottomleft
            )
            self._center += vector_to_add
            self.__compute_points()

    @bottom_right.setter
    def bottom_right(self, bottom_right: "Vector2d"):
        if isinstance(bottom_right, Vector2d):
            vector_to_add = bottom_right.distance_vector(
                self._bottomright
            )
            self._center += vector_to_add
            self.__compute_points()

    @x.setter
    def x(self, new_x: int):
        self._center.x = new_x
        self.__compute_points()

    @y.setter
    def y(self, new_y: int):
        self._center.y = new_y
        self.__compute_points()

    @left.setter
    def left(self, distance: int):
        add_vector = Vector2d(distance, 0)
        self._left_mid -= add_vector

    @right.setter
    def right(self, distance: int):
        add_vector = Vector2d(distance, 0)
        self._right_mid += add_vector

    @top.setter
    def top(self, distance: int):
        add_vector = Vector2d(0, distance)
        self._top_mid += add_vector

    @bottom.setter
    def bottom(self, distance: int):
        add_vector = Vector2d(0, distance)
        self.mid_bottom -= add_vector

    @rotation.setter
    def rotation(self, angle: int):
        if angle == 90 or angle == 270:
            self.__height = self.width
            self.__width = self.height
        elif angle == 0 or angle == 180:
            self.__height = self.height
            self.__width = self.width
        self.__compute_points()
        self._rotation = angle

    @width.setter
    def width(self, newwidth):
        self.__width = newwidth
        self._width = newwidth
        self.__compute_points()

    @height.setter
    def height(self, new_height):
        self.__height = new_height
        self._height = new_height
        self.__compute_points()

    def __compute_points(self):
        half_width: int = self.__width / 2
        half_height: int = self.__height / 2
        self._midleft = Vector2d(self.x - half_width, self.y)
        self._mid_right = Vector2d(self.x + half_width, self.y)
        self._midtop = Vector2d(self.x, self.y + half_height)
        self._midbottom = Vector2d(self.x, self.y - half_height)
        self.__compute_auxiliar_points()

    def __compute_auxiliar_points(self):
        half_width = self.__width / 2
        self._topright = Vector2d(
            self._midtop.x + half_width, self._midtop.y
        )
        self._topleft = Vector2d(
            self._midtop.x - half_width, self._midtop.y
        )
        self._bottomright = Vector2d(
            self._midbottom.x + half_width, self._midbottom.y
        )
        self._bottomleft = Vector2d(
            self._midbottom.x - half_width, self._midbottom.y
        )

    def is_interior_point(self, vector: "Vector2d"):
        return (
            self.x >= self.left
            and self.y <= self.right
            and self.y >= self.bottom
            and self.y <= self.top
        )
