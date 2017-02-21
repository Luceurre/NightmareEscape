from game.utils.SurfaceHelper import load_image

from game.actors.ActorCollidable import ActorCollidable


class ActorRock(ActorCollidable):

    ID = 4
    NAME = "ROCK"

    def load_sprite(self):
        super().load_sprite()

        self.sprite = load_image("assets/rock.png", True)