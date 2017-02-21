import pygame, math
from game.utils.SurfaceHelper import get_real_rect


class Animation:
    def __init__(self, image, load_rect, tile_number, time, auto_rect=False):
        self.tile = []
        self.rects = []
        self.auto_rect = auto_rect

        for i in range(tile_number):
            self.tile.append(
                image.subsurface(load_rect.x + load_rect.width * i, load_rect.y, load_rect.width, load_rect.height))

        if auto_rect:
            # Obtention des hitboxs réels des images -> utils.Image.get_real_rect :
            rect = get_real_rect(self.tile[0])
            for index, tile in enumerate(self.tile):
                # On en profite pour redimensionner les images :
                self.tile[index] = tile.subsurface(rect)
                self.rects.append(rect)

        self.now = pygame.time.get_ticks()
        self.at = 0
        self.tile_number = tile_number
        self.time = time

    def get_sprite(self):
        if self.tile_number == 1:
            return self.tile[0]
        elif pygame.time.get_ticks() - self.now >= self.time:
            self.at = (self.at + 1) % (self.tile_number - 1)
            self.now = pygame.time.get_ticks()

        return self.tile[self.at]

    def get_rect(self, rect):

        rect.size = self.rects[self.at].size
        return rect
