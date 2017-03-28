import pygame

from api.Logger import Logger, LOG_LEVEL
from api.StageManager import StageManager
from api.StageState import StageState


class Game(Logger):
    """Les bases de la logique du jeu... Si on veut modifier quelque chose qui touche tout le jeu, on le fait ici"""

    CURRENT_STAGE = None

    def __init__(self, width=640, height=480, log_level=LOG_LEVEL.INFO, framerate=120,
                 fullscreen=False):  # Initialisation du jeu, On initialise pygame, on crée l'écran
        pygame.init()
        pygame.mixer.init()

        if fullscreen:
            flags = pygame.FULLSCREEN
        else:
            flags = pygame.NOFRAME

        self.stage_manager = StageManager()
        # assert not pygame.display.mode_ok((width, height), flags)
        self.screen = pygame.display.set_mode((width, height), flags)

        self.framerate = framerate
        self.clock = pygame.time.Clock()                                    #Création d'un système temporel -> pour géré certains trucs selon temps ( ex : vitesse )
        Logger.set_log_level(log_level)
        

    def start(self):
        """Called when you want the game to start -> unless you're using multi-threading, you won't be able to do
        anything until your game ends """

        """ Jeu fonctionne selon succesion de Stages ( comme un pièce de théâtre ) -> toutes les scènes se déroulent ici: StageManager gère le nombre de scènes en cours
        la boucle qui suit active seulement les scènes selon leurs état ( StageState ) """
        
        if self.screen == None:
            self.error("Ecran non defini", LOG_LEVEL.ERROR)
            StageManager().exit()

        while not self.stage_manager.is_empty:
            self.clock.tick(self.framerate)
            self.screen.fill((0, 0, 0))         #écran est noir, on colle ensuite le stage et les images des acteurs par dessus

            for index, stage in enumerate(self.stage_manager): # Appelle fct correspondant à ce que le Stage doit faire selon son état ( quit() par exemple ne fait généralement rien)
                type(self).CURRENT_STAGE = stage
                if stage.state == StageState.RUN:
                    stage.run()
                elif stage.state == StageState.PAUSE:
                    stage.pause()
                elif stage.state == StageState.RESUME:
                    stage.state = StageState.RUN
                    stage.resume()
                elif stage.state == StageState.INIT:
                    stage.state = StageState.RUN
                    stage.init()
                elif stage.state == StageState.QUIT:
                    self.stage_manager.pop(index)
                    stage.quit()
            pygame.display.update()

        pygame.mixer.quit()                             # Plus de 'zic
        pygame.quit()                                   # le jeu est fini :)
        print("Done")
