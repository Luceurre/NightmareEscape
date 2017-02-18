import pygame

from api.ActorSprite import ActorSprite


class ActorAnimation(ActorSprite):
    def __init__(self, animation = None):
        super().__init__()

        if animation != None:
            self.animation = animation

    @property
    def sprite(self):
        return self.animation.get_sprite()

    @property
    def rect(self):
        return self.animation.get_rect(self._rect)