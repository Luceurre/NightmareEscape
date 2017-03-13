import copy

import pygame

from api.Actor import Actor
from api.Logger import LOG_LEVEL
from api.StageManager import StageManager
from game.utils.Constants import WINDOW_WIDTH, WINDOW_HEIGHT
from game.utils.SurfaceHelper import shadowizer


class ActorSprite(Actor):

    def __init__(self, load_sprite=True):
        super().__init__()

        # Définition de nouveaux attributs
        self._rect = pygame.Rect(0, 0, 0, 0)
        self._sprite = None
        "self.sounds = None"
        self.draw_shadow = False
        self.collidable = False
        self.h = 0 # Hauteur pour les ombres
        self.depth = 0  # Profondeur de l'Actor ?

        if load_sprite:
            self.load_sprite() # Chargement des images ici !!

        # Modification d'attribut venant de la classe Actor
        self.should_draw = True

    def load_sprite(self):
        # Tous les chargements d'images, animations et autres trucs visuels doivent se faire ici !
        self._sprite = None
    
    """  
    def load_sounds(self):
        #chargement des sons 
        self.sounds = None
    """
    
    def reload(self):
        super().reload()

        self.draw_shadow = False
        self.collidable = False
        self.h = 0
        
        self.load_sprite()
        "self.load_sounds()"

    def unload(self):
        super().unload()
        self.unload_sprite()
        "self.unload_sound()"

    def unload_sprite(self):
        try:
            del self._sprite
        except:
            self.warning("Calling unload_sprite without calling load_sprite!")
            
    """      
    def unload_sound(self):
        try:
            del self.sounds
        except:
            self.warning("Calling unload_sounds without calling load_sounds!")
    """

    @property
    def rect(self):
        return self._rect

    @property
    def sprite(self):
        return self._sprite

    @sprite.setter
    def sprite(self, sprite):
        if not isinstance(sprite, pygame.Surface):
            self.log("Le Sprite n'est pas valide!", LOG_LEVEL.ERROR)
            StageManager().exit()
        else:
            self.rect.width = sprite.get_width()
            self.rect.height = sprite.get_height()
            self._sprite = sprite

    def draw(self, screen):
        if not isinstance(self.sprite, pygame.Surface):
            self.log("Le Sprite n'est pas valide!", LOG_LEVEL.ERROR)
            StageManager().exit()
        else:
            try:
                if self.draw_shadow:
                    rect = copy.copy(self.rect)
                    rect.y += self.h
                    screen.blit(shadowizer(self.sprite), rect)
                screen.blit(self.sprite, self.rect)
            except:
                self.load_sprite()
                self.info("Rechargement des images car Pickle.")
                screen.blit(self.sprite, self._rect)

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    # Quelques methodes pour aider :

    def set_centered_x(self, width):
        self.rect.x = (width - self.rect.width) / 2

    def set_centered_y(self, height):
        self.rect.y = (height - self.rect.height) / 2

    def set_centered(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT):
        self.rect.x = (width - self.rect.width) / 2
        self.rect.y = (height - self.rect.height) / 2