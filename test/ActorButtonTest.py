import pygame
from api.ActorButton import ActorButton, BUTTON_STATE

class ActorButtonTest(ActorButton):
    def __init__(self):
        super().__init__()

        sprites = {
            BUTTON_STATE.NORMAL: pygame.image.load("assets/mario.jpg").convert(),
            BUTTON_STATE.HOVERED: pygame.image.load("assets/yoshi.jpg").convert(),
            BUTTON_STATE.PRESSED: pygame.image.load("assets/mario.jpg").convert()
        }

        self.sprites = sprites

    def draw(self, screen):
        super().draw(screen)