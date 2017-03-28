from api.ActorAnimation import ActorAnimation


class ActorAnimations(ActorAnimation):
    def __init__(self):
        super().__init__()

        self.animations = {}

    @property
    def animation(self):
        return self.animations
