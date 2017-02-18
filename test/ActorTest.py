import pygame

from api.ActorSprite import ActorSprite
from api.Timer import Timer

class ActorTest(ActorSprite):
    def __init__(self):
        super().__init__(pygame.image.load("assets/mario.jpg").convert())

        self.add_timer(timer = Timer(2000, self.print_test,repeat=True,how_many=2, infinite=False))

    def handle_keydown(self, unicode, key, mod):
        if unicode == "z":
            print("ACTOR WORKS!")
            return True
        else:
            return False

    def draw(self, screen):
        super().draw(screen)
        self.update_timers()

    def print_test(self, *args, **kwargs):
        print("Hello World!")