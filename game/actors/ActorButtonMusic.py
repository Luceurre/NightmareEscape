import pygame.mixer

from api.ActorButton import ActorButton
from api.StageManager import StageManager
from game.utils.Constants import WINDOW_HEIGHT, WINDOW_WIDTH


class ActorButtonMusic(ActorButton):


    def __init__(self):
        self.fct_suffixe()       #On cherche si la musique est on ou off afin de choisir le bon boutton
        
        super().__init__(files_prefix="musique" + self.suffixe)  # initialisation de la musique, cahrge les fichiers musiqueON ou musique OFF selon le suffixe
        
        self.button_job_leave = False       # Afin qu'appuyer sur le boutton ne fasse pas quitter le stage, donc le jeu ( car n'en relance pas d'autre)
        
    def execute(self):      # On inverse la constante lorsque le boutton est activé (certes dans ce cas ce n'est plus une constante, mais bon...)
        super().execute()
        
        StageManager().music_state = not StageManager().music_state
        
        if not StageManager().music_state:
            pygame.mixer.music.stop()
        else:
            pygame.mixer.music.play()
        
        self.__init__()  # On change de boutton - > On vers OFF, ou inverse
        
        height = WINDOW_HEIGHT / 7
        
        self.set_centered_x(WINDOW_WIDTH)   # Il faut recentrer le boutton
        
        self.rect.y = (3) * height
        
    def fct_suffixe(self):      #On cherche si la musique est on ou off afin de choisir le bon boutton
        if StageManager().music_state : 
            self.suffixe = "ON"
        else:
            self.suffixe = "OFF"
        
        