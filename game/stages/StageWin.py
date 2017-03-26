import pygame.mixer
import os

from api.StageAutoManage import StageAutoManage
from api.StageMenu import StageMenu
from api.StageManager import StageManager
from api.Timer import Timer
from game.actors.ActorBackground import ActorBackgroundWin, ActorCredits
from game.utils.Sounds import MUSIC_WIN
from game.stages.StageMainMenu import StageMainMenu
from api.StageState import StageState




class StageWin(StageAutoManage):
    '''
    Stage du la victoire, est appellé via l'event EVENT_WIN
    '''


    def __init__(self):
        super().__init__()
        
        self.map.add_actor(ActorBackgroundWin())
        
        if StageManager().music_state:
            pygame.mixer.music.load(MUSIC_WIN)
            pygame.mixer.music.play()
        
    
        self.map.add_actor(ActorCredits())
        self.alpha = 0
        self.map.actors[1].sprite.set_alpha(self.alpha)
        self.add_timer(Timer(56, self.fade_in_image, True, 63))
            
        
    def fade_in_image(self, *args, **kwargs):
        self.alpha += 2
        self.map.actors[1].sprite.set_alpha(self.alpha)
        
    def handle_keydown(self, unicode, key, mod):
        pygame.mixer.music.stop()
        StageManager().push(StageMainMenu())
        self.state = StageState.QUIT
        
