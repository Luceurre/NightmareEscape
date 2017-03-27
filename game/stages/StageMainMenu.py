import pygame.mixer

from api.StageManager import StageManager
from api.StageMenu import StageMenu
from game.actors.ActorButtonEdit import ActorButtonEdit
from game.actors.ActorButtonQuit import ActorButtonQuit
from game.actors.ActorButtonSetting import ActorButtonSetting
from game.actors.ActorButtonStart import ActorButtonStart
from game.actors.ActorBackground import ActorBackgroundMenu
from api.ActorButton import ActorButton


class StageMainMenu(StageMenu):
    """ Stage du menu principal"""
    def __init__(self):
        super().__init__()

    def init(self):
        #ajout des différents acteurs ( bouttons ( dans l'ordre ) et fond d'écran)
        
        self.map.add_actor(ActorBackgroundMenu())
        if StageManager().music_state and not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("music/Beginning.ogg")
            pygame.mixer.music.play()

        self.map.add_actor(ActorButtonStart())
        self.map.add_actor(ActorButtonEdit())
        self.map.add_actor(ActorButtonSetting())
        self.map.add_actor(ActorButtonQuit())

        
        # répartis les bouttons au centre de l'écran
        
        height = self.screen.get_height() / (len(self.map.actors) + 3)      

        for index, button in enumerate(self.map.actors):
            if isinstance(button, ActorButton):                         #pour ne pas centrer le fond d'écran au centre de l'écran
                
                button.set_centered_x(self.screen.get_width())          #on centre en x
                button.rect.y = (index + 1) * height                    #et on répartit en y
            else:
                pass
