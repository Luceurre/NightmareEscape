from game.utils.SurfaceHelper import load_image
from game.actors.ActorArrow import ActorArrow
from game.utils.Vector import VECTOR_NULL
from game.utils.Direction import DIRECTION

class ActorArrowSlime(ActorArrow):
    
    '''
    projectile du Slime
    '''
    
    ID = 31
    NAME = "SLIMEARROW"


    def __init__(self, dir=DIRECTION.NONE, velocity=VECTOR_NULL):
        super().__init__(dir, velocity)
        self.damage = 10
        
        
    def load_sprite(self):
        self.sprite = load_image("assets/bullets.png", False).subsurface(208 , 67, 11, 11)