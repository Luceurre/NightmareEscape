import copy

import pygame

from api.ActorSprite import ActorSprite
from api.Timer import Timer
from game.utils.SurfaceHelper import load_image


class ActorGUIBar(ActorSprite):
    ID = 105
    NAME = "GUI_BAR"

    def __init__(self, ratio=1, color=(255, 255, 255, 255)):
        super().__init__()

        self.ratio = ratio
        self.color = color
        self.should_update = True

        # Constante de notre image...
        self.bar_rect = pygame.Rect(2, 2, 4 * 48 - 4, 24 - 4)

        self.add_timer(Timer(500, self.animation, True, infinite=True))

    def update(self):
        self.update_timers()

    def animation(self, *args, **kwargs):
        self.ratio *= 0.9
        print(self.ratio)

    def load_sprite(self):
        super().load_sprite()

        self.sprite = load_image("assets/gui_bar.png")

    def draw(self, screen):
        self.sprite.fill((0, 0, 0), self.bar_rect)
        rect = copy.copy(self.bar_rect)
        rect.w *= self.ratio
        self.sprite.fill(self.color, rect)

        super().draw(screen)


""
