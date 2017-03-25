import pygame.mixer

from api.StageAutoManage import StageAutoManage
from api.StageManager import StageManager


class StageGameOver(StageAutoManage):
    """
    Stage de game over
    """
    def __init__(self):
        
        if StageManager().music_state:
			pygame.mixer.music.load(MUSIC_GAME_OVER)
			pygame.mixer.music.play()
            