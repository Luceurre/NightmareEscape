import pygame

from api.ActorSprite import ActorSprite


class ActorSimpleLife(ActorSprite):
    def __init__(self, path):
        super().__init__()

        self.path = path
        self.load_sprite()
        self.z = 100

    def load_sprite(self):
        super().load_sprite()

        try:
            self.sprite = pygame.image.load("assets/" + self.path)
        except:
            self.info("C'est normal, mon programme est puant !")
