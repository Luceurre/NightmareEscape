import pygame

from api.ActorSprite import ActorSprite


class ActorEvent(ActorSprite):
    def __init__(self, size=(32, 32)):
        super().__init__()

        self.should_draw = False
        self._rect.size = size

        self.load_sprite()


    def load_sprite(self):
        self.sprite = pygame.Surface(self._rect.size)
        self.sprite.fill((255, 0, 255, 100))

