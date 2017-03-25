
from api.StageMenu import StageMenu
import game.actors.ActorButtonReturn
from game.actors.ActorButtonMusic import ActorButtonMusic
from game.actors.ActorBackground import ActorBackgroundSettings
from api.ActorButton import ActorButton


class StageMenuSetting(StageMenu): 
    
    """ Menu permettant à changer des options ( En fait c'est assez ouvert : ici seule possibilité est la musique )"""
    
    def __init__(self):
        super().__init__()
        
        
    def init(self):
        """ copie conforme de StageMainMenu, donc pour plus de commentaires..."""
        
        self.map.add_actor(ActorBackgroundSettings())
        
        #self.map.add_actor(ActorButtonSettingKeys()) # enlevé par révision à la baisse des ambitions
        
        self.map.add_actor(game.actors.ActorButtonReturn.ActorButtonReturn())
        self.map.add_actor(ActorButtonMusic())
        
        height = self.screen.get_height() / (len(self.map.actors) + 2 + 2)
        
        for index, button in enumerate(self.map.actors):
            if isinstance(button, ActorButton):
                
                button.set_centered_x(self.screen.get_width())
                button.rect.y = (index + 1) * height
            else:
                pass
        
