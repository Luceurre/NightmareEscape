from api.ActorSprite import ActorSprite
from game.utils.SurfaceHelper import load_image


class ActorDoor(ActorSprite):
    def __init__(self):
        super().__init__(True)

        self.is_open = False

    def load_sprite(self):
        super().load_sprite()

        self.sprites = {}
        self.sprites[True] = load_image("assets/door_open.png", False)
        self.sprites[False] = load_image("assets/door_close.png", False)

    def unload_sprite(self):
        super().unload_sprite()
        del self.sprites

    @property
    def sprite(self):
        return self.sprites[self.is_open]
