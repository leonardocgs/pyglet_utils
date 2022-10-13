import pyglet
from pyglet.window import mouse

from Rectangle import Rectangle
from Vector2d import Vector2d


class Text:
    """
    Classe para ser utilizada para manipular label do pyglet.
    Seus pontos são represantados pela classe Vector2d,
    ou seja eles são representados como um vetor.
    A posição do Text está ancorada no ponto médio das
    diagonais do Text, ou seja, seu x e y correspondem
    aos x e y do desse ponto médio.
    Em particular essa classe permite mover o triângulo
    no plano cartesiano através dos :
        Vertices:
            top_left: Vértice superior esquerdo
            top_right: Vértice superior direito
            tottom_left: Vértice inferior esquerdo
            bottom_right: Vértice inferior direito
        Pontos médios:
            top_mid: Ponto médio do lado superior do Text.
            bottom_mid: Ponto médio do lado inferior do Text.
            left_mid: Ponto médio do lado esquerdo do Text.
            right_mid: Ponto médio lado direito do Text.
            center: Ponto médio das diagonais do Text.
        Posição:
            position: Ponto que representa a posição do triângulo no plano
            cartesiano.
        Abscissa e ordenada:
            x: Abcissa da posição do Text
            y :Ordenada da posição do Text
        Mover em relação a uma direção:
            left: Move à esquerda
            right: Move à direita
            top: Move para cima
            bottom :move para baixo
    :param position: Posição inicial do Text
    :type position: "Vector2d"
    :param img_path: path da imagem do Text
    :type img_path: str
    :param batch: Batch do Text
    :type batch: [TODO:type], optional
    :param rotation: Ângulo de rotação do triângulo no sentido horário.
    :type rotation: int, optional
    """

    def __init__(
        self,
        text: str,
        position: "Vector2d",
        batch=None,
    ):
        """
        Construtor do Text


        :param position: Posição inicial do Text
        :type position: "Vector2d"
        :param img_path: path da imagem do Text
        :type img_path: str
        :param batch: Batch do Text
        :type batch: [TODO:type], optional
        :param rotation: Ângulo de rotação do triângulo no sentido horário.
        :type rotation: int, optional
        """
        self._label = pyglet.text.Label(
            text=text,
            x=position.x,
            y=position.y,
            anchor_x="center",
            anchor_y="center",
            batch=batch,
        )
        self._width = self._label.content_width
        self._height = self._label.content_height
        print(self._height, self._width)
        self._position = position
        self._rectangle = Rectangle(
            position, self._width, self._height
        )

    def connect_Text_with_rectangle(self):
        """
        Conecta a classe de label do pyglet com a classe Rectangle.
        Isso é feito associando as respectivas abscissas e ordenadas
        das duas classes.

        """
        self._label.x = self._rectangle.x
        self._label.y = self._rectangle.y

    @property
    def center(self):
        """
        Getter para o centro do Text
        (Ponto médio das diagonais do Text)

        :return: Centro do Text.
        :rtype: "Vector2d"
        """
        return self._rectangle.center

    def draw(self):
        """
        Reescreve o método draw do pyglet.label.Label

        """
        self._label.draw()

    def delete(self):
        """
        Método para deletar o Text.

        """
        self._label.delete()

    def is_interior_point(self, vector: "Vector2d"):
        """
        Verifica se o ponto correspondente ao vetor passado
        como argumento é interior ao Text.

        :param vector: Vetor que representa o ponto para checar.
        :type vector: "Vector2d"
        """
        return self._rectangle.is_interior_point(vector)

    @property
    def left_mid(self):
        """
        Getter para o ponto médio do lado
        esquerdo do Text.

        :return: Ponto médio do lado esquerdo do Text.
        :rtype: "Vector2d"
        """
        return self._rectangle.left_mid

    @property
    def right_mid(self):
        """
        Getter para o ponto médio do lado
        direito do Text.

        :return: Ponto médio do lado direito do Text.
        :rtype: "Vector2d"
        """
        return self._rectangle.right_mid

    @property
    def top_mid(self):
        """
        Getter para o ponto médio do lado
        superior do Text.

        :return: Ponto médio do lado superior do Text.
        :rtype: "Vector2d"
        """
        return self._rectangle.top_mid

    @property
    def bottom_mid(self):
        """
        Getter para o ponto médio do lado
        inferior do Text.

        :return: Ponto médio do lado inferor do Text.
        :rtype: "Vector2d"
        """
        return self._rectangle.bottom_mid

    @property
    def top_left(self):
        """
        Getter para o vértice superior esquerdo.


        :return: Vértice superior esquerdo.
        :rtype: "Vector2d"
        """
        return self._rectangle.top_left

    @property
    def top_right(self):
        """
        Getter para o vértice superior direito.


        :return: Vértice superior direito.
        :rtype: "Vector2d"
        """
        return self._rectangle.top_right

    @property
    def bottom_left(self):
        """
        Getter para o vértice inferior esquerdo.


        :return: Vértice inferior esquerdo.
        :rtype: "Vector2d"
        """
        return self._rectangle.bottom_left

    @property
    def bottom_right(self):
        """
        Getter para o vértice inferior direito.


        :return: Vértice inferior direito.
        :rtype: "Vector2d"
        """
        return self._rectangle.bottom_right

    @property
    def left(self):
        """
        Getter para o x do lado esquerdo do Text.

        :return: X do lado esquerdo do Text.
        :rtype: int
        """
        return self._rectangle.left

    @property
    def right(self):
        """
        Getter para o x do lado direito do Text.

        :return: X do lado direito do Text.
        :rtype: int
        """
        return self._rectangle.right

    @property
    def top(self):
        """
        Getter para o y do lado superior do Text.

        :return: y do lado superior do Text.
        :rtype: int
        """
        return self._rectangle.top

    @property
    def bottom(self):
        """
        Getter para o y do lado inferior do Text.

        :return: y do lado inferior do Text.
        :rtype: int
        """
        return self._rectangle.bottom

    @property
    def position(self):
        """
        Getter para a posição do Text.
        A posição do Text, por sua vez,
        está configurada como o seu centro.

        :return: Posição do Text
        :rtype: "Vector2d"
        """
        return (
            self._position.x,
            self._position.y,
        )

    @property
    def x(self):
        """
        Getter para a abscissa da posição do Text.

        :return: Abcissa da posição.
        :rtype: int
        """
        return self._label.x

    @property
    def width(self):
        """
        Getter para a largura do Text.

        :return: Largura do Text.
        :rtype: int | float
        """
        return self._rectangle.width

    @property
    def height(self):
        """
        Getter para a altura do Text.

        :return: Altura do Text.
        :rtype: int | float
        """
        return self._rectangle.height

    @property
    def y(self):
        """
        Getter para a ordenada da posição do Text.


        :return: Ordenada da posição do Text.
        :rtype: int
        """
        return self._label.y

    @position.setter
    def position(self, vector_position: "Vector2d"):
        """
        Setter para a posição do Text.


        :param vector_position: Novo posição no plano ocupado pelo Text.
        :type vector_position: "Vector2d"
        """
        self._rectangle.position = vector_position
        self.connect_Text_with_rectangle()

    @center.setter
    def center(self, new_center: "Vector2d"):
        """
        Setter para o centro do Text.
        Define a posição do Text a partir do centro.

        :param new_center: Nova posição do centro do Text.
        :type new_center: "Vector2d"
        """
        self._rectangle.center = new_center
        self.connect_Text_with_rectangle()

    @left_mid.setter
    def left_mid(self, new_left_mid: "Vector2d"):
        """
        Setter para o ponto médio do lado esquerdo.
        Define a posição do Text a partir do ponto métido do lado
        esquerdo.

        :param new_left_mid: Nova posição do ponto médio do lado esquerdo.
        :type new_left_mid: "Vector2d"
        """
        self._rectangle.left_mid = new_left_mid
        self.connect_Text_with_rectangle()

    @right_mid.setter
    def right_mid(self, new_right_mid: "Vector2d"):
        """
        Setter para o ponto médio do lado direito.
        Define a posição do Text a partir do ponto médio do lado direito
        do Text.

        :param new_right_mid: Nova posição do ponto médio do lado direito.
        :type new_right_mid: "Vector2d"
        """
        self._rectangle.right_mid = new_right_mid
        self.connect_Text_with_rectangle()

    @top_mid.setter
    def top_mid(self, new_top_mid: "Vector2d"):
        """
        Setter para o ponto médio do lado superior.
        Define a posição do Text a partir do ponto médio do lado
        superior do Text

        :param new_top_mid: Nova posição do ponto médio do lado superior.
        :type new_top_mid: "Vector2d"
        """
        self._rectangle.top_mid = new_top_mid
        self.connect_Text_with_rectangle()

    @bottom_mid.setter
    def bottom_mid(self, new_bottom_mid: "Vector2d"):
        """
        Setter para o ponto médio do lado inferior.
        Define a posição do Text a partir do ponto médio do lado
        inferior do Text.

        :param new_bottom_mid: Nova posição do ponto médio do lado inferior.
        :type new_bottom_mid: "Vector2d"
        """
        self._rectangle.bottom_mid = new_bottom_mid
        self.connect_Text_with_rectangle()

    @top_left.setter
    def top_left(self, top_left: "Vector2d"):
        """
        Setter para o vértice superior esquerdo do Text.
        Define a posição do Text a partir do vértice superior
        esquerdo do Text.

        :param new_top_left: Nova posição do vértice superior esquerdo.
        :type new_top_left: "Vector2d"
        """
        self._rectangle.top_left = top_left

    @position.setter
    def position(self, vector_position: "Vector2d"):
        """
        Setter para a posição do Text.


        :param vector_position: Novo posição no plano ocupado pelo Text.
        :type vector_position: "Vector2d"
        """
        self._rectangle.position = vector_position
        self.connect_Text_with_rectangle()

    @center.setter
    def center(self, new_center: "Vector2d"):
        """
        Setter para o centro do Text.
        Define a posição do Text a partir do centro.

        :param new_center: Nova posição do centro do Text.
        :type new_center: "Vector2d"
        """
        self._rectangle.center = new_center
        self.connect_Text_with_rectangle()

    @left_mid.setter
    def left_mid(self, new_left_mid: "Vector2d"):
        """
        Setter para o ponto médio do lado esquerdo.
        Define a posição do Text a partir do ponto métido do lado
        esquerdo.

        :param new_left_mid: Nova posição do ponto médio do lado esquerdo.
        :type new_left_mid: "Vector2d"
        """
        self._rectangle.left_mid = new_left_mid
        self.connect_Text_with_rectangle()

    @right_mid.setter
    def right_mid(self, new_right_mid: "Vector2d"):
        """
        Setter para o ponto médio do lado direito.
        Define a posição do Text a partir do ponto médio do lado direito
        do Text.

        :param new_right_mid: Nova posição do ponto médio do lado direito.
        :type new_right_mid: "Vector2d"
        """
        self._rectangle.right_mid = new_right_mid
        self.connect_Text_with_rectangle()

    @top_mid.setter
    def top_mid(self, new_top_mid: "Vector2d"):
        """
        Setter para o ponto médio do lado superior.
        Define a posição do Text a partir do ponto médio do lado
        superior do Text

        :param new_top_mid: Nova posição do ponto médio do lado superior.
        :type new_top_mid: "Vector2d"
        """
        self._rectangle.top_mid = new_top_mid
        self.connect_Text_with_rectangle()

    @bottom_mid.setter
    def bottom_mid(self, new_bottom_mid: "Vector2d"):
        """
        Setter para o ponto médio do lado inferior.
        Define a posição do Text a partir do ponto médio do lado
        inferior do Text.

        :param new_bottom_mid: Nova posição do ponto médio do lado inferior.
        :type new_bottom_mid: "Vector2d"
        """
        self._rectangle.bottom_mid = new_bottom_mid
        self.connect_Text_with_rectangle()

    @top_left.setter
    def top_left(self, new_top_left: "Vector2d"):
        """
        Setter para o vértice superior esquerdo do Text.
        Define a posição do Text a partir do vértice superior
        esquerdo do Text.

        :param new_top_left: Nova posição do vértice superior esquerdo.
        :type new_top_left: "Vector2d"
        """
        self._rectangle.top_left = new_top_left
        self.connect_Text_with_rectangle()

    @top_right.setter
    def top_right(self, new_top_right: "Vector2d"):
        """
        Setter para o vértice superior direito do Text.
        Define a posição do Text a partir do vértice superior direito.

        :param new_top_right: Nova posição do vértice superior direito.
        :type new_top_right: "Vector2d"
        """
        self._rectangle.top_right = new_top_right
        self.connect_Text_with_rectangle()

    @bottom_left.setter
    def bottom_left(self, new_bottom_left: "Vector2d"):
        """
        Setter para o vértice inferior esquerdo do Text.
        Define a posição do Text a partir do vértice inferior esquerdo.

        :param new_bottom_left: Nova posição do vértice inferior esquerdo.
        :type new_bottom_left: "Vector2d"
        """
        self._rectangle.bottom_left = new_bottom_left
        self.connect_Text_with_rectangle()

    @bottom_right.setter
    def bottom_right(self, new_bottom_right: "Vector2d"):
        """
        Setter para o vértice inferior direito do Text.
        Define a posição do Text a partir do vértice inferior direito.

        :param new_bottom_right: Nova posição do vértice inferior direito.
        :type new_bottom_right: "Vector2d"
        """
        self._rectangle.bottom_right = new_bottom_right
        self.connect_Text_with_rectangle()

    @x.setter
    def x(self, new_x: int):
        """
        Setter para o x da posição do Text.

        :param new_x: Novo x da posição do Text.
        :type new_x: int
        """
        self._rectangle.x = new_x
        self.connect_Text_with_rectangle()

    @y.setter
    def y(self, new_y: int):
        """
        Setter para o y da posição do Text.

        :param new_y: Novo y da posição do Text.
        :type new_y: int
        """
        self._rectangle.y = new_y
        self.connect_Text_with_rectangle()

    @left.setter
    def left(self, distance: int):
        """
        Setter para a esquerda do Text.
        Desloca o Text à esquerda.
        Por exemplo: rec.left = 3
        desloca o Text 3 pontos a esquerda.

        :param distance: Quantidade de deslocamento à esquerda.
        :type distance: int
        """
        self._rectangle.left = distance
        self.connect_Text_with_rectangle()

    @right.setter
    def right(self, distance: int):
        """
        Setter para a direita do Text.
        Desloca o Text à direita.
        Por exemplo: rec.right = 3
        desloca o Text 3 pontos a direita.

        :param distance: Quantidade de deslocamento à direita.
        :type distance: int
        """

        self._rectangle.right = distance
        self.connect_Text_with_rectangle()

    @top.setter
    def top(self, distance: int):
        """
        Setter para o top do Text.
        Desloca o Text para cima.
        Por exemplo: rec.top = 3
        desloca o Text 3 pontos para cima.

        :param distance: Quantidade de deslocamento para cima.
        :type distance: int
        """
        self._rectangle.top = distance
        self.connect_Text_with_rectangle()

    @bottom.setter
    def bottom(self, distance: int):
        """
        Setter para o bottom do Text.
        Desloca o Text para baixo.
        Por exemplo: rec.bottom = 3
        desloca o Text 3 pontos para baixo.

        :param distance: Quantidade de deslocamento para baixo.
        :type distance: int
        """
        self._rectangle.bottom = distance
        self.connect_Text_with_rectangle()

    def on_click(self):
        """
        Método para determinar o comportamento do clique.

        """

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            mouse_position = Vector2d(x, y)
            if self.is_interior_point(mouse_position):
                self.on_click()
