import pygame, math


class Animation:
    def __init__(self, image, load_rect, tile_number, time, corr_rect=None, link_rect=False):
        self.tile = []
        self.rect = None

        for i in range(tile_number):
            self.tile.append(
                image.subsurface(load_rect.x + load_rect.width * i, load_rect.y, load_rect.width, load_rect.height))

        if corr_rect is not None:
            for i in range(tile_number):
                self.tile[i] = self.tile[i].subsurface(corr_rect.x, corr_rect.y, corr_rect.width, corr_rect.height)

        if corr_rect is not None and link_rect:
            for i in range(tile_number):
                self.rect.append(pygame.Rect((0, 0), (corr_rect.width, corr_rect.height)))

        elif link_rect and corr_rect is None:
            min_x = self.tile[i].get_width()
            min_y = self.tile[i].get_height()
            max_x = max_y = 0

            for i in range(tile_number):
                for x in range(self.tile[i].get_width()):
                    for y in range(self.tile[i].get_height()):
                        if self.tile[i].get_at((x, y))[3] is not 0:
                            if x < min_x:
                                min_x = x
                            elif x > max_x:
                                max_x = x
                            if y < min_y:
                                min_y = y
                            elif y > max_y:
                                max_y = y

            self.rect = pygame.Rect(min_x, min_y, max_x - min_x +1, max_y - min_y + 1)

            for i in range(tile_number):
                self.tile[i] = self.tile[i].subsurface(self.rect.x, self.rect.y, self.rect.width, self.rect.height)

        else:
            for i in range(tile_number):
                self.rect = pygame.Rect(0, 0, self.tile[0].get_width(), self.tile[0].get_height())

        self.now = pygame.time.get_ticks()
        self.at = 0
        self.tile_number = tile_number
        self.time = time
        self.linked_rect = link_rect

    def get_sprite(self):
        if self.tile_number == 1:
            return self.tile[0]
        elif pygame.time.get_ticks() - self.now >= self.time:
            self.at = (self.at + 1) % (self.tile_number - 1)
            self.now = pygame.time.get_ticks()

        return self.tile[self.at]

    def get_rect(self, rect):
        """
        if rect.size == self.rect[self.at].size:
            return rect
        else:
            rect.x += int((rect.w - self.rect[self.at].w) / 2) - (self.rect[self.at -1].x - self.rect[self.at].x) #((rect.w - self.rect[self.at].w) / 2)
            rect.y += (rect.h - self.rect[self.at].h) / 2
            rect.size = self.rect[self.at].size
        """

        return rect