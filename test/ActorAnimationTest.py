import pygame

from api.ActorAnimation import ActorAnimation
from api.Animation import Animation


class ActorAnimationTest(ActorAnimation):
    def __init__(self, default=False):
        super().__init__()

        self.animation = Animation(pygame.image.load("assets/test.png"), pygame.Rect(0, 64 * 11, 64, 64), 9, 50, None, default)
        self._rect = pygame.Rect((0, 0), self.animation.rect.size)