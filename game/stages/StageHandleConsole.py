import pygame.mixer

from api.StageAutoManage import StageAutoManage
from api.StageManager import StageManager
from api.StageState import StageState
from game.stages.StageConsole import StageConsole
import game.stages


class StageHandleConsole(StageAutoManage):
    """
    ajout à StageAutoManage la fonction d'utiliser une console, via la touche c pour débuter le stage console, puis une fct execute pour géré l'entrée
    """
    def execute(self, command):
        
        """ Gère les entrées dans l'invite de commande"""
        
        commands = command.split(sep=" ")  # sépare l'entrée en une liste ( escpaces supprimés, remplacés par les ',' de la liste)

        if commands[0] == "debug":
            pass
        elif commands[0] == "hitbox":
            self.draw_hit_box = not self.draw_hit_box
        elif commands[0] == "print":
            print(self.__getattribute__(commands[1]))
            print(self.__getattribute__(commands[1]).__getattribute__(commands[2]))
        elif commands[0] == "menu" or commands[0] == "quit":                        #permet de revenir au menu via l'invite de commande
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()                                           # On éteint la music pour permettre à celle du menu de se lancer (car vérifie si une musique est
            self.state = StageState.QUIT                                            # en trainde jouer ou non)
            StageManager().push(game.stages.StageMainMenu.StageMainMenu())

    def pause(self):        #continuer d'être affiché même en pause
        self.draw()

    def handle_keydown(self, unicode, key, mod):  #gère l'évènement 'c' : lance la console
        if unicode == 'c':
            self.state = StageState.PAUSE
            StageManager().push(StageConsole(self))