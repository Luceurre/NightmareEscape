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
    
    def set_origin(self, Ox, Oy): #change l'origine de la grille selon les coordonnées Ox, Oy
        self.Ox = Ox
        self.Oy = Oy
        

    def draw(self, screen):
        if self.should_draw:
            width = screen.get_width()
            height = screen.get_height()

            nb_w = int(width / self.width) + 1
            nb_h = int(height / self.height) + 1

            for x in range(nb_w):
                pygame.gfxdraw.vline(screen, self.Ox + x * self.width, self.Oy, self.Oy + height, (255, 255, 255))

            for y in range(nb_h):
                pygame.gfxdraw.hline(screen, self.Ox, self.Ox + width, self.Oy + y * self.height, (255, 255, 255))
    
    def new_position(self, pos):
        new_pos = [0,0]
        if self.should_draw:            
            new_pos[0] = pos[0] - (pos[0] % self.width) + self.Ox
            new_pos[1] = pos[1] - (pos[1] % self.height) + self.Oy
        else:
            new_pos[0] = pos[0]
            new_pos[1] = pos[1]
        return new_pos
        
        
    
