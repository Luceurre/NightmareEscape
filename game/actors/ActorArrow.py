import pygame

from api.ActorSprite import ActorSprite
from game.utils.Direction import DIRECTION
from game.utils.Vector import VECTOR_NULL, Vector


class ActorArrow(ActorSprite):

    ID = 2

    def __init__(self, dir=DIRECTION.NONE, velocity=VECTOR_NULL):
        super().__init__()

        self.dir = dir.value
        self.speed = 8
        self.velocity = Vector(0, 0)
        if self.dir.x * velocity.x >= 0:
            self.velocity.x = velocity.x / 2
        if self.dir.y * velocity.y >= 0:
            self.velocity.y = velocity.y / 2
        self.should_update = True

    def load_sprite(self):
        self.sprite = pygame.image.load("assets/bullet.png").convert_alpha()

    def update(self):
        super().update()

        self.move(self.speed * self.dir.x + self.velocity.x, self.speed * self.dir.y + self.velocity.y)

    def move(self, x, y):
        super().move(x ,y)

        if self.rect.colliderect(self.stage.rect) == False:
            self.stage.remove_actor(self)