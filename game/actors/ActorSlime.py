import pygame

from api.ActorAnimation import ActorAnimation
from api.Animation import Animation
from api.EnumAuto import EnumAuto
from api.EnumTeam import EnumTeam
from game.utils.SurfaceHelper import load_image


class ActorSlime(ActorAnimation):
    ID = 32
    NAME = "SLIME"

    class State(EnumAuto):
        IDLE = ()
        ATTACK = ()
        JUMP = ()
        MOVE = ()
        DIE = ()

    WIDTH = 32
    HEIGHT = 32
    FILE = "assets/slime.png"

    def __init__(self):
        super().__init__()

        self.state = ActorSlime.State.IDLE
        self.handle_event = True
        self.should_update = True

    def update(self):
        super().update()

        target = self.map.get_closest_ennemi(self.rect, EnumTeam.PLAYER_TEAM)
        if self.can_attack() and target is not None:
            self.attack(target)

    def can_attack(self):
        return self.state != ActorSlime.State.ATTACK

    def attack(self, target):
        self.state = ActorSlime.State.ATTACK

    def load_sprite(self):
        super().load_sprite()

        self.animations = {}
        self.animations[ActorSlime.State.IDLE] = Animation(load_image("assets/slime.png"), pygame.Rect(0, 0, 128, 128),
                                                           9, 50, True)
        self.animations[ActorSlime.State.MOVE] = Animation(load_image("assets/slime.png"),
                                                           pygame.Rect(0, 128, 128, 128), 9, 50, True)
        self.animations[ActorSlime.State.JUMP] = Animation(load_image("assets/slime.png"),
                                                           pygame.Rect(0, 256, 128, 128), 9, 50, True)
        self.animations[ActorSlime.State.ATTACK] = Animation(load_image("assets/slime.png"),
                                                             pygame.Rect(0, 384, 128, 128), 9, 50, True)
        self.animations[ActorSlime.State.DIE] = Animation(load_image("assets/slime.png"), pygame.Rect(0, 512, 128, 128),
                                                          9, 50, True)

    @property
    def animation(self):
        return self.animations[self.state]
