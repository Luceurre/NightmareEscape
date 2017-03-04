import pygame

from api.ActorSprite import ActorSprite
from game.utils.SurfaceHelper import load_image


class ActorSimpleLife(ActorSprite):
    def __init__(self, path):
        super().__init__(False)

        self.path = path
        self.load_sprite()
        self.z = 100
        self.load_sprite()

    def load_sprite(self):
        super().load_sprite()

        try:
            self.sprite = load_image("assets/" + self.path, False)
        except:
            self.info("C'est normal, mon programme est puant !")
