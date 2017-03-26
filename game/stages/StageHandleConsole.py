import pygame.mixer

from api.StageAutoManage import StageAutoManage
from api.StageManager import StageManager
from api.StageState import StageState
from game.actors.ActorPlayer import ActorPlayer
from game.stages.StageConsole import StageConsole
import game.stages
from game.utils.Constants import EVENT_TP
from game.utils.Vector import Vector


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
        elif commands[0] == "tp":
            event = pygame.event.Event(pygame.USEREVENT, name=EVENT_TP, map_name=commands[1],
                                       spawn_pos=Vector(700, 700), actor=self.map.get_actor(ActorPlayer))
            pygame.event.post(event)
        elif commands[0] == "invicible":
            self.map.get_actor(ActorPlayer).invicible = not self.map.get_actor(ActorPlayer).invicible

    def pause(self):        #continuer d'être affiché même en pause
        self.draw()

    def handle_keydown(self, unicode, key, mod):  #gère l'évènement 'c' : lance la console
        super().handle_keydown(unicode,key,mod)
        
        if unicode == 'c':
            self.state = StageState.PAUSE
            StageManager().push(StageConsole(self))