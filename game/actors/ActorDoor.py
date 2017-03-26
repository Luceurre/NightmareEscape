import pygame

from api.ActorSprite import ActorSprite
from api.Animation import Animation
from api.Timer import Timer
import game.actors.ActorPlayer
from game.utils.Constants import EVENT_TP, EVENT_PLAYER_INTERACT, EVENT_WIN
from game.utils.Direction import DIRECTION
from game.utils.SurfaceHelper import load_image, load_image_tile
from game.utils.Vector import Vector


class ActorDoor(ActorSprite):

    """Et oui, une porte, tout simplement, qui peut s'ouvrir, téléporter le player sur une autre map via l'event EVENT_TP """
    
    NAME = "DOOR"
    ID = 7

    def __init__(self, map_name= "level_0", spawn_pos_x=700, spawn_pos_y=650, direction=DIRECTION.BAS):
        super().__init__(False)

        self.is_open = False
        self.map_name = map_name
        self.spawn_pos = Vector(spawn_pos_x, spawn_pos_y)

        self.sprites = {}
        self.animation = None
        self.direction = direction
        self.reload()

    def reload(self):
        """ lorsqu'on recharge l'image """
        super().reload()

        self.should_update = True
        self.collidable = True
        self.handle_event = True

    def update(self):
        super().update()

        self.update_timers()

    def load_sprite(self): # Chargement des images de la porte
        super().load_sprite()

        self.sprites = {}

        self.sprites[False] = pygame.transform.flip(
            load_image_tile("assets/gates.png", pygame.Rect(0, 0, 96, 64), True), False, False)
        self.sprites[True] = pygame.transform.flip(
            load_image_tile("assets/gates.png", pygame.Rect(0, 192, 96, 64), True), False, False)
        self.sprite = self.sprites[self.is_open]

        self.animation = Animation(load_image("assets/gates.png"), pygame.Rect(0, 64, 96, 64), 2, auto_rect=True,
                                   vertical=True)

    def open(self):
        if not self.is_open and self.timers == []:
            timer = Timer(200, self.open_animation, True, 2)

            self.add_timer(timer)

    def close(self):
        if self.is_open and self.timers == []:
            timer = Timer(200, self.close_animation, True, 2)

            self.add_timer(timer)


    def open_animation(self, *args, **kwargs):
        sprite = self.animation.next_sprite()
        if sprite is None:
            self.sprite = self.sprites[True]
            self.is_open = True
        else:
            self.sprite = sprite

    def close_animation(self, *args, **kwargs):
        sprite = self.animation.previous_sprite()
        if sprite is None:
            self.sprite = self.sprites[False]
            self.is_open = False
        else:
            self.sprite = sprite


    def unload_sprite(self):
        super().unload_sprite()

    def interact(self, actor):
        # gère la collision d'un Acteur avec la porte: si c'est le player, et qu'elle est ouverte : poste un event du type EVENT_TP avec pour attribut le nom de la map, la position
        #du spawn et l'acteur en question ( même si est en théorie tjrs le player )
        if isinstance(actor, game.actors.ActorPlayer.ActorPlayer) and self.is_open:

            event = pygame.event.Event(pygame.USEREVENT, name=EVENT_TP, map_name=self.map_name,
                                       spawn_pos=self.spawn_pos, actor=actor)
            pygame.event.post(event)

            return True
        elif actor.collidable and self.collidable:
            return True
        else:
            return False

    def handle_userevent(self, event): # gère l'ouverture de porte via event EVENT_PLAYER_INTERACT ( à utiliser avec une plaque de pression, ou la suppression de tout les monstre, etc)
        if event.name == EVENT_PLAYER_INTERACT:
            self.open()



class ActorDoorWin(ActorSprite):

    """Et oui, une porte, tout simplement, qui peut s'ouvrir, téléporter le player sur une autre map via l'event EVENT_TP """
    
    NAME = "DOORWIN"
    ID = 70

    def __init__(self):
        super().__init__(False)

        self.is_open = False

        self.sprites = {}
        self.animation = None
        self.reload()

    def reload(self):
        """ lorsqu'on recharge l'image """
        super().reload()

        self.should_update = True
        self.collidable = True
        self.handle_event = True

    def update(self):
        super().update()

        self.update_timers()

    def load_sprite(self): # Chargement des images de la porte
        super().load_sprite()

        self.sprites = {}

        self.sprites[False] = pygame.transform.flip(
            load_image_tile("assets/gates.png", pygame.Rect(0, 0, 96, 64), True), False, False)
        self.sprites[True] = pygame.transform.flip(
            load_image_tile("assets/gates.png", pygame.Rect(0, 192, 96, 64), True), False, False)
        self.sprite = self.sprites[self.is_open]

        self.animation = Animation(load_image("assets/gates.png"), pygame.Rect(0, 64, 96, 64), 2, auto_rect=True,
                                   vertical=True)

    def open(self):
        if not self.is_open and self.timers == []:
            timer = Timer(200, self.open_animation, True, 2)

            self.add_timer(timer)

    def close(self):
        if self.is_open and self.timers == []:
            timer = Timer(200, self.close_animation, True, 2)

            self.add_timer(timer)


    def open_animation(self, *args, **kwargs):
        sprite = self.animation.next_sprite()
        if sprite is None:
            self.sprite = self.sprites[True]
            self.is_open = True
        else:
            self.sprite = sprite

    def close_animation(self, *args, **kwargs):
        sprite = self.animation.previous_sprite()
        if sprite is None:
            self.sprite = self.sprites[False]
            self.is_open = False
        else:
            self.sprite = sprite


    def unload_sprite(self):
        super().unload_sprite()


    def handle_userevent(self, event): # gère l'ouverture de porte via event EVENT_PLAYER_INTERACT ( à utiliser avec une plaque de pression, ou la suppression de tout les monstre, etc)
        if event.name == EVENT_PLAYER_INTERACT:
            self.open()
        
    def interact(self, actor):
        
        if isinstance(actor, game.actors.ActorPlayer.ActorPlayer) and self.is_open:

            event = pygame.event.Event(pygame.USEREVENT, name=EVENT_WIN)
            pygame.event.post(event)

            return True
        elif actor.collidable and self.collidable:
            return True
        else:
            return False
        
    """    
    def update(self):
        super().update()    
        
    def reload(self):
        super().reload()
        
    def load_sprite(self):
        super().load_sprite()
        
    def open(self):
        super().open()
    def close(self):
        super.close()
        
    def open_animation(self, *args, **kwargs):
        super().open_animation(*args, **kwargs)
        
    def close_animation(self, *args, **kwargs):
        super().close_animation(*args, **kwargs)  
    
    def unload_sprite(self):
        super().unload_sprite()  
        
    def handle_userevent(self, event):
        super().handle_userevent(event)
        
    """    
    
