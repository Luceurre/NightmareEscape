import pygame

from api.ActorAnimation import ActorAnimation
from api.Animation import Animation
from api.EnumAuto import EnumAuto
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
        
        self.damage = 1 / tick #Ca fait quand même beaucoup!!!

    def reload(self):
        super().reload()

    def load_sprite(self):
        super().load_sprite()

        self.animations = {}

        self.animations[ActorBomb.State.DETONATE] = Animation(load_image("assets/bomb.png", False), pygame.Rect(0, 0, 48, 48), 1, 2500, callback_fun=self.explode)
        self.animations[ActorBomb.State.EXPLODE] = Animation(load_image("assets/explosion.png", False), pygame.Rect(0, 0, 192, 192), 5, 75, False, False, 5, self.destroyed)

    def explode(self):
        rect_tmp = self.rect
        self.state = ActorBomb.State.EXPLODE
        self.rect.center = rect_tmp.center

    def destroyed(self):
        self.map.remove_actor(self)
        del self

    @property
    def animation(self):
        return self.animations[self.state]
    
    def interact(self, actor):
        if actor.etre_vivant:
            actor.hp -= self.damage
            
        return False