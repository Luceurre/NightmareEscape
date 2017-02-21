import pygame

from api.Actor import Actor
from api.ActorSprite import ActorSprite


class ActorBackground(ActorSprite):
    def load_sprite(self):
        self.sprite = None