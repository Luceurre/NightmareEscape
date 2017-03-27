import copy
import random
import math

import pygame

from api.ActorAnimation import ActorAnimation
from api.Animation import Animation
from api.EnumAuto import EnumAuto
from api.EnumTeam import EnumTeam
from api.Rect import Rect
from api.Timer import Timer
from game.actors.ActorArrowPlayer import ActorArrowPlayer
from game.actors.ActorArrowSlime import ActorArrowSlime
from game.utils.SurfaceHelper import load_image
from game.utils.Vector import Vector
from game.actors.ActorDoor import ActorDoor, ActorDoorWin


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

    WIDTH = 128
    HEIGHT = 128
    FILE = "assets/slime_blue_128.png"

    def __init__(self):
        super().__init__()

        self.state = ActorSlime.State.IDLE
        self.team = EnumTeam.MONSTER_TEAM

        self.attack_shoot = False
        self.shoot_range = 500
        self.detection_range = 1000 # Distance à laquelle il perçoit un ennemi
        self.jump_range = 700
        self.jump_cd = 0
        self.jump_cd_max = 200
        self.jump_theta = 0
        self.jump_in = True
        self.jump_count = 0
        self.jump_count_max = 30
        self.jump_initial_pos = None
        self.jump_velocity = 12
        self.ammo_max = 3 # Le nombre de balles
        self.ammo = self.ammo_max # Le nombre de balles max
        self.hp = 50 # vie du slime

        self.collidable = True
        self.should_update = True

        self.velocity = Vector(0,0)

    def reload(self):
        super().reload()

        self.handle_event = True
        self.should_update = True
        self.etre_vivant = True

        self.attack_shoot = False  # Permet de ne pas tirer dès le début
        self.shoot_range = 500
        self.shoot_rate = 1000  # Période des tirs : en ms
        self.detection_range = 1000  # Distance à laquelle il perçoit un ennemi
        self.jump_range = 700
        self.jump_cd = 0
        self.jump_cd_max = 400
        self.jump_theta = 0 #angle définissant le jump
        self.jump_in = True
        self.jump_count = 0
        self.jump_count_max = 30
        self.jump_initial_pos = None
        self.jump_velocity = 12     #vitesse du saut
        self.theta = 0
        self.ammo_max = 3  # Le nombre de balles
        self.ammo = self.ammo_max  # Le nombre de balles max
        self.hp = 50     # vie su slime

        self.move_cd = 0
        self.move_cd_max = 125
        self.move_vect = None
        self.move_count = 0
        self.move_count_max = 75
        self.move_velocity = 2

        self.collidable = True
        self.should_update = True

        self.velocity = Vector(0, 0)
        
        self.add_timer(Timer(2000, self.allow_attack))

    def allow_attack(self, *arks, **kwargs):
        self.attack_shoot = True
        
    def update(self):
        super().update()

        self.update_timers()
        if self.jump_cd > 0:
            self.jump_cd -= 1
        if self.move_cd > 0:
            self.move_cd -= 1

        if self.state == ActorSlime.State.JUMP:
            if self.jump_in:
                can_move = self.move(self.jump_vect_in.x * self.jump_velocity, self.jump_vect_in.y * self.jump_velocity)

                if not can_move:
                    self.state = ActorSlime.State.IDLE
                    self.jump_cd = self.jump_cd_max

                if self.jump_vect_in.x * (self.jump_target_pos.center_real[0] - self.rect.center_real[0]) < 0 and self.jump_vect_in.y * (self.jump_target_pos.center_real[1] - self.rect.center_real[1]) < 0:
                    self.jump_in = False
                    theta = random.random() * 2 * math.pi
                    self.jump_vect_out = Vector(self.rect.x + 100 * math.cos(theta) - self.rect.center_real[0],
                                   self.rect.y + 300 * math.sin(theta) - self.rect.center_real[1])
                    self.jump_vect_out.normalize()
                    self.jump_return_pos = Rect(self.rect.x + 100 * math.cos(theta), self.rect.y + 300 * math.sin(theta), 0, 0)
            else:
                self.jump_cd = self.jump_cd_max
                self.state = ActorSlime.State.IDLE
        elif self.state == ActorSlime.State.MOVE:
            can_move = self.move(self.move_vect.x * self.move_velocity, self.move_vect.y * self.move_velocity)
            self.move_count += 1
            if not can_move or self.move_count >= self.move_count_max:
                self.state = ActorSlime.State.IDLE
                self.move_cd = self.move_cd_max

        target = self.map.get_closest_ennemi(self.rect, range=self.detection_range, ennemi_team=self.team.get_ennemi())
        
        if self.can_attack() and target is not None and self.allowed_attack:
            if self.can_shoot(target):
                self.shoot(target)
            elif self.can_jump(target):
                self.jump(target)
            elif self.can_move():
                self.move_it()
        elif self.can_move():
            self.move_it()

    def can_move(self):
        return self.state == ActorSlime.State.IDLE and self.move_cd == 0

    def move_it(self):
        theta = random.random() * 2 * math.pi
        self.move_vect = Vector(150 * math.cos(theta), 150 * math.sin(theta))
        self.move_vect.normalize()
        self.state = ActorSlime.State.MOVE
        self.move_count = 0

    def can_attack(self):
        return self.state == ActorSlime.State.IDLE

    def get_distance(self, target):
        return (self.rect.x - target.rect.x) ** 2 + (self.rect.y - target.rect.y) ** 2

    def can_shoot(self, target):
        return self.get_distance(target) <= self.shoot_range ** 2 and self.ammo > 0

    def can_jump(self, target):
        return self.get_distance(target) <= self.jump_range ** 2 and self.jump_cd == 0

    def jump(self, target):
        self.state = ActorSlime.State.JUMP
        self.jump_initial_pos = copy.deepcopy(self.rect)
        self.jump_return_pos = copy.deepcopy(target.rect)
        self.jump_target_pos = copy.deepcopy(target.rect)
        self.jump_return_pos.x += 300
        self.jump_count = 0
        self.jump_in = True

        self.jump_vect_in = Vector(target.rect.center_real[0] - self.rect.center_real[0],
                                   target.rect.center_real[1] - self.rect.center_real[1])
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
        nb_slime = 0
        
        for actor in self.map.actors:
            if isinstance(actor, ActorSlime):
                nb_slime += 1
        
        if nb_slime == 1:
            for actor in self.map.actors:
                if isinstance(actor, ActorDoor) or isinstance(actor, ActorDoorWin):
                    actor.open()
        
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

        sprite_sheet = load_image(type(self).FILE, False)
        width = type(self).WIDTH
        height = type(self).HEIGHT

        self.animations = {}
        self.animations[ActorSlime.State.IDLE] = Animation(sprite_sheet, pygame.Rect(0, 0, width, height),
                                                           9, 50 , True)
        self.animations[ActorSlime.State.MOVE] = Animation(sprite_sheet,
                                                           pygame.Rect(0, height, width, height), 9, 100, True)
        self.animations[ActorSlime.State.JUMP] = Animation(sprite_sheet,
                                                           pygame.Rect(0, height * 2, width, height), 9, 50, True)
        self.animations[ActorSlime.State.ATTACK] = Animation(sprite_sheet,
                                                             pygame.Rect(0, height * 3, width, height), 9, 50, True,
                                                             callback_fun=self.idle)
        self.animations[ActorSlime.State.DIE] = Animation(sprite_sheet, pygame.Rect(0, height * 4, width, height),
                                                          9, 50, True, callback_fun=self.dead)
        pass

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
            self.hp -= actor.damage
            if self.hp <= 0:
                self.die()
            return True
        else:
            return False
