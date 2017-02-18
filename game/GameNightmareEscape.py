from api.Game import Game
from api.StageManager import StageManager
from game.stages.StageLevel import StageLevel
from game.stages.StageLoadingScreen import StageLoadingScreen


class GameNightmareEscape(Game):
    def __init__(self):
        super().__init__(1400, 800)

        StageManager().push(StageLoadingScreen())