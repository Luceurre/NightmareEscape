import pygame

from api.ActorAnimation import ActorAnimation
from api.Animation import Animation
from api.EnumAuto import EnumAuto
from api.EnumTeam import EnumTeam
from api.Timer import Timer
from game.actors.ActorArrowPlayer import ActorArrowPlayer
from game.actors.ActorArrowSlime import ActorArrowSlime
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
        self.shoot_range = 350
        self.shoot_rate = 1 / 3  # Nombre de tirs par seconde
        self.hp = 3

        self.collidable = True
        
        self.velocity = Vector(0,0)

    def reload(self):
        super().reload()

        self.handle_event = True

    def update(self):
        super().update()
        
        self.now = pygame.time.get_ticks()

        target = self.map.get_closest_ennemi(self.rect, range=200, ennemi_team=self.team.get_ennemi())
        if self.can_attack() and target is not None:
            self.attack(target)

    def can_attack(self):
        return self.state != ActorSlime.State.ATTACK

    def attack(self, target):
        self.state = ActorSlime.State.ATTACK
        print("le slime attaque")
        if self.attack_shoot: # création d'une attaque lancé de boulles verts vers la player
            print("le slime tire")
            if self.shoot and self.can_shoot:
                self.is_shooting = True
                self.can_shoot = False
                self.add_timer(Timer(self.shoot_rate, self.turn_on_shoot))
    
                arrow = ActorArrowSlime(self.detect_target_position(target), self.velocity)
                arrow.team = self.team
                arrow.rect.x = self.rect.x + (self.rect.w - arrow.rect.w) / 2
                arrow.rect.y = self.rect.y + (self.rect.h - arrow.rect.w) / 2
                self.map.add_actor(arrow)
                
                
                
        else: # création d'une attaque saut vers le player
            pass

    def idle(self):
        if not self.is_dead:
            self.state = ActorSlime.State.IDLE

    def die(self):
        self.collidable = False
        self.state = ActorSlime.State.DIE
        self.map.remove_actor(self)

    def dead(self):
        self.map.remove_actor(self)
        del self


    def turn_on_shoot(self):
        self.can_shoot = True
        
    def detect_target_position(self, target):
        x = target.rect.x - self.rect.x
        y = target.rect.y - self.rect.y
        d = (x*x + y*y)**0.5
        x = int( 2*  x/d )  #si cos < 0.5 ( angle > 60°), on considère que x doit valoir 0
        y = int( 2 * y/d ) # same here
        
        #pour gérer pb du int() dans le cas ou x et y sont négatifs
        if x < 0:
            x -= 1
        if y <0:
            y -=1
        return Vector(x, y)             # on renvoie bien une direction : le slime ne peut tirer que dans 8 directions

    def load_sprite(self):
        super().load_sprite()

        self.animations = {}
        self.animations[ActorSlime.State.IDLE] = Animation(load_image("assets/slime.png"), pygame.Rect(0, 0, 128, 128),
                                                           9, 50 , True)
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
        if isinstance(actor, ActorArrowPlayer) and actor.team == self.team.get_ennemi():
            self.hp -= 1
            if self.hp == 0:
                self.die()
            return True
        else:
            return False
