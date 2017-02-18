import pygame
import api.Game
from api.Logger import Logger, LOG_LEVEL
from test.StageInit import StageInit


class GameTest(api.Game.Game, Logger):
    def __init__(self):
        super().__init__(640, 480, LOG_LEVEL.DEBUG)

        # On définit le niveau de LOG de l'application
        self.stage_manager.push(StageInit(self.screen))

        self.start()
