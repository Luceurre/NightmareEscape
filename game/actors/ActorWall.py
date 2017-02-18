import pygame

from game.actors.ActorCollidable import ActorCollidable

class ActorWall(ActorCollidable):

    ID = 1
    NAME = "Wall"

    def __init__(self):
        super().__init__()

        self.should_update = True
        self.speed = 5

    def load_sprite(self):
        self.sprite = pygame.image.load("assets/mario.jpg").convert_alpha()

    def update(self):
        self.rect.y += self.speed
        if self.rect.y + self.rect.height > pygame.display.get_surface().get_height():
            self.rect.y = pygame.display.get_surface().get_height() - self.rect.height
            self.speed *= -1
        elif self.rect.y < 0:
            self.rect.y = 0
            self.speed *= -1