from game.actors.ActorSlime import ActorSlime
from game.utils.Register import Register


class ActorBigSlime(ActorSlime):
    NAME = "BIGSLIME"
    ID = 238

    WIDTH = 384
    HEIGHT = 384
    FILE = "assets/slime_red_384.png"

    REGISTERED = False
    
    def __init__(self):
        super().__init__()
        self.hp = 200
        
    def reload(self):
        super().reload()
        self.hp = 200