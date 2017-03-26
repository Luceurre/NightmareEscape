import pygame


class Rect:
    def __init__(self, x, y, w, h):
        self._x = x
        self._y = y
        self._w = w
        self._h = h

        self.pyrect = pygame.Rect(int(x), int(y), int(w), int(h))

    @property
    def x_real(self):
        return self._x

    @property
    def y_real(self):
        return self._y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x
        self.pyrect.x = int(x)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y
        self.pyrect.y = int(y)

    @property
    def w(self):
        return self.pyrect.w

    @w.setter
    def w(self, w):
        self._w = w
        self.pyrect.w = int(w)

    @property
    def width(self):
        return self.w

    @width.setter
    def width(self, w):
        self.w = w

    @property
    def height(self):
        return self.h

    @height.setter
    def height(self, h):
        self.h = h

    @property
    def h(self):
        return self.pyrect.h

    @h.setter
    def h(self, h):
        self._h = h
        self.pyrect.h = int(h)

    @property
    def topleft(self):
        return self.pyrect.topleft

    @topleft.setter
    def topleft(self, tuple):
        self.x = tuple[0]
        self.y = tuple[1]

    @property
    def center(self):
        return (self.x + self.w / 2, self.y + self.h / 2)

    @center.setter
    def center(self, tuple):
        self.x = tuple[0] - self.w / 2
        self.y = tuple[1] - self.h / 2

    @property
    def size(self):
        return (self.w, self.h)

    @size.setter
    def size(self, tuple):
        self.w = tuple[0]
        self.h = tuple[1]

    @property
    def centerx(self):
        return self.center[0]

    @centerx.setter
    def centerx(self, x):
        self.x = x - self.w / 2

    @property
    def centery(self):
        return self.center[1]

    @centery.setter
    def centery(self, y):
        self.y = y - self.h / 2

    @property
    def center_real(self):
        return (self._x + self._w / 2, self._y + self._h / 2)

    def collidepoint(self, x, y):
        return self.pyrect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.pyrect.colliderect(rect)