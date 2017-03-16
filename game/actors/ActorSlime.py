import pygame

from api.ActorAnimation import ActorAnimation
from api.Animation import Animation
from api.EnumAuto import EnumAuto
from api.EnumTeam import EnumTeam
from game.actors.ActorArrow import ActorArrow
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
        self.team = EnumTeam.MONSTER_TEAM

        self.shoot_range = 350
        self.shoot_rate = 1 / 3  # Nombre de tirs par seconde
        self.hp = 3
        self.collidable = True

    def reload(self):
        super().reload()

        self.handle_event = True
        self.should_update = True

    def update(self):
        super().update()

        target = self.map.get_closest_ennemi(self.rect, range=200, ennemi_team=self.team.get_ennemi())
        if self.can_attack() and target is not None:
            self.attack(target)

    def can_attack(self):
        return self.state != ActorSlime.State.ATTACK

    def attack(self, target):
        self.state = ActorSlime.State.ATTACK

    def idle(self):
        if not self.is_dead:
            self.state = ActorSlime.State.IDLE

    def die(self):
        self.collidable = False
        self.state = ActorSlime.State.DIE

    def dead(self):
        self.map.remove_actor(self)
        del self

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
                                                             pygame.Rect(0, 384, 128, 128), 9, 50, True,
                                                             callback_fun=self.idle)
        self.animations[ActorSlime.State.DIE] = Animation(load_image("assets/slime.png"), pygame.Rect(0, 512, 128, 128),
                                                          9, 50, True, callback_fun=self.dead)

    @property
    def animation(self):
        return self.animations[self.state]

    @property
    def is_dead(self):
        return self.hp <= 0

    def interact(self, actor):
        if not self.collidable:
            return False
        if isinstance(actor, ActorArrow) and actor.team == self.team.get_ennemi():
            self.hp -= 1
            if self.hp == 0:
                self.die()
            return True
        else:
            return False
