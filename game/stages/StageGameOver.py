
import pygame.mixer

from api.StageMenu import StageMenu
from api.StageManager import StageManager
from api.Timer import Timer
from game.actors.ActorBackground import ActorBackgroundGameOver
from game.utils.Sounds import MUSIC_GAME_OVER
from api.ActorButton import ActorButton
from game.actors.ActorButtonsGameOver import ActorButtonGOmenu, ActorButtonGOquit


class StageGameOver(StageMenu):
    """Stage de game over"""
    def __init__(self):
        super().__init__()
 
    def init(self):
        # ajout fond d'écran, musique et bouttons
        self.map.add_actor(ActorBackgroundGameOver())
        
        if StageManager().music_state:
            pygame.mixer.music.load(MUSIC_GAME_OVER)
            pygame.mixer.music.play()
            

        
        self.map.add_actor(ActorButtonGOmenu())
        self.map.add_actor(ActorButtonGOquit())
        
        
        #placement des bouttons
        
        width = self.screen.get_width() / 4
        

        for index, button in enumerate(self.map.actors):
            if isinstance(button, ActorButton):                         #pour ne pas centrer le fond d'écran au centre de l'écran
                
                button.rect.y = int(self.screen.get_height() / 2)
                button.rect.x =  index * width
                
            else:
                pass
        
        
        #initiation apparition des images
        for actor in self.map.actors:
            if isinstance(actor, ActorButton):
                actor.should_draw = False

        self.add_timer(Timer(8800, self.reset_drawing ))
        
        self.alpha = 0
        self.map.actors[0].sprite.set_alpha(self.alpha)
        self.add_timer(Timer(28, self.fade_in_image, True, 127 ))
            
        
    def fade_in_image(self, *args, **kwargs):
        self.alpha += 2
        self.map.actors[0].sprite.set_alpha(self.alpha)


    def reset_drawing(self, *args, **kwargs):
        for actor in self.map.actors:
            actor.should_draw = True
