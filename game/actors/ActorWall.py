from game.actors.ActorCollidable import ActorCollidable
from game.utils.SurfaceHelper import load_image


class ActorWall(ActorCollidable):
    ID = 5
    NAME = "WALL"

    def __init__(self):
        super().__init__()

    def load_sprite(self):
        super().load_sprite()

        self.sprite = load_image("assets/Wall1.png")
