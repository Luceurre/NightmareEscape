import pygame

from game.actors.ActorCollidable import ActorCollidable


class ActorRock(ActorCollidable):

    ID = 4

    def load_sprite(self):
        super().load_sprite()

        self.sprite = pygame.image.load("assets/rock.png")