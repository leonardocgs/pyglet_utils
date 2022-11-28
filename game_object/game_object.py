import pyglet
from pyglet.window import mouse
from typing import TYPE_CHECKING
from geometry import vector2d, rectangle

if TYPE_CHECKING:
    from game_state import GameState


class GameObject:
    """
        Classe para ser utilizada para manipular sprite do pyglet.
        Seus pontos são represantados pela classe vector2d.Vector2d,
        ou seja eles são representados como um vetor.
        A posição do GameObject está ancorada no ponto médio das
        diagonais do GameObject, ou seja, seu x e y correspondem
    90aos x e y do desse ponto médio.
        Em particular essa classe permite mover o triângulo
        no plano cartesiano através dos :
            Vertices:
                top_left: Vértice superior esquerdo
                top_right: Vértice superior direito
                tottom_left: Vértice inferior esquerdo
                bottom_right: Vértice inferior direito
            Pontos médios:
                top_mid: Ponto médio do lado superior do GameObject.
                bottom_mid: Ponto médio do lado inferior do GameObject.
                left_mid: Ponto médio do lado esquerdo do GameObject.
                right_mid: Ponto médio lado direito do GameObject.
                center: Ponto médio das diagonais do GameObject.
            Posição:
                position: Ponto que representa a posição do triângulo no plano
                cartesiano.
            Abscissa e ordenada:
                x: Abcissa da posição do GameObject
                y :Ordenada da posição do GameObject
            Mover em relação a uma direção:
                left: Move à esquerda
                right: Move à direita
                top: Move para cima
                bottom :move para baixo
        :param position: Posição inicial do GameObject
        :type position: "vector2d.Vector2d"
        :param img_path: path da imagem do GameObject
        :type img_path: str
        :param batch: Batch do GameObject
        :type batch: [TODO:type], optional
        :param rotation: Ângulo de rotação do triângulo no sentido horário.
        :type rotation: int, optional
    """

    def __init__(
        self,
        position: "vector2d.Vector2d",
        game_state: "GameState",
        img_path: str,
        batch=None,
        rotation=0,
    ):
        """
        Construtor do GameObject


        :param position: Posição inicial do GameObject
        :type position: "vector2d.Vector2d"
        :param img_path: path da imagem do GameObject
        :type img_path: str
        :param batch: Batch do GameObject
        :type batch: [TODO:type], optional
        :param rotation: Ângulo de rotação do triângulo no sentido horário.
        :type rotation: int, optional
        """
        self._create_image(img_path)
        self._width = self._image.width
        self._height = self._image.height
        self._rotation = rotation
        self._create_rectangle(position)
        self._create_sprite(batch)
        self.position = position
        self.rotation = self._rotation
        self.was_clicked: bool = False
        self.game_state: GameState = game_state

    def _create_image(self, img_path):
        pyglet.resource.path = ["./Dominoes/images"]
        pyglet.resource.reindex()
        self._image = pyglet.resource.image(img_path)
        self._image.anchor_x = self._image.width // 2
        self._image.anchor_y = self._image.height // 2

    def _create_rectangle(self, position):
        self._rectangle = rectangle.Rectangle(
            position,
            self._width,
            self._height,
            self._rotation,
        )

    def _create_sprite(self, batch):
        self._sprite = pyglet.sprite.Sprite(
            self._image,
            x=self._rectangle.x,
            y=self._rectangle.y,
            batch=batch,
        )

    def connect_GameObject_with_rectangle(self):
        """
        Conecta a classe de sprite do pyglet com a classe rectangle.Rectangle.
        Isso é feito associando as respectivas abscissas e ordenadas
        das duas classes.

        """
        self._sprite.x = self._rectangle.x
        self._sprite.y = self._rectangle.y

    def checks_if_another_object_colides(self, rect_to_check):
        """
        Verifica se o GameObject colide com outro GameObject ou retângulo.

        :param other: Outro GameObject
        :type other: GameObject
        """

        return self._rectangle.checks_if_another_object_colides(rect_to_check)

    def __eq__(self, other):
        """
        Sobrecarga do operador de igualdade.

        :param other: Outro GameObject
        :type other: GameObject
        """
        return self.x == other.x and self.y == other.y

    @property
    def batch(self):
        return self._sprite.batch

    @batch.setter
    def batch(self, batch: "pyglet.graphics.Batch"):
        self._sprite.batch = batch

    @property
    def center(self):
        """
        Getter para o centro do GameObject
        (Ponto médio das diagonais do GameObject)

        :return: Centro do GameObject.
        :rtype: "vector2d.Vector2d"
        """
        return self._rectangle.center

    @center.setter
    def center(self, new_center: "vector2d.Vector2d"):
        """
        Setter para o centro do GameObject.
        Define a posição do GameObject a partir do centro.

        :param new_center: Nova posição do centro do GameObject.
        :type new_center: "vector2d.Vector2d"
        """
        self._rectangle.center = new_center
        self.connect_GameObject_with_rectangle()

    def draw(self):
        """
        Reescreve o método draw do pyglet.sprite.Sprite.

        """
        self._sprite.draw()

    def delete(self):
        """
        Método para deletar o GameObject.

        """
        self._sprite.delete()

    def is_interior_point(self, vector: "vector2d.Vector2d"):
        """
        Verifica se o ponto correspondente ao vetor passado
        como argumento é interior ao GameObject.

        :param vector: Vetor que representa o ponto para checar.
        :type vector: "vector2d.Vector2d"
        """
        return self._rectangle.is_interior_point(vector)

    @property
    def left_mid(self):
        """
        Getter para o ponto médio do lado
        esquerdo do GameObject.

        :return: Ponto médio do lado esquerdo do GameObject.
        :rtype: "vector2d.Vector2d"
        """
        return self._rectangle.left_mid

    @left_mid.setter
    def left_mid(self, new_left_mid: "vector2d.Vector2d"):
        """
        Setter para o ponto médio do lado esquerdo.
        Define a posição do GameObject a partir do ponto métido do lado
        esquerdo.

        :param new_left_mid: Nova posição do ponto médio do lado esquerdo.
        :type new_left_mid: "vector2d.Vector2d"
        """
        self._rectangle.left_mid = new_left_mid
        self.connect_GameObject_with_rectangle()

    @property
    def right_mid(self):
        """
        Getter para o ponto médio do lado
        direito do GameObject.

        :return: Ponto médio do lado direito do GameObject.
        :rtype: "vector2d.Vector2d"
        """
        return self._rectangle.right_mid

    @right_mid.setter
    def right_mid(self, new_right_mid: "vector2d.Vector2d"):
        """
        Setter para o ponto médio do lado direito.
        Define a posição do GameObject a partir do ponto médio do lado direito
        do GameObject.

        :param new_right_mid: Nova posição do ponto médio do lado direito.
        :type new_right_mid: "vector2d.Vector2d"
        """
        self._rectangle.right_mid = new_right_mid
        self.connect_GameObject_with_rectangle()

    @property
    def top_mid(self):
        """
        Getter para o ponto médio do lado
        superior do GameObject.

        :return: Ponto médio do lado superior do GameObject.
        :rtype: "vector2d.Vector2d"
        """
        return self._rectangle.top_mid

    @top_mid.setter
    def top_mid(self, new_top_mid: "vector2d.Vector2d"):
        """
        Setter para o ponto médio do lado superior.
        Define a posição do GameObject a partir do ponto médio do lado
        superior do GameObject

        :param new_top_mid: Nova posição do ponto médio do lado superior.
        :type new_top_mid: "vector2d.Vector2d"
        """
        self._rectangle.top_mid = new_top_mid
        self.connect_GameObject_with_rectangle()

    @property
    def right_top_quarter(self):
        """
        Getter para o ponto médio do segmento formado pelo vertice superior direito e o ponto médio do lado direito do GameObject.
        return: Ponto médio do segmento formado pelo vertice superior direito e o ponto médio do lado direito do GameObject.
        rtype: "vector2d.Vector2d"
        """
        return self._rectangle.right_top_quarter

    @right_top_quarter.setter
    def right_top_quarter(self, new_top_quarter):
        """
        Setter para o ponto médio do segmento formado pelo vertice superior direito e o ponto médio do lado direito do GameObject.
        return: Ponto médio do segmento formado pelo vertice superior direito e o ponto médio do lado direito do GameObject.
        rtype: "vector2d.Vector2d"
        """
        self._rectangle.right_top_quarter = new_top_quarter
        self.connect_GameObject_with_rectangle()

    @property
    def right_bottom_quarter(self):
        """
        Getter para o ponto médio do segmento formado pelo vertice inferior direito e o ponto médio do lado direito do GameObject.
        return: Ponto médio do segmento formado pelo vertice inferior direito e o ponto médio do lado direito do GameObject.
        rtype: "vector2d.Vector2d"
        """
        return self._rectangle.right_bottom_quarter

    @right_bottom_quarter.setter
    def right_bottom_quarter(self, new_bottom_quarter):
        """
        Setter para o ponto médio do segmento formado pelo vertice inferior direito e o ponto médio do lado direito do GameObject.
        return: Ponto médio do segmento formado pelo vertice inferior direito e o ponto médio do lado direito do GameObject.
        rtype: "vector2d.Vector2d"
        """
        self._rectangle.right_bottom_quarter = new_bottom_quarter
        self.connect_GameObject_with_rectangle()

    @property
    def left_top_quarter(self):
        """
        Getter para o ponto médio do segmento formado pelo vertice superior esquerdo e o ponto médio do lado esquerdo do GameObject.
        return: Ponto médio do segmento formado pelo vertice superior esquerdo e o ponto médio do lado esquerdo do GameObject.
        rtype: "vector2d.Vector2d"
        """
        return self._rectangle.left_top_quarter

    @left_top_quarter.setter
    def left_top_quarter(self, new_top_quarter):
        """
        Setter para o ponto médio do segmento formado pelo vertice superior esquerdo e o ponto médio do lado esquerdo do GameObject.
        return: Ponto médio do segmento formado pelo vertice superior esquerdo e o ponto médio do lado esquerdo do GameObject.
        rtype: "vector2d.Vector2d"
        """
        self._rectangle.left_top_quarter = new_top_quarter
        self.connect_GameObject_with_rectangle()

    @property
    def left_bottom_quarter(self):
        """
        Getter para o ponto médio do segmento formado pelo vertice inferior esquerdo e o ponto médio do lado esquerdo do GameObject.
        return: Ponto médio do segmento formado pelo vertice inferior esquerdo e o ponto médio do lado esquerdo do GameObject.
        rtype: "vector2d.Vector2d"
        """
        return self._rectangle.left_bottom_quarter

    @left_bottom_quarter.setter
    def left_bottom_quarter(self, new_bottom_quarter):
        """
        Setter para o ponto médio do segmento formado pelo vertice inferior esquerdo e o ponto médio do lado esquerdo do GameObject.
        return: Ponto médio do segmento formado pelo vertice inferior esquerdo e o ponto médio do lado esquerdo do GameObject.
        rtype: "vector2d.Vector2d"
        """
        self._rectangle.left_bottom_quarter = new_bottom_quarter
        self.connect_GameObject_with_rectangle()

    @property
    def top_left_quarter(self):
        """
        Getter para o ponto médio do segmento formado pelo vertice superior esquerdo e o ponto médio do lado superior do GameObject.
        return: Ponto médio do segmento formado pelo vertice superior esquerdo e o ponto médio do lado superior do GameObject.
        rtype: "vector2d.Vector2d"
        """
        return self._rectangle.top_left_quarter

    @top_left_quarter.setter
    def top_left_quarter(self, new_top_quarter):
        """
        Setter para o ponto médio do segmento formado pelo vertice superior esquerdo e o ponto médio do lado superior do GameObject.
        return: Ponto médio do segmento formado pelo vertice superior esquerdo e o ponto médio do lado superior do GameObject.
        rtype: "vector2d.Vector2d"
        """
        self._rectangle.top_left_quarter = new_top_quarter
        self.connect_GameObject_with_rectangle()

    @property
    def top_right_quarter(self):
        """
        Getter para o ponto médio do segmento formado pelo vertice superior direito e o ponto médio do lado superior do GameObject.
        return: Ponto médio do segmento formado pelo vertice superior direito e o ponto médio do lado superior do GameObject.
        rtype: "vector2d.Vector2d"
        """
        return self._rectangle.top_right_quarter

    @top_right_quarter.setter
    def top_right_quarter(self, new_top_quarter):
        """
        Setter para o ponto médio do segmento formado pelo vertice superior direito e o ponto médio do lado superior do GameObject.
        return: Ponto médio do segmento formado pelo vertice superior direito e o ponto médio do lado superior do GameObject.
        rtype: "vector2d.Vector2d"
        """
        self._rectangle.top_right_quarter = new_top_quarter
        self.connect_GameObject_with_rectangle()

    @property
    def bottom_left_quarter(self):
        """
        Getter para o ponto médio do segmento formado pelo vertice inferior esquerdo e o ponto médio do lado inferior do GameObject.
        return: Ponto médio do segmento formado pelo vertice inferior esquerdo e o ponto médio do lado inferior do GameObject.
        rtype: "vector2d.Vector2d"
        """
        return self._rectangle.bottom_left_quarter

    @bottom_left_quarter.setter
    def bottom_left_quarter(self, new_bottom_quarter):
        """
        Setter para o ponto médio do segmento formado pelo vertice inferior esquerdo e o ponto médio do lado inferior do GameObject.
        return: Ponto médio do segmento formado pelo vertice inferior esquerdo e o ponto médio do lado inferior do GameObject.
        rtype: "vector2d.Vector2d"
        """
        self._rectangle.bottom_left_quarter = new_bottom_quarter
        self.connect_GameObject_with_rectangle()

    @property
    def bottom_right_quarter(self):
        """
        Getter para o ponto médio do segmento formado pelo vertice inferior direito e o ponto médio do lado inferior do GameObject.
        return: Ponto médio do segmento formado pelo vertice inferior direito e o ponto médio do lado inferior do GameObject.
        rtype: "vector2d.Vector2d"
        """
        return self._rectangle.bottom_right_quarter

    @bottom_right_quarter.setter
    def bottom_right_quarter(self, new_bottom_quarter):
        """
        Setter para o ponto médio do segmento formado pelo vertice inferior direito e o ponto médio do lado inferior do GameObject.
        return: Ponto médio do segmento formado pelo vertice inferior direito e o ponto médio do lado inferior do GameObject.
        rtype: "vector2d.Vector2d"
        """
        self._rectangle.bottom_right_quarter = new_bottom_quarter
        self.connect_GameObject_with_rectangle()

    @property
    def bottom_mid(self):
        """
        Getter para o ponto médio do lado
        inferior do GameObject.

        :return: Ponto médio do lado inferor do GameObject.
        :rtype: "vector2d.Vector2d"
        """
        return self._rectangle.bottom_mid

    @bottom_mid.setter
    def bottom_mid(self, new_bottom_mid: "vector2d.Vector2d"):
        """
        Setter para o ponto médio do lado inferior.
        Define a posição do GameObject a partir do ponto médio do lado
        inferior do GameObject.

        :param new_bottom_mid: Nova posição do ponto médio do lado inferior.
        :type new_bottom_mid: "vector2d.Vector2d"
        """
        self._rectangle.bottom_mid = new_bottom_mid
        self.connect_GameObject_with_rectangle()

    @property
    def top_left(self):
        """
        Getter para o vértice superior esquerdo.


        :return: Vértice superior esquerdo.
        :rtype: "vector2d.Vector2d"
        """
        return self._rectangle.top_left

    @top_left.setter
    def top_left(self, new_top_left: "vector2d.Vector2d"):
        """
        Setter para o vértice superior esquerdo do GameObject.
        Define a posição do GameObject a partir do vértice superior
        esquerdo do GameObject.

        :param new_top_left: Nova posição do vértice superior esquerdo.
        :type new_top_left: "vector2d.Vector2d"
        """
        self._rectangle.top_left = new_top_left
        self.connect_GameObject_with_rectangle()

    @property
    def top_right(self):
        """
        Getter para o vértice superior direito.


        :return: Vértice superior direito.
        :rtype: "vector2d.Vector2d"
        """
        return self._rectangle.top_right

    @top_right.setter
    def top_right(self, new_top_right: "vector2d.Vector2d"):
        """
        Setter para o vértice superior direito do GameObject.
        Define a posição do GameObject a partir do vértice superior direito.

        :param new_top_right: Nova posição do vértice superior direito.
        :type new_top_right: "vector2d.Vector2d"
        """
        self._rectangle.top_right = new_top_right
        self.connect_GameObject_with_rectangle()

    @property
    def bottom_left(self):
        """
        Getter para o vértice inferior esquerdo.


        :return: Vértice inferior esquerdo.
        :rtype: "vector2d.Vector2d"
        """
        return self._rectangle.bottom_left

    @bottom_left.setter
    def bottom_left(self, new_bottom_left: "vector2d.Vector2d"):
        """
        Setter para o vértice inferior esquerdo do GameObject.
        Define a posição do GameObject a partir do vértice inferior esquerdo.

        :param new_bottom_left: Nova posição do vértice inferior esquerdo.
        :type new_bottom_left: "vector2d.Vector2d"
        """
        self._rectangle.bottom_left = new_bottom_left
        self.connect_GameObject_with_rectangle()

    @property
    def bottom_right(self):
        """
        Getter para o vértice inferior direito.


        :return: Vértice inferior direito.
        :rtype: "vector2d.Vector2d"
        """
        return self._rectangle.bottom_right

    @bottom_right.setter
    def bottom_right(self, new_bottom_right: "vector2d.Vector2d"):
        """
        Setter para o vértice inferior direito do GameObject.
        Define a posição do GameObject a partir do vértice inferior direito.

        :param new_bottom_right: Nova posição do vértice inferior direito.
        :type new_bottom_right: "vector2d.Vector2d"
        """
        self._rectangle.bottom_right = new_bottom_right
        self.connect_GameObject_with_rectangle()

    @property
    def rotation(self):
        """
        Getter para o ângulo de rotação do GameObject.

        :return: Ângulo de rotação.
        :rtype: int
        """
        return self._rectangle.rotation

    @rotation.setter
    def rotation(self, angle: int):
        """
        Setter para rotation do GameObject.
        A rotação é feita no sentido horário.

        :param angle: Ângulo que desejamos rotacionar.
        :type angle: int
        """
        self._rectangle.rotation = angle
        self.connect_GameObject_with_rectangle()
        self._sprite.rotation = angle

    @property
    def left(self):
        """
        Getter para o x do lado esquerdo do GameObject.

        :return: X do lado esquerdo do GameObject.
        :rtype: int
        """
        return self._rectangle.left

    @left.setter
    def left(self, distance: int):
        """
        Setter para a esquerda do GameObject.
        Desloca o GameObject à esquerda.
        Por exemplo: rec.left = 3
        desloca o GameObject 3 pontos a esquerda.

        :param distance: Quantidade de deslocamento à esquerda.
        :type distance: int
        """
        self._rectangle.left = distance
        self.connect_GameObject_with_rectangle()

    @property
    def right(self):
        """
        Getter para o x do lado direito do GameObject.

        :return: X do lado direito do GameObject.
        :rtype: int
        """
        return self._rectangle.right

    @right.setter
    def right(self, distance: int):
        """
        Setter para a direita do GameObject.
        Desloca o GameObject à direita.
        Por exemplo: rec.right = 3
        desloca o GameObject 3 pontos a direita.

        :param distance: Quantidade de deslocamento à direita.
        :type distance: int
        """

        self._rectangle.right = distance
        self.connect_GameObject_with_rectangle()

    @property
    def top(self):
        """
        Getter para o y do lado superior do GameObject.

        :return: y do lado superior do GameObject.
        :rtype: int
        """
        return self._rectangle.top

    @top.setter
    def top(self, distance: int):
        """
        Setter para o top do GameObject.
        Desloca o GameObject para cima.
        Por exemplo: rec.top = 3
        desloca o GameObject 3 pontos para cima.

        :param distance: Quantidade de deslocamento para cima.
        :type distance: int
        """
        self._rectangle.top = distance
        self.connect_GameObject_with_rectangle()

    @property
    def bottom(self):
        """
        Getter para o y do lado inferior do GameObject.

        :return: y do lado inferior do GameObject.
        :rtype: int
        """
        return self._rectangle.bottom

    @bottom.setter
    def bottom(self, distance: int):
        """
        Setter para o bottom do GameObject.
        Desloca o GameObject para baixo.
        Por exemplo: rec.bottom = 3
        desloca o GameObject 3 pontos para baixo.

        :param distance: Quantidade de deslocamento para baixo.
        :type distance: int
        """
        self._rectangle.bottom = distance
        self.connect_GameObject_with_rectangle()

    @property
    def position(self):
        """
        Getter para a posição do GameObject.
        A posição do GameObject, por sua vez,
        está configurada como o seu centro.

        :return: Posição do GameObject
        :rtype: "vector2d.Vector2d"
        """
        return self._rectangle.position

    @position.setter
    def position(self, vector_position: "vector2d.Vector2d"):
        """
        Setter para a posição do GameObject.


        :param vector_position: Novo posição no plano ocupado pelo GameObject.
        :type vector_position: "vector2d.Vector2d"
        """
        self._rectangle.position = vector_position
        self.connect_GameObject_with_rectangle()

    @property
    def scale(self):
        """
        Getter para o valor de escala do sprite.

        """
        return self._sprite.scale

    @scale.setter
    def scale(self, size):
        """
        Setter para a proporção do tamanho do sprite
        do GameObject.

        :param size: Proporção do tamanho do sprite.
        :type size: [TODO:type]
        """

        self._sprite.scale = size
        self._rectangle.height = self._sprite.height
        self._rectangle.width = self._sprite.width
        self.connect_GameObject_with_rectangle()

    @property
    def x(self):
        """
        Getter para a abscissa da posição do GameObject.

        :return: Abcissa da posição.
        :rtype: int
        """
        return self._sprite.x

    @x.setter
    def x(self, new_x: int):
        """
        Setter para o x da posição do GameObject.

        :param new_x: Novo x da posição do GameObject.
        :type new_x: int
        """
        self._rectangle.x = new_x
        self.connect_GameObject_with_rectangle()

    @property
    def width(self):
        """
        Getter para a largura do GameObject.

        :return: Largura do GameObject.
        :rtype: int | float
        """
        return self._rectangle.width

    @property
    def height(self):
        """
        Getter para a altura do GameObject.

        :return: Altura do GameObject.
        :rtype: int | float
        """
        return self._rectangle.height

    @property
    def y(self):
        """
        Getter para a ordenada da posição do GameObject.


        :return: Ordenada da posição do GameObject.
        :rtype: int
        """
        return self._sprite.y

    @y.setter
    def y(self, new_y: int):
        """
        Setter para o y da posição do GameObject.

        :param new_y: Novo y da posição do GameObject.
        :type new_y: int
        """
        self._rectangle.y = new_y
        self.connect_GameObject_with_rectangle()

    @property
    def biggest_size(self):
        if self.width > self.height:
            return self.width
        if self.height > self.width:
            return self.height

    def on_click(self):
        """
        Método para determinar o comportamento do clique.

        """
        self.game_state.choose_tile_index = (
            self.game_state.my_player.hand_sprites.index(self)
        )

    def on_unclick(self):
        self.game_state.choose_tile_index = -1

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            mouse_position = vector2d.Vector2d(x, y)
            if self.is_interior_point(mouse_position):
                self.on_click()

    def on_mouse_release(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            self.on_unclick()
