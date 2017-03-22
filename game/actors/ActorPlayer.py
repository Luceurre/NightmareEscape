import copy

import pygame
import pygame.locals
import platform

from api.ActorAnimation import ActorAnimation
from api.Animation import Animation
from api.EnumTeam import EnumTeam
from api.Timer import Timer
from game.actors.ActorArrowPlayer import ActorArrowPlayer
from game.actors.ActorArrowSlime import ActorArrowSlime
from game.utils.Constants import *
from game.utils.Direction import DIRECTION
from game.utils.SurfaceHelper import load_image
from game.utils.Vector import VECTOR_NULL


class ActorPlayer(ActorAnimation):
    ID = 3
    NAME = "PLAYER"

    def __init__(self):
        super().__init__()

        # On charge toutes les images etc...
        # Chargement des animations :
        # => ça a changé cf load_sprite()

        self.z = -50
        self.team = EnumTeam.PLAYER_TEAM

        self.should_update = True
        self.handle_event = True

        self.direction = DIRECTION.BAS

        # Déplacements
        self.walk = False
        self.has_moved = False
        self.speed = 4  # En pixel par tick
        self.direction_walk = []

        self.velocity = Vector(0, 0)
        self.velocity_max = 4

        # Tirs
        self.shoot_rate = 200.0  # Période des tirs : en ms
        self.can_shoot = True
        #self.is_shooting = False  # Pour l'animation ? #inutile: pas de projet de faire animation de tirs en cours
        self.shoot = False

        # Quelques caractèristiques :
        self.hp_max = 100
        self.hp = 100

        # 3D ?
        self.depth = PLAYER_DEPTH

        self.reload()

    def reload(self):
        super().reload()

        # Gestion des touches utilisées :
        # [key]: [activate?, direction(optional)] => toujours utiliser ce format
        # Test pour voir OS utilisé car pygame considère que windows est tjrs en qwerty
        
        if platform.system() == 'Windows':
            
            self.keys_shoot = {
                273: [False, DIRECTION.HAUT],
                276: [False, DIRECTION.GAUCHE],
                274: [False, DIRECTION.BAS],
                275: [False, DIRECTION.DROITE]
            }
    
            self.keys_move = {
                pygame.locals.K_w: [False, DIRECTION.HAUT],
                pygame.locals.K_a: [False, DIRECTION.GAUCHE],
                pygame.locals.K_s: [False, DIRECTION.BAS],
                pygame.locals.K_d: [False, DIRECTION.DROITE]
            }
    
            self.keys_other = {
                pygame.locals.K_b: [False]
            }
        else:
            
            self.keys_shoot = {
                273: [False, DIRECTION.HAUT],
                276: [False, DIRECTION.GAUCHE],
                274: [False, DIRECTION.BAS],
                275: [False, DIRECTION.DROITE]
            }
    
            self.keys_move = {
                pygame.locals.K_z: [False, DIRECTION.HAUT],
                pygame.locals.K_q: [False, DIRECTION.GAUCHE],
                pygame.locals.K_s: [False, DIRECTION.BAS],
                pygame.locals.K_d: [False, DIRECTION.DROITE]
            }
    
            self.keys_other = {
                pygame.locals.K_b: [False]
            }
            
            

        self.keys = [self.keys_shoot, self.keys_move, self.keys_other]
        self.direction = DIRECTION.BAS

        self.draw_shadow = True
        self.collidable = True
        self.team = EnumTeam.PLAYER_TEAM

    def unload(self):
        super().unload()

        del self.keys_shoot
        del self.keys_move
        del self.keys_other
        del self.keys
        del self.direction

    def load_sprite(self):
        sprites_sheet = load_image("assets/marinka.png", False)
        self.animations = {}

        self.animations[DIRECTION.HAUT] = Animation(sprites_sheet, pygame.Rect(PLAYER_MOVE_TOP.x * PLAYER_SPRITE_WIDTH,
                                                                               PLAYER_MOVE_TOP.y * PLAYER_SPRITE_HEIGHT,
                                                                               PLAYER_SPRITE_WIDTH,
                                                                               PLAYER_SPRITE_HEIGHT),
                                                    PLAYER_MOVE_TILES_NUMBER, PLAYER_MOVE_TIME, auto_rect=True)
        self.animations[DIRECTION.GAUCHE] = Animation(sprites_sheet,
                                                      pygame.Rect(PLAYER_MOVE_LEFT.x * PLAYER_SPRITE_WIDTH,
                                                                  PLAYER_MOVE_LEFT.y * \
                                                                  PLAYER_SPRITE_HEIGHT, PLAYER_SPRITE_WIDTH,
                                                                  PLAYER_SPRITE_HEIGHT),
                                                      PLAYER_MOVE_TILES_NUMBER, PLAYER_MOVE_TIME, True)
        self.animations[DIRECTION.DROITE] = Animation(sprites_sheet,
                                                      pygame.Rect(PLAYER_MOVE_RIGHT.x * PLAYER_SPRITE_WIDTH,
                                                                  PLAYER_MOVE_RIGHT.y * \
                                                                  PLAYER_SPRITE_HEIGHT, PLAYER_SPRITE_WIDTH,
                                                                  PLAYER_SPRITE_HEIGHT),
                                                      PLAYER_MOVE_TILES_NUMBER, PLAYER_MOVE_TIME, True)
        self.animations[DIRECTION.BAS] = Animation(sprites_sheet,
                                                   pygame.Rect(PLAYER_MOVE_BOTTOM.x * PLAYER_SPRITE_WIDTH,
                                                               PLAYER_MOVE_BOTTOM.y * \
                                                               PLAYER_SPRITE_HEIGHT, PLAYER_SPRITE_WIDTH,
                                                               PLAYER_SPRITE_HEIGHT),
                                                   PLAYER_MOVE_TILES_NUMBER, PLAYER_MOVE_TIME, True)
        self.animations[DIRECTION.NONE] = Animation(sprites_sheet, pygame.Rect(PLAYER_STANDBY.x * PLAYER_SPRITE_WIDTH,
                                                                               PLAYER_STANDBY.y * \
                                                                               PLAYER_SPRITE_HEIGHT,
                                                                               PLAYER_SPRITE_WIDTH,
                                                                               PLAYER_SPRITE_HEIGHT), 1, 1000, True)

        self.animation = self.animations[DIRECTION.NONE]

    def unload_sprite(self):
        super().unload_sprite()

        del self.animation
        del self.animations

        self.info("Sprites unloaded successfully!")

    def update(self):
        super().update()

        if self.keys_other[pygame.K_b][0]:
            for actor in self.map.actors:
                try:
                    actor.close()
                except:
                    pass

        self.update_timers()

        self.walk = False
        self.direction = DIRECTION.NONE
        self.direction_walk = []
        for value in self.keys_move.values():
            if value[0]:
                self.direction = value[1]
                self.direction_walk.append(value[1])
                self.walk = True

        self.shoot = False
        for value in self.keys_shoot.values():
            if value[0]:
                self.direction = value[1]
                self.shoot = True
                break

        if self.walk:
            speed_x = 0
            speed_y = 0
            for direction in self.direction_walk:
                speed_x += direction.value.x
                speed_y += direction.value.y

            self.velocity.x = self.velocity_max * speed_x
            self.velocity.y = self.velocity_max * speed_y
        else:
            self.velocity.null()

        if self.velocity != VECTOR_NULL:
            self.has_moved = self.move(x=self.velocity.x, y=self.velocity.y)

        if not self.has_moved:
            self.velocity.null()

        if self.shoot and self.can_shoot:
            #self.is_shooting = True     #inutile: pas de projet de faire animation de tirs en cours
            self.can_shoot = False
            self.add_timer(Timer(self.shoot_rate, self.turn_on_shoot))

            arrow = ActorArrowPlayer(self.direction, self.velocity)
            arrow.team = self.team
            arrow.rect.x = self.rect.x + (self.rect.w - arrow.rect.w) / 2
            arrow.rect.y = self.rect.y + (self.rect.h - arrow.rect.w) / 2
            self.map.add_actor(arrow)

        self.animation = self.animations[self.direction]

    def move(self, x=0, y=0):
        """Return True if the Player moved, False otherwise"""

        if x == 0 and y == 0:
            return False

        rect = copy.copy(pygame.Rect(self.rect))
        rect.x += x - 2
        rect.y += y - 2

        rect.y += rect.h - self.depth
        rect.h = self.depth

        rect.w += 1
        rect.h += 1

        actors = self.map.get_actors_collide(rect, [self])

        a_interagi = False
        for actor in actors:
            b = actor.interact(self)
            if not a_interagi and b:
                a_interagi = True

        if not a_interagi:
            self.rect.x += x
            self.rect.y += y

            return True
        else:
            return False

    def interact(self, actor):
        # Pour éviter que le Joueur prenne des dégâts de ses propres projectiles :)
        if isinstance(actor, ActorArrowPlayer):
            return False
        if isinstance(actor, ActorArrowSlime) and actor.team == self.team.get_ennemi():
            self.hp -= actor.damage
            return True
        else:
            return super().interact(actor)

    def turn_on_shoot(self, *args, **kwargs):
        self.can_shoot = True

    # Override methods

    def handle_keydown(self, unicode, key, mod): # indique quel déplacement, quel tir a été activé par l'évènement
        for index, keys in enumerate(self.keys):
            if key in keys.keys():
                self.keys[index][key][0] = True
                return True
        if key == pygame.K_e:
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, name=EVENT_PLAYER_INTERACT, actor=self))
            return True

    def handle_keyup(self, key, mod):
        for index, keys in enumerate(self.keys):
            if key in keys.keys():
                self.keys[index][key][0] = False
                return True
