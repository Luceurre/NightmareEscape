import pygame.mixer

pygame.mixer.init()

""" On enregistre ici les sons/musique dont on pourrait avoir besoin, pas possible de le faire dans les acteurs car sinon bug de pickle ( question de facilité )"""


SON_PORTE = pygame.mixer.Sound("sounds/door.ogg")
SON_ACHIEVMENT = pygame.mixer.Sound("sounds/gem.ogg")

MUSIC_MAP = {"level_1" : "music/Eredin.wav", "level_0" : "music/ThesongoftheSwordDancer.wav", "level_2" : "music/ThreeFatGnomes.wav", "default" : "music/CityofIntrigues.wav"}

MUSIC_GAME_OVER = "music/PaintInBlack.ogg"
