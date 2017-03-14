from game.actors.ActorMovable import ActorMovable
from game.utils.SurfaceHelper import load_image


class ActorWall(ActorMovable):
    ID = 5
    NAME = "WALL"

    def __init__(self):
        super().__init__()

    def load_sprite(self):
        super().load_sprite()

        self.sprite = load_image("assets/Wall1.png")
