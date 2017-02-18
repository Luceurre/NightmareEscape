import pygame
from api.StageManager import StageManager
from api.StageState import StageState

from api.Logger import Logger, LOG_LEVEL


class Game(Logger):
    """Les bases de la logique du jeu... Si on veut modifier quelque chose qui touche tout le jeu, on le fait ici"""

    def __init__(self, width=640, height=480, log_level=LOG_LEVEL.INFO, framerate=120):
        pygame.init()

        self.stage_manager = StageManager()
        self.screen = pygame.display.set_mode((width, height))
        self.framerate = framerate
        self.clock = pygame.time.Clock()
        Logger.set_log_level(log_level)

    def start(self):
        """Called when you want the game to start -> unless you're using multi-threading, you won't be able to do
        anything until your game ends """

        if self.screen == None:
            self.error("Ecran non defini", LOG_LEVEL.ERROR)
            StageManager().exit()

        while not self.stage_manager.is_empty:
            self.clock.tick(self.framerate)
            self.screen.fill((0, 0, 0))

            for index, stage in enumerate(self.stage_manager):
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

        pygame.quit()

