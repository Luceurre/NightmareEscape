import pygame.gfxdraw

from api.Actor import Actor


class Grid2(Actor):
    def __init__(self):
        super().__init__()

        self.width = 64
        self.height = 64
        self.Ox = 0
        self.Oy = 0

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def get_size(self):
        return (self.width, self.height)
    
    def set_origin(self, Ox = 0, Oy = 0): #change l'origine de la grille selon les coordonnées Ox, Oy
        self.Ox = Ox % self.width
        self.Oy = Oy % self.height
        

    def draw(self, screen):
        if self.should_draw:
            width = screen.get_width()
            height = screen.get_height()

            nb_w = int(width / self.width) + 1
            nb_h = int(height / self.height) + 1

            for x in range(nb_w):
                pygame.gfxdraw.vline(screen, self.Ox + x * self.width, 0, self.Oy + height, (255, 255, 255))

            for y in range(nb_h):
                pygame.gfxdraw.hline(screen, 0, self.Ox + width, self.Oy + y * self.height, (255, 255, 255))

    def get_pos_x(self, x):  # Renvoie la coordonnée x de la droite de la grille se trouvant à gauche de cette droite.
        return x - x % self.width + self.Ox

    def get_pos_y(self, y):
        return y - y % self.height + self.Oy
