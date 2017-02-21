from api.Game import Game
from api.StageManager import StageManager
from game.stages.StageLevel import StageLevel
from game.stages.StageLoadingScreen import StageLoadingScreen
from game.utils.Constants import *


class GameNightmareEscape(Game):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT)

        StageManager().push(StageLoadingScreen())