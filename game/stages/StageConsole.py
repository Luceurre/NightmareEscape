import pygame

from api.StageAutoManage import StageAutoManage
from api.StageState import StageState


class StageConsole(StageAutoManage):
    """ Stage appelé en appuyant sur 'c' , crée une invite de commande qui s'affiche en haut à gauche, qui s'éteint en retournant la commande en appuyant sur ESPACE"""
    
    def __init__(self, previous_stage):
        super().__init__()
        self.console = ""
        self.font = pygame.font.Font("freesansbold.ttf", 15)
        self.previous_stage = previous_stage

    def draw(self):
        super().draw()

        self.screen.blit(self.font.render(self.console, True, (255, 0, 255)), (0, 0))   #colle surface générée par render ( chaine, aliasing, couleur, bckgrnd ) sur écran

    def quit(self):
        super().quit()

        self.previous_stage.state = StageState.RESUME       # relance stage précédent
        self.previous_stage.execute(self.console)           # appelle la fonction execute su stage précédent avec pour argument la strg de la console

    def handle_keydown(self, unicode, key, mod):
        if key == pygame.K_RETURN:                          # permet de valider l'entrée
            self.state = StageState.QUIT
        elif key == pygame.K_BACKSPACE:                     # permet d'utiliser la touche  <----
            self.console = self.console[:-1]
        else:
            self.console += unicode

