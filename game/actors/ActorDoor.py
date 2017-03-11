import pygame

from api.ActorSprite import ActorSprite
from api.Animation import Animation
from api.Timer import Timer
from game.actors.ActorPlayer import ActorPlayer
from game.utils.Constants import EVENT_TP
from game.utils.Direction import DIRECTION
from game.utils.SurfaceHelper import load_image, load_image_tile
from game.utils.Vector import Vector


class ActorDoor(ActorSprite):
    NAME = "DOOR"
    ID = 7

    def __init__(self, map_name, spawn_pos_x=0, spawn_pos_y=0, direction=DIRECTION.BAS):
        super().__init__(False)

        self.is_open = False
        self.map_name = map_name
        self.spawn_pos = Vector(spawn_pos_x, spawn_pos_y)

        self.sprites = {}
        self.animation = None
        self.direction = direction
        self.reload()

    def reload(self):
        super().reload()

        self.should_update = True
        self.collidable = True

    def update(self):
        super().update()

        self.update_timers()

    def load_sprite(self):
        super().load_sprite()

        self.sprites = {}

        self.sprites[False] = pygame.transform.flip(
            load_image_tile("assets/gates.png", pygame.Rect(0, 0, 96, 64), True), False, True)
        self.sprites[True] = pygame.transform.flip(
            load_image_tile("assets/gates.png", pygame.Rect(0, 192, 96, 64), True), False, True)
        self.sprite = self.sprites[self.is_open]

        self.animation = Animation(load_image("assets/gates.png"), pygame.Rect(0, 64, 96, 64), 2, auto_rect=True,
                                   vertical=True)

    def open(self):
        if not self.is_open and self.timers == []:
            timer = Timer(200, self.open_animation, True, 2)

            self.add_timer(timer)

    def open_animation(self, *args, **kwargs):
        sprite = self.animation.next_sprite()
        if sprite is None:
            self.sprite = self.sprites[True]
            self.is_open = True
        else:
            self.sprite = sprite

    def unload_sprite(self):
        super().unload_sprite()

    def interact(self, actor):
        if isinstance(actor, ActorPlayer) and self.is_open:

            event = pygame.event.Event(pygame.USEREVENT, name=EVENT_TP, map_name=self.map_name,
                                       spawn_pos=self.spawn_pos, actor=actor)
            pygame.event.post(event)

            return True
        elif actor.collidable and self.collidable:
            return True
        else:
            return False
