from game.actors.ActorMovable import ActorMovable
from game.utils.SurfaceHelper import load_image

class ActorBlock(ActorMovable):
    
    NAME = "BLOCK"
    ID = 1
    
    def __init__(self):
        super().__init__()
        
    def load_sprite(self):
        super().load_sprite()
        
        self.sprite = load_image("assets/block.png")
    