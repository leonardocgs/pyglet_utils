import copy

from Vector2d import Vector2d


class Rectangle:
    """
    Classe que representa um retângulo.
    Seus pontos são represantados pela classe Vector2d,
    ou seja eles são representados como um vetor.
    A posição do retângulo está ancorada no ponto médio das
    diagonais do retângulo, ou seja, seu x e y correspondem
    aos x e y do desse ponto médio.
    Em particular essa classe permite mover o triângulo
    no plano cartesiano através dos :
        Vertices:
            top_left: Vértice superior esquerdo
            top_right: Vértice superior direito
            tottom_left: Vértice inferior esquerdo
            bottom_right: Vértice inferior direito
        Pontos médios:
            top_mid: Ponto médio do lado superior do retângulo.
            bottom_mid: Ponto médio do lado inferior do retângulo.
            left_mid: Ponto médio do lado esquerdo do retângulo.
            right_mid: Ponto médio lado direito do retângulo.
            center: Ponto médio das diagonais do retângulo.
        Posição:
            position: Ponto que representa a posição do triângulo no plano
            cartesiano.
        Abscissa e ordenada:
            x: Abcissa da posição do retângulo
            y :Ordenada da posição do retângulo

    :param middle_point: A posição do ponto médio das diagonais do retângulo.
    :type middle_point: "Vector2d"
    :param width: Largura do retângulo.
    :type width: int | float
    :param height: Altura do retângulo.
    :type height: int | float
    :param rotation: Ângulo de rotação do triângulo no sentido horário.
    :type rotation: int, optional
    """

    def __init__(
        self, middle_point: "Vector2d", width, height, rotation=0
    ):
        """
        Construtor da classe.


        :param middle_point: Posição do ponto médio das diagonais do retângulo.
        :type middle_point: "Vector2d"
        :param width: Largura do retângulo.
        :type width: int | float
        :param height: Altura do retângulo.
        :type height: int | float
        :param rotation: Ângulo de rotação do triângulo no sentido horário.
        :type rotation: int, optional
        """

        self._width = width
        self._height = height
        self._center = middle_point
        self.rotation = rotation

    @property
    def center(self) -> "Vector2d":
        """
        Getter para o centro do retângulo
        (Ponto médio das diagonais do retângulo)

        :return: Centro do retângulo.
        :rtype: "Vector2d"
        """
        return self._center

    @property
    def left_mid(self) -> "Vector2d":
        """
        Getter para o ponto médio do lado
        esquerdo do retângulo.

        :return: Ponto médio do lado esquerdo do retângulo.
        :rtype: "Vector2d"
        """
        return copy.copy(self._midleft)

    @property
    def right_mid(self) -> "Vector2d":
        """
        Getter para o ponto médio do lado
        direito do retângulo.

        :return: Ponto médio do lado direito do retângulo.
        :rtype: "Vector2d"
        """
        return copy.copy(self._mid_right)

    @property
    def top_mid(self) -> "Vector2d":
        """
        Getter para o ponto médio do lado
        superior do retângulo.

        :return: Ponto médio do lado superior do retângulo.
        :rtype: "Vector2d"
        """
        return copy.copy(self._midtop)

    @property
    def bottom_mid(self) -> "Vector2d":
        """
        Getter para o ponto médio do lado
        inferior do retângulo.

        :return: Ponto médio do lado inferor do retângulo.
        :rtype: "Vector2d"
        """
        return copy.copy(self._midbottom)

    @property
    def top_left(self) -> "Vector2d":
        """
        Getter para o vértice superior esquerdo.


        :return: Vértice superior esquerdo.
        :rtype: "Vector2d"
        """
        return copy.copy(self._topleft)

    @property
    def top_right(self) -> "Vector2d":
        """
        Getter para o vértice superior direito.


        :return: Vértice superior direito.
        :rtype: "Vector2d"
        """
        return copy.copy(self._topright)

    @property
    def bottom_left(self) -> "Vector2d":
        """
        Getter para o vértice inferior esquerdo.


        :return: Vértice inferior esquerdo.
        :rtype: "Vector2d"
        """
        return copy.copy(self._bottomleft)

    @property
    def bottom_right(self) -> "Vector2d":
        """
        Getter para o vértice inferior direito.


        :return: Vértice inferior direito.
        :rtype: "Vector2d"
        """
        return copy.copy(self._bottomright)

    @property
    def rotation(self) -> "Vector2d":
        return self._rotation

    @property
    def x(self) -> int:
        """
        Getter para a abscissa da posição do retângulo.

        :return: Abcissa da posição.
        :rtype: int
        """
        return self._center.x

    @property
    def y(self) -> int:
        """
        Getter para a ordenada da posição do retângulo.


        :return: Ordenada da posição do retângulo.
        :rtype: int
        """
        return self._center.y

    @property
    def left(self) -> int:
        """
        Getter para o x do lado esquerdo do retângulo.

        :return: X do lado esquerdo do retângulo.
        :rtype: int
        """
        return self.left_mid.x

    @property
    def right(self) -> int:
        """
        Getter para o x do lado direito do retângulo.

        :return: X do lado direito do retângulo.
        :rtype: int
        """
        return self.right_mid.x

    @property
    def top(self) -> int:
        """
        Getter para o y do lado superior do retângulo.

        :return: y do lado superior do retângulo.
        :rtype: int
        """
        return self.top_mid.y

    @property
    def bottom(self) -> int:
        """
        Getter para o y do lado inferior do retângulo.

        :return: y do lado inferior do retângulo.
        :rtype: int
        """
        return self.bottom_mid.y

    @property
    def position(self) -> "Vector2d":
        """
        Getter para a posição do retângulo.
        A posição do retângulo, por sua vez,
        está configurada como o seu centro.

        :return: Posição do retângulo
        :rtype: "Vector2d"
        """
        return self.center

    @property
    def width(self) -> int | float:
        """
        Getter para a largura do retângulo.

        :return: Largura do retângulo.
        :rtype: int | float
        """
        return self._width

    @property
    def height(self) -> int | float:
        """
        Getter para a altura do retângulo.

        :return: Altura do retângulo.
        :rtype: int | float
        """
        return self._height

    @position.setter
    def position(self, vector_position: "Vector2d"):
        """
        Setter para a posição do retângulo.


        :param vector_position: Novo posição no plano ocupado pelo retângulo.
        :type vector_position: "Vector2d"
        """
        self._center = vector_position

    @center.setter
    def center(self, new_center: "Vector2d"):
        """
        Setter para o centro do retângulo.
        Define a posição do retângulo a partir do centro.

        :param new_center: Nova posição do centro do retângulo.
        :type new_center: "Vector2d"
        """

        if isinstance(new_center, Vector2d):
            self._center = new_center
            self.__compute_mid_points()

    @left_mid.setter
    def left_mid(self, new_left_mid: "Vector2d"):
        """
        Setter para o ponto médio do lado esquerdo.
        Define a posição do retângulo a partir do ponto métido do lado
        esquerdo.

        :param new_left_mid: Nova posição do ponto médio do lado esquerdo.
        :type new_left_mid: "Vector2d"
        """
        if isinstance(new_left_mid, Vector2d):
            vector_to_add = new_left_mid.distance_vector(
                self._midleft
            )
            self._center += vector_to_add
            self.__compute_mid_points()

    @right_mid.setter
    def right_mid(self, new_right_mid: "Vector2d"):
        """
        Setter para o ponto médio do lado direito.
        Define a posição do retângulo a partir do ponto médio do lado direito
        do retângulo.

        :param new_right_mid: Nova posição do ponto médio do lado direito.
        :type new_right_mid: "Vector2d"
        """
        if isinstance(new_right_mid, Vector2d):
            vector_to_add = new_right_mid.distance_vector(
                self._mid_right
            )
            self._center += vector_to_add
            self.__compute_mid_points()

    @top_mid.setter
    def top_mid(self, new_top_mid: "Vector2d"):
        """
        Setter para o ponto médio do lado superior.
        Define a posição do retângulo a partir do ponto médio do lado
        superior do retângulo

        :param new_top_mid: Nova posição do ponto médio do lado superior.
        :type new_top_mid: "Vector2d"
        """
        if isinstance(new_top_mid, Vector2d):
            vector_to_add = new_top_mid.distance_vector(self._midtop)
            self._center += vector_to_add
            self.__compute_mid_points()

    @bottom_mid.setter
    def bottom_mid(self, new_bottom_mid: "Vector2d"):
        """
        Setter para o ponto médio do lado inferior.
        Define a posição do retângulo a partir do ponto médio do lado
        inferior do retângulo.

        :param new_bottom_mid: Nova posição do ponto médio do lado inferior.
        :type new_bottom_mid: "Vector2d"
        """
        if isinstance(new_bottom_mid, Vector2d):
            vector_to_add = new_bottom_mid.distance_vector(
                self._midbottom
            )
            self._center += vector_to_add
            self.__compute_mid_points()

    @top_left.setter
    def top_left(self, new_top_left: "Vector2d"):
        """
        Setter para o vértice superior esquerdo do retângulo.
        Define a posição do retângulo a partir do vértice superior
        esquerdo do retângulo.

        :param new_top_left: Nova posição do vértice superior esquerdo.
        :type new_top_left: "Vector2d"
        """
        if isinstance(new_top_left, Vector2d):
            vector_to_add = new_top_left.distance_vector(
                self._topleft
            )
            self._center += vector_to_add
            self.__compute_mid_points()

    @top_right.setter
    def top_right(self, new_top_right: "Vector2d"):
        """
        Setter para o vértice superior direito do retângulo.
        Define a posição do retângulo a partir do vértice superior direito.

        :param new_top_right: Nova posição do vértice superior direito.
        :type new_top_right: "Vector2d"
        """
        if isinstance(new_top_right, Vector2d):
            vector_to_add = new_top_right.distance_vector(
                self._topright
            )
            self._center += vector_to_add
            self.__compute_mid_points()

    @bottom_left.setter
    def bottom_left(self, new_bottom_left: "Vector2d"):
        """
        Setter para o vértice inferior esquerdo do retângulo.
        Define a posição do retângulo a partir do vértice inferior esquerdo.

        :param new_bottom_left: Nova posição do vértice inferior esquerdo.
        :type new_bottom_left: "Vector2d"
        """
        if isinstance(new_bottom_left, Vector2d):
            vector_to_add = new_bottom_left.distance_vector(
                self._bottomleft
            )
            self._center += vector_to_add
            self.__compute_mid_points()

    @bottom_right.setter
    def bottom_right(self, new_bottom_right: "Vector2d"):
        """
        Setter para o vértice inferior direito do retângulo.
        Define a posição do retângulo a partir do vértice inferior direito.

        :param new_bottom_right: Nova posição do vértice inferior direito.
        :type new_bottom_right: "Vector2d"
        """
        if isinstance(new_bottom_right, Vector2d):
            vector_to_add = new_bottom_right.distance_vector(
                self._bottomright
            )
            self._center += vector_to_add
            self.__compute_mid_points()

    @x.setter
    def x(self, new_x: int):
        """
        Setter para o x da posição do retângulo.

        :param new_x: Novo x da posição do retângulo.
        :type new_x: int
        """
        self._center.x = new_x
        self.__compute_mid_points()

    @y.setter
    def y(self, new_y: int):
        """
        Setter para o y da posição do retângulo.

        :param new_y: Novo y da posição do retângulo.
        :type new_y: int
        """
        self._center.y = new_y
        self.__compute_mid_points()

    @left.setter
    def left(self, distance: int):
        """
        Setter para a esquerda do retângulo.
        Desloca o retângulo à esquerda.
        Por exemplo: rec.left = 3
        desloca o retângulo 3 pontos a esquerda.

        :param distance: Quantidade de deslocamento à esquerda.
        :type distance: int
        """
        add_vector = Vector2d(distance, 0)
        self._left_mid -= add_vector

    @right.setter
    def right(self, distance: int):
        """
        Setter para a direita do retângulo.
        Desloca o retângulo à direita.
        Por exemplo: rec.right = 3
        desloca o retângulo 3 pontos a direita.

        :param distance: Quantidade de deslocamento à direita.
        :type distance: int
        """
        add_vector = Vector2d(distance, 0)
        self._right_mid += add_vector

    @top.setter
    def top(self, distance: int):
        """
        Setter para o top do retângulo.
        Desloca o retângulo para cima.
        Por exemplo: rec.top = 3
        desloca o retângulo 3 pontos para cima.

        :param distance: Quantidade de deslocamento para cima.
        :type distance: int
        """
        add_vector = Vector2d(0, distance)
        self._top_mid += add_vector

    @bottom.setter
    def bottom(self, distance: int):
        """
        Setter para o botom do retângulo.
        Desloca o retângulo para baixo.
        Por exemplo: rec.bottom = 3
        desloca o retângulo 3 pontos para baixo.

        :param distance: Quantidade de deslocamento para baixo.
        :type distance: int
        """
        add_vector = Vector2d(0, distance)
        self.bottom_mid -= add_vector

    @rotation.setter
    def rotation(self, angle: int):
        """
        Setter para rotation do retângulo.
        A rotação é feita no sentido horário.

        :param angle: Ângulo que desejamos rotacionar.
        :type angle: int
        """
        if angle == 90 or angle == 270:
            self.__height = self.width
            self.__width = self.height
        elif angle == 0 or angle == 180:
            self.__height = self.height
            self.__width = self.width
        self.__compute_mid_points()
        self._rotation = angle

    @width.setter
    def width(self, newwidth):
        """
        Setter para a largura do retângulo.

        :param newwidth: Nova largura do do retângulo.
        :type newwidth: int | float
        """
        self.__width = newwidth
        self._width = newwidth
        self.__compute_mid_points()

    @height.setter
    def height(self, new_height):
        """
        Setter para altura do retângulo.

        :param new_height: Nova altura do retângulo.
        :type new_height: int | float
        """
        self.__height = new_height
        self._height = new_height
        self.__compute_mid_points()

    def __compute_mid_points(self):
        """
        Calcula os pontos médios dos lados.

        """
        half_width: int = self.__width / 2
        half_height: int = self.__height / 2
        self._midleft = Vector2d(self.x - half_width, self.y)
        self._mid_right = Vector2d(self.x + half_width, self.y)
        self._midtop = Vector2d(self.x, self.y + half_height)
        self._midbottom = Vector2d(self.x, self.y - half_height)
        self.__compute_vertices()

    def __compute_vertices(self):
        """
        Calcula os vértice do retângulo.

        """
        half_width = self.__width / 2
        self._topright = Vector2d(
            self.top_mid.x + half_width, self.top_mid.y
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
        """
        Verifica se o ponto correspondente ao vetor é
        interior ao retângulo.

        :param vector: Vetor que representa o ponto para checar.
        :type vector: "Vector2d"
        """
        return (
            self.x >= self.left
            and self.y <= self.right
            and self.y >= self.bottom
            and self.y <= self.top
        )
