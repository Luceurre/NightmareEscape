import pygame

from api.ActorAnimation import ActorAnimation
from api.Animation import Animation
from api.EnumAuto import EnumAuto
from api.Rect import Rect
from api.Timer import Timer
from game.utils.SurfaceHelper import load_image


class ActorBomb(ActorAnimation):
    """Une belle bombe qui fait pleins de dégats avec surtout de très jolies animations"""

    class State(EnumAuto):
         DETONATE = () # Avant qu'elle explose
         EXPLODE = () # Quand elle explose

    def __init__(self):
        super().__init__()

        self.state = ActorBomb.State.DETONATE
        self.should_update = True
        
        self.damage = 1 #Ca fait quand même beaucoup!!!

        self.fuse_timer = Timer(20, self.fuse, True, infinite=True)
        self.add_timer(self.fuse_timer)

    def reload(self):
        super().reload()

    def load_sprite(self):
        super().load_sprite()

        self.animations = {}

        self.animations[ActorBomb.State.DETONATE] = Animation(load_image("assets/bibomb.png", False), Rect(0, 0, 41, 48), 2, 800)
        self.animations[ActorBomb.State.EXPLODE] = Animation(load_image("assets/explosion.png", False), pygame.Rect(0, 0, 192, 192), 5, 25, False, False, 5, self.destroyed)

    def fuse(self):
        self.animations[ActorBomb.State.DETONATE].time -= 10
        if self.animations[ActorBomb.State.DETONATE].time <= 20:
            self.explode()
            self.timers.remove(self.fuse_timer)


    def explode(self):
        rect_tmp = self.rect
        self.state = ActorBomb.State.EXPLODE
        self.rect.center = rect_tmp.center

    def destroyed(self):
        self.map.remove_actor(self)
        del self

    def update(self):
        super().update()

        self.update_timers()

    @property
    def animation(self):
        return self.animations[self.state]
    
    def interact(self, actor):
        if actor.etre_vivant:
            actor.hp -= self.damage
            
        return False