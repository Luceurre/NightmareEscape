import pygame.mixer

from api.StageAutoManage import StageAutoManage
from api.StageManager import StageManager
from game.utils.Sounds import MUSIC_GAME_OVER


class StageGameOver(StageAutoManage):
    """
    Stage de game over
    """
    def __init__(self):
        super().__init__()

        if StageManager().music_state:
            pygame.mixer.music.load(MUSIC_GAME_OVER)
            pygame.mixer.music.play()
            