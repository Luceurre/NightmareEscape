import pygame

from api.ActorAnimation import ActorAnimation
from api.Animation import Animation
from api.EnumAuto import EnumAuto


class DIRECTION(EnumAuto):
    NORD = ()
    NORD_OUEST = ()
    OUEST = ()
    SUD_OUEST = ()
    SUD = ()
    SUD_EST = ()
    EST = ()
    NORD_EST = ()
    SHOOT_OUEST = ()

class ActorPlayerTest(ActorAnimation):


    def __init__(self):
        super().__init__()

        self.direction = DIRECTION.SUD
        self.animations = {}
        self.walk = False
        self.speed = 5
        self.shoot_rate = 1.2 # per second
        self.is_shooting = False

        self.keys = {122: False, 113: False, 115: False, 100: False, 273: False, 276: False, 274: False, 275: False}

        image = pygame.image.load("assets/marinka.png")

        self.animations[DIRECTION.SUD] = Animation(image, pygame.Rect(64, 10 * 64, 64, 64), 9, 50)
        self.animations[DIRECTION.NORD] = Animation(image, pygame.Rect(64, 8 * 64, 64, 64), 9, 50)
        self.animations[DIRECTION.OUEST] = Animation(image, pygame.Rect(0, 9 * 64, 64, 64), 10, 50)
        self.animations[DIRECTION.EST] = Animation(image, pygame.Rect(0, 11 * 64, 64, 64), 10, 50)

        self.animations[DIRECTION.SHOOT_OUEST] = Animation

        self.handle_event = True
        self.should_update = True

    def update(self):
        super().update()

        self.walk = True in self.keys.values()

        if self.keys[122]:
            self.direction = DIRECTION.NORD
        elif self.keys[113]:
            self.direction = DIRECTION.OUEST
        elif self.keys[115]:
            self.direction = DIRECTION.SUD
        elif self.keys[100]:
            self.direction = DIRECTION.EST



        if self.walk:
            if self.direction == DIRECTION.NORD:
                self.rect.y -= self.speed
            elif self.direction == DIRECTION.SUD:
                self.rect.y += self.speed
            elif self.direction == DIRECTION.EST:
                self.rect.x += self.speed
            elif self.direction == DIRECTION.OUEST:
                self.rect.x -= self.speed

    @property
    def animation(self):
        return self.animations[self.direction]

    @property
    def sprite(self):
        if self.walk == False:
            return self.animation.tile[0]
        else:
            return super().sprite

    def handle_keydown(self, unicode, key, mod):
        if key in self.keys.keys():
            self.keys[key] = True
            return True

    def handle_keyup(self, key, mod):
        if key in self.keys.keys():
            self.keys[key] = False
            return True

