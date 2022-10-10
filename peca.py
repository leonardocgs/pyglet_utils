from game_object import GameObject
from Vector2d import Vector2d


class peca(GameObject):
    def __init__(
        self,
        position: "Vector2d",
        primeiro_valor,
        segundo_valor,
        img_path: str,
        rotation=0,
        batch=None,
    ):
        super().__init__(position, img_path, batch, rotation)
        self.primeiro_valor = primeiro_valor
        self.segundo_valor = segundo_valor
