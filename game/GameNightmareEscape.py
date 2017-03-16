from api.Game import Game
from api.StageManager import StageManager
from game.stages.StageLevel import StageLevel
from game.stages.StageLoadingScreen import StageLoadingScreen
from game.utils.Constants import *


class GameNightmareEscape(Game):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, framerate=60) # Appel de l'initialisation de Game -> du jeu

        StageManager().push(StageLoadingScreen())                   # on lance la scène de chargement - > première scène, sinon le jeu se fermerait (tout simplement ))