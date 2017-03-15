import pygame

from api.ActorSprite import ActorSprite
#from game.utils.Constants import WINDOW_WIDTH, WINDOW_HEIGHT


class ActorBackgroundMenu(ActorSprite):
    def __init__(self):
        super().__init__()
        
        
    
    def load_sprite(self):
        super().load_sprite()
        
        
        self.sprite = pygame.image.load("assets/backgrounds/MenuScreen.png").convert()
        
        

class ActorBackgroundSettings(ActorSprite):
    def __init__(self):
        super().__init__()
        
        
    def load_sprite(self):
        super().load_sprite()
        
        self.sprite = pygame.image.load("assets/backgrounds/OptionScreen.png").convert()

        
class ActorBackgroundGameOver(ActorSprite):
    def __init__(self):
        super().__init__()
    
        
    def load_sprite(self):
        super().load_sprite()
        
        self.sprite = pygame.image.load("assets/backgounds/GameOver.png")


class ActorBackgroundPlay(ActorSprite):
    def __init__(self):
        super().__init__()
    
    
    def load_sprite(self):
        super().load_sprite()
        
        self.sprite = pygame.image.load("assets/backgrounds/PlayScreen.png")