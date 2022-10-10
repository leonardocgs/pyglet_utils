from game_object import GameObject




class peca(GameObject):


    def __init__(
        self,
        position: "Vector2d",
        img_path: str,
        batch=None,
        rotation=0,
        primeiro_valor,
        segundo_valor
    ):
        super().__init__(position,img_path,batch, rotation)
        self.primeiro_valor = primeiro_valor
        self.segundo_valor = segundo_valor
