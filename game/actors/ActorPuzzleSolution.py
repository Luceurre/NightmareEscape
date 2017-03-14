from api.ActorEvent import ActorEvent
import game.actors.ActorMovable
from game.utils.Sounds import SON_ACHIEVMENT


class ActorPuzzleSolution(ActorEvent):
    
    NAME = "PUZZLESOLUTION"
    
    def __init__(self):
        super().__init__((64,64))
        
    def interact(self, actor):
        if isinstance(actor, game.actors.ActorMovable.ActorMovable):
            for actor in self.map.actors:
                try:
                    actor.open()
                    SON_ACHIEVMENT.play()
                except:
                    pass
        return False