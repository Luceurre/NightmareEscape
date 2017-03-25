import copy
import pygame

from api.ActorAnimation import ActorAnimation
from api.Animation import Animation
from api.EnumAuto import EnumAuto
from api.EnumTeam import EnumTeam
from api.Timer import Timer
from game.actors.ActorArrowPlayer import ActorArrowPlayer
from game.actors.ActorArrowSlime import ActorArrowSlime
from game.actors.ActorPlayer import ActorPlayer
from game.utils.SurfaceHelper import load_image
from game.utils.Vector import Vector


class ActorSlime(ActorAnimation):
    """ Un ennemi (slime en l'occurence) qui a plusieurs animations selon qu'il soit imobile, attaquant , mourant ou en déplacement"""
    
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

        self.attack_shoot = True
        self.shoot_range = 500
        self.shoot_rate = 1000  # Période des tirs : en ms
        self.detection_range = 1000 # Distance à laquelle il perçoit un ennemi
        self.jump_range = 700
        self.jump_cd = 0
        self.jump_cd_max = 200
        self.jump_vect_in = None
        self.jump_in = True
        self.jump_count = 0
        self.jump_count_max = 30
        self.jump_return_pos = None
        self.jump_initial_pos = None
        self.jump_velocity = 12
        self.ammo_max = 3 # Le nombre de balles
        self.ammo = self.ammo_max # Le nombre de balles max
        self.hp = 3
        
        self.collidable = True
        self.should_update = True
        
        self.velocity = Vector(0,0)

    def reload(self):
        super().reload()

        self.handle_event = True
        self.should_update = True
        self.etre_vivant = True

    def update(self):
        super().update()

        self.update_timers()
        if self.jump_cd > 0:
            self.jump_cd -= 1

        if self.state == ActorSlime.State.JUMP:
            if self.jump_in:
                self.rect.x += self.jump_vect_in.x * self.jump_velocity
                self.rect.y += self.jump_vect_in.y * self.jump_velocity

                if self.jump_vect_in.x * (self.jump_target_pos.center[0] - self.rect.center[0]) < 0 or self.jump_vect_in.y * (self.jump_target_pos.center[1] - self.rect.center[1]) < 0:
                    self.state = ActorSlime.State.IDLE
                    self.jump_cd = self.jump_cd_max
            else:
                self.rect.x += (self.jump_return_pos.center[0] - self.jump_pos.center[0]) / 40
                self.rect.y += (self.jump_return_pos.center[1] - self.jump_pos.center[1]) / 40

                if (self.jump_return_pos.center[0] - self.jump_pos.center[0]) * (self.jump_return_pos.center[0] - self.rect.center[0]) < 0:
                    self.state = ActorSlime.State.IDLE



        target = self.map.get_closest_ennemi(self.rect, range=self.detection_range, ennemi_team=self.team.get_ennemi())
        if self.can_attack() and target is not None:
            if self.can_shoot(target):
                self.shoot(target)
            elif self.can_jump(target):
                self.jump(target)

    def can_attack(self):
        return self.state == ActorSlime.State.IDLE

    def get_distance(self, target):
        return (self.rect.x - target.rect.x) ** 2 + (self.rect.y - target.rect.y) ** 2

    def can_shoot(self, target):
        return self.get_distance(target) <= self.shoot_range ** 2 and self.ammo > 0

    def can_jump(self, target):
        return  self.get_distance(target) <= self.jump_range ** 2 and self.jump_cd == 0

    def jump(self, target):
        self.state = ActorSlime.State.JUMP
        self.jump_initial_pos = copy.copy(self.rect)
        self.jump_return_pos = copy.copy(target.rect)
        self.jump_target_pos = copy.copy(target.rect)
        self.jump_return_pos.x += 300
        self.jump_count = 0

        self.jump_vect_in = Vector(target.rect.center[0] - self.rect.center[0],
                                   target.rect.center[1] - self.rect.center[1])
        self.jump_vect_in.normalize()
    def shoot(self, target):
        self.state = ActorSlime.State.ATTACK

        arrow = ActorArrowSlime(self.detect_target_position(target))
        arrow.team = self.team
        arrow.rect.x = self.rect.x + (self.rect.w - arrow.rect.w) / 2
        arrow.rect.y = self.rect.y + (self.rect.h - arrow.rect.w) / 2
        self.map.add_actor(arrow)

        self.ammo -= 1

        if self.ammo == 0:
            self.reload_ammo()

    def reload_ammo(self):
        self.add_timer(Timer(2500, self.reload_ammo_callback))

    def reload_ammo_callback(self):
        self.ammo = self.ammo_max

    def idle(self):
        if not self.is_dead:
            self.state = ActorSlime.State.IDLE

    def die(self):
        self.collidable = False
        self.state = ActorSlime.State.DIE

    def dead(self):
        self.map.remove_actor(self)
        del self


    def turn_on_shoot(self):
        print("turn on shoor appellé")
        self.can_shoot = True
        
    def detect_target_position(self, target):
        """Renvoie le vecteur (target.rect.center - self.rect.center) pour donner la direction où aller/tirer"""

        pos = Vector(target.rect.center[0] - self.rect.center[0],  target.rect.center[1] - self.rect.center[1])

        return pos

    def load_sprite(self):
        super().load_sprite()

        self.animations = {}
        self.animations[ActorSlime.State.IDLE] = Animation(load_image("assets/slime.png"), pygame.Rect(0, 0, 128, 128),
                                                           9, 50 , True)
        self.animations[ActorSlime.State.MOVE] = Animation(load_image("assets/slime.png"),
                                                           pygame.Rect(0, 128, 128, 128), 9, 100, True)
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
        if isinstance(actor, ActorArrowPlayer) and actor.team == self.team.get_ennemi():
            self.hp -= 1
            if self.hp == 0:
                self.die()
            return True
        else:
            return False
