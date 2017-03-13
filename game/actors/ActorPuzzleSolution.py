from api.ActorEvent import ActorEvent
import game.actors.ActorMovable


class ActorPuzzleSolution(ActorEvent):
    
    NAME = "PUZZLESOLUTION"
    
    def __init__(self):
        super().__init__((64,64))
        
    def interact(self, actor):
        if isinstance(actor, game.actors.ActorMovable.ActorMovable):
            for actor in self.map.actors:
                try:
                    actor.open()
                except:
                    pass
        return False