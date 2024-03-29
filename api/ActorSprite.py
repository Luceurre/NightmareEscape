import copy

import pygame

from api.Actor import Actor
from api.EnumTeam import EnumTeam
from api.Logger import LOG_LEVEL
from api.Rect import Rect
from api.StageManager import StageManager
from game.utils.Constants import WINDOW_WIDTH, WINDOW_HEIGHT
from game.utils.SurfaceHelper import shadowizer


class ActorSprite(Actor):
    
    """ Acteurs qui seront affichés à l'écran ( en pratique tout les acteurs héritent de ça je croit )
    """
    
    def __init__(self, load_sprite=True):
        super().__init__()

        # Définition de nouveaux attributs
        self._rect = Rect(0, 0, 0, 0)
        self._sprite = None
        "self.sounds = None"
        self.draw_shadow = False
        self.collidable = False  # Permet de savoir si un objet est "dur" ou "mou"
        self.h = 0 # Hauteur pour les ombres
        self.depth = 0  # Profondeur de l'Actor ?
        self.invicible = False # Pour tricher

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
        
        self.load_sprite()
        "self.load_sounds()"

        if isinstance(self.rect, pygame.Rect):
            rect_t = Rect(self.rect.x, self.rect.y, self.rect.w, self.rect.h)
            self._rect = rect_t

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

    @rect.setter
    def rect(self, rect):
        if isinstance(rect, pygame.Rect):
            rect_t = Rect(rect.x, rect.y, rect.w, rect.h)
            self._rect = rect
        else:
            self._rect = rect

    @property
    def sprite(self):
        return self._sprite

    @sprite.setter
    def sprite(self, sprite): # pour lier l'acteur et l'image
        if not isinstance(sprite, pygame.Surface):
            self.log("Le Sprite n'est pas valide!", LOG_LEVEL.ERROR)
            StageManager().exit()
        else:
            self.rect.width = sprite.get_width()
            self.rect.height = sprite.get_height()
            self._sprite = sprite

    def draw(self, screen): # Dessine l'image
        if not isinstance(self.sprite, pygame.Surface):
            self.log("Le Sprite n'est pas valide!", LOG_LEVEL.ERROR)
            StageManager().exit()
        else:
            try:
                if self.draw_shadow:
                    rect = copy.deepcopy(self.rect)
                    rect.y += self.h
                    screen.blit(shadowizer(self.sprite), rect.pyrect)
                screen.blit(self.sprite, self.rect.pyrect)
            except:
                self.load_sprite()
                self.info("Rechargement des images car Pickle.")
                screen.blit(self.sprite, self._rect.pyrect)

    # Quelques methodes pour aider : (noms assez explicites)

    def set_centered_x(self, width):
        self.rect.x = (width - self.rect.width) / 2

    def set_centered_y(self, height):
        self.rect.y = (height - self.rect.height) / 2

    def set_centered(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT):
        self.rect.x = (width - self.rect.width) / 2
        self.rect.y = (height - self.rect.height) / 2

    def move(self, x=0, y=0):
        """Return True if the Actor moved , False otherwise + make the Actor move"""

        if x == 0 and y == 0:
            return False

        rect_tmp = copy.deepcopy(self.rect)
        rect_tmp.x += x
        rect_tmp.y += y
        if self.depth != 0:
            rect_tmp.y += self.rect.h - self.depth
            rect_tmp.h = self.depth

        actors = self.map.get_actors_collide(rect_tmp.pyrect, [self])

        """
        remove_indexes = []

        for index, actor in enumerate(actors):
            if not actor.collidable:
                remove_indexes.append(index)

        for i, index in enumerate(remove_indexes):
            actors.pop(index - i)
        """

        a_interagi = False
        for actor in actors:
            b = actor.interact(self)  # PB: envoie son rect actuel, pas le rect qu'il aura après son déplacement
            if not a_interagi and b:
                a_interagi = True

        if not a_interagi:
            self.rect.x += x
            self.rect.y += y

            return True
        else:
            return False

    def interact(self, actor):
        if not super().interact(actor):
            if actor.collidable and self.collidable and (self.team != actor.team or self.team == EnumTeam.NEUTRAL_TEAM):
                return True
            else:
                return False
        else:
            return True

    def get_move_rect(self):
        return self.rect
