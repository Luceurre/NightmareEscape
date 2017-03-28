import copy

from api.ActorSprite import ActorSprite
from game.actors.ActorPlayer import ActorPlayer
#from game.actors.ActorPuzzleSolution import ActorPuzzleSolution
#from game.actors.ActorDoor import ActorDoor
#from pygame.examples.scaletest import SpeedTest




class ActorMovable(ActorSprite):                # A passer probablement sur ActorAnimation
    def __init__(self):
        super().__init__()

        self.speed = 1  # En pixel par déplacement   _____ MAIS : si trop bas par rapport au perso, enlève fluidité au personnage
        
        #collision
        self.collidable = True
        
    def reload(self):
        super().reload()
        
        self.collidable = True
        self.speed = 1
        
    def interact(self, actor):
        if isinstance(actor, ActorPlayer):
            if len(actor.direction_walk) == 1:
                rect_tmp = copy.deepcopy(actor.rect)
                actor.rect = actor.get_move_rect()
                test = self.move(actor.direction_walk[0].value.x * self.speed,
                                 actor.direction_walk[0].value.y * self.speed)
                if test:
                    actor.rect = rect_tmp
                    actor.move( actor.direction_walk[0].value.x * self.speed, actor.direction_walk[0].value.y * self.speed)
                actor.rect = rect_tmp
            return True
        else:
            return actor.collidable and self.collidable
