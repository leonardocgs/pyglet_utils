import math


class Vector2d:
    def __init__(self, x: int | float, y: int | float):
        self.x: int | float = x
        self.y: int | float = y

    def __sub__(self, vector: "Vector2d") -> "Vector2d":
        """
        Método de sobrecarga do operador de subtração, permite que a operação
        de subtração seja feita duas instâncias de Vector2d.

        :param vector: Instância de Vector2d que ocupa a posição de subtraendo.
        :type vector: "Vector2d"
        :return: Vetor resultado da subtração.
        :rtype: "Vector2d"
        """
        if isinstance(vector, Vector2d):
            result_vector = self + vector.opposite_vector
            return result_vector

    def __add__(self, vector: "Vector2d") -> "Vector2d":
        """
        Método de sobrecarga do operador de adição, permite que a operação de
        adição seja feita duas instâncias de Vector2d.

        :param vector: Instância de Vector2d a ser adicionado.
        :type vector: "Vector2d"
        :return: Vetor resultado da adição.
        :rtype: "Vector2d"
        """
        if isinstance(vector, Vector2d):

            new_x = self.x + vector.x
            new_y = self.y + vector.y
            result_vector = Vector2d(new_x, new_y)
        return result_vector

    def distance(self, vector: "Vector2d") -> float:
        """
        Calcula a distância entre a instância de Vector2d que chama o
        método e uma outra instância passada como argumento do método.

        :param vector: Instância de Vector2d alvo para obter a distância
        :type vector: "Vector2d"
        :return: Distância entre os vetores
        :rtype: float
        :raises TypeError: Erro ao passar ao arg "vector" um tipo inválido.
        """
        if isinstance(vector, Vector2d):
            lenght = self.distance_vector(vector).magnitude
            return lenght
        raise TypeError('vector must be instance of "Vector2d"')

    def distance_vector(self, vector: "Vector2d") -> "Vector2d":
        """
        Obtêm o Vector2d que possui como magnitude a distância entre duas
        instâncias de  Vector2d.
        Considere o seguinte cenário:
        A = Vector2d(20,15)
        B = Vector2d(30,50)
        C = B.distance_vector(A)
        print(C)

        Nesse cenário temos como resultante do print(C):

        (10,35)

        O Vector2d C, nesse caso, é um Vector2d que adicionado ao Vector2d A,
        obtemos o Vector2d B.
        Ou seja, efetivamente é o Vector2d que precisamos adicionar a A para
        que as coordenadas de A virem as coordenadas de B.


        :param vector: Instância alvo para obter o Vector2d distância.
        :type vector: "Vector2d"
        :return: Vector2d que tem como magnitude a distância.
        :rtype: "Vector2d"
        :raises TypeError: Erro gerado caso seja o argumento passado à "vector"
        não seja do tipo "Vector2d".
        """
        if isinstance(vector, Vector2d):
            difference_vector = self - vector
            return difference_vector
        raise TypeError(
            'vector argument must be instance of "Vector2d"'
        )

    @property
    def opposite_vector(self) -> "Vector2d":
        """
        Getter para obter o Vector2d oposto

        :return: Vector2d oposto à instancia.
        :rtype: "Vector2d"
        """
        new_x = -self.x
        new_y = -self.y
        result_vector = Vector2d(new_x, new_y)
        return result_vector

    @property
    def magnitude(self) -> float:
        """
        Getter para a magnitude(comprimento) da istância do Vector2d.

        :return: Magnitude da instância de Vector2d.
        :rtype: float
        """
        lenght = math.sqrt(self.x**2 + self.y**2)
        return lenght

    def __eq__(self, vector: "Vector2d") -> bool:
        """
        Determina se duas instâncias de Vector2d são iguais.
        Dois Vector2d são iguais se e somente se tiverem o mesmo x e o mesmo y
        ao mesmo tempo.

        :param vector: instância de Vector2d que queremos comparar
        :type vector: "Vector2d"
        :return: True se são iguais ou False se forem diferentes.
        :rtype: bool
        """

        if isinstance(vector, Vector2d):
            return self.x == vector.x and self.y == vector.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return str((self.x, self.y))
