import pygame.gfxdraw

from api.Actor import Actor

class Grid(Actor):
    def __init__(self):
        super().__init__()

        self.size = 64


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