from api.ActorSprite import ActorSprite
from game.utils import Vector
from game.utils.SurfaceHelper import load_image


class ActorTile(ActorSprite):
    def __init__(self, path: str, pos: Vector, size: int):
        super().__init__(False)

        self.path = path
        self.pos = pos
        self.size = size

        self.load_sprite()

    def load_sprite(self):
        super().load_sprite()

        self.sprite = load_image(self.path, False).subsurface((self.pos.x, self.pos.y), (self.size, self.size))
