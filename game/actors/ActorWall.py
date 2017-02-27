import pygame

from game.actors.ActorCollidable import ActorCollidable


class ActorWall(ActorCollidable):
    ID = 5
    NAME = "WALL"

    def load_sprite(self):
        super().load_sprite()

        self.sprite = pygame.image.load("assets/Wall1.png").convert()
