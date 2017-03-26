from game.actors.ActorArrow import ActorArrow
from game.utils.SurfaceHelper import load_image
from game.utils.Vector import VECTOR_NULL
from game.utils.Direction import DIRECTION


class ActorArrowPlayer(ActorArrow):
    
    '''
    projectile du Slime
    '''
    
    ID = 30
    NAME = "PLAYERARROW"


    def __init__(self, dir=DIRECTION.NONE, velocity=VECTOR_NULL):
        
        super().__init__(dir, velocity)
        self.damage = 10
        
        
        
        
    def load_sprite(self):
        self.sprite = load_image("assets/bullet.png")
        