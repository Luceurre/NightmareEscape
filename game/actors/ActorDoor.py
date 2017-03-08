import pygame

from api.ActorSprite import ActorSprite
from game.actors.ActorPlayer import ActorPlayer
from game.utils.Constants import EVENT_TP
from game.utils.SurfaceHelper import load_image
from game.utils.Vector import Vector


class ActorDoor(ActorSprite):
    NAME = "DOOR"
    ID = 7

    def __init__(self, map_name, spawn_pos_x=0, spawn_pos_y=0):
        super().__init__(False)

        self.is_open = True
        self.map_name = map_name
        self.spawn_pos = Vector(spawn_pos_x, spawn_pos_y)
        self.reload()

    def load_sprite(self):
        super().load_sprite()

        self.sprites = {}
        self.sprites[True] = load_image("assets/rock.png", False)
        self.sprites[False] = load_image("assets/rock.png", False)
        self.rect.w = self.sprite.get_width()
        self.rect.h = self.sprite.get_height()

    def unload_sprite(self):
        super().unload_sprite()
        del self.sprites

    @property
    def sprite(self):
        return self.sprites[self.is_open]

    def interact(self, actor):
        if isinstance(actor, ActorPlayer) and self.is_open:
            event = pygame.event.Event(pygame.USEREVENT, name=EVENT_TP, map_name=self.map_name,
                                       spawn_pos=self.spawn_pos, actor=actor)
            pygame.event.post(event)

            return True
        else:
            return False
