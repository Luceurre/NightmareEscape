import pygame.gfxdraw

from api.Actor import Actor
from game.utils.Vector import Vector
from _operator import pos


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
        pos_t = []
        if isinstance(pos, Vector):                                #Au cas où pos serait un Vector
            pos_t.append(pos.x)
            pos_t.append(pos.y)
        else:
            pos_t = pos
            
        new_pos = []
        
        if self.should_draw:            
            new_pos.append( (pos_t[0] + self.Ox)  - ((pos_t[0])  % self.width) )
            new_pos.append( (pos_t[1] + self.Oy)  - ((pos_t[1]) % self.height) )
        else:
            new_pos.append( pos_t[0] )
            new_pos.append( pos_t[1] )
        
        
        return Vector(new_pos[0], new_pos[1])
        
        
    
