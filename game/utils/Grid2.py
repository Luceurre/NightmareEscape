import pygame

from api.Actor import Actor


class Grid2(Actor):
    def __init__(self):
        super().__init__()

        self.width = 64
        self.height = 64

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def get_size(self):
        return (self.width, self.height)

    def draw(self, screen):
        if self.should_draw:
            width = screen.get_width()
            height = screen.get_height()

            nb_w = int(width / self.size) + 1
            nb_h = int(height / self.size) + 1

            for x in range(nb_w):
                pygame.gfxdraw.vline(screen, x * self.size, 0, height, (255, 255, 255))

            for y in range(nb_h):
                pygame.gfxdraw.hline(screen, 0, width, y * self.size, (255, 255, 255))
