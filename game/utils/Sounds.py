import pygame.mixer

pygame.mixer.init()

SON_PORTE = pygame.mixer.Sound("sounds/door.ogg")
SON_ACHIEVMENT = pygame.mixer.Sound("sounds/gem.ogg")

MUSIC_MAP = {"level_1" : "music/Eredin.wav", "level_0" : "music/ThesongoftheSwordDancer.wav", "level_2" : "music/ThreeFatGnomes.wav"}
