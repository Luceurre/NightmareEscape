from api.ActorSprite import ActorSprite


class ActorAnimation(ActorSprite):
    def __init__(self, animation = None):
        super().__init__()

        if animation != None:
            self.animation = animation

    @property
    def sprite(self):
        if self.should_update:
            return self.animation.get_sprite()
        else:
            return self.animation.tile[0]

    @property
    def rect(self):
        return self.animation.get_rect(self._rect)