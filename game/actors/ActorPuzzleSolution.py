from api.ActorEvent import ActorEvent
import game.actors.ActorMovable
from game.utils.Sounds import SON_ACHIEVMENT


class ActorPuzzleSolution(ActorEvent):
    
    ID = 8
    NAME = "PUZZLESOLUTION"
    
    def __init__(self, size = (96, 96)):
        super().__init__(size)
        
    def interact(self, actor):
        if isinstance(actor, game.actors.ActorMovable.ActorMovable):
            for actor in self.map.actors:
                try:
                    actor.open()
                except:
                    pass
        return False