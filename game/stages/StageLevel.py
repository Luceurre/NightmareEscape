import pygame.mixer

from api.Map import Map
from api.StageManager import StageManager
from game.actors.ActorGUIBar import ActorGUIBar
from game.actors.ActorPlayer import ActorPlayer
from game.actors.ActorSpawnpoint import ActorSpawnpoint
from game.stages.StageHandleConsole import StageHandleConsole
from game.stages.StageGameOver import StageGameOver
from game.utils.Constants import EVENT_TP, EVENT_GAME_OVER
from game.utils.Sounds import MUSIC_MAP
from api.StageState import StageState


class StageLevel(StageHandleConsole):
    
    """ Stage du jeu"""
    
    def __init__(self, map="level_0"):
        """la base : initialise les trucs classiques de StageHandleConsole, ajoute une map, cherche le spwanpoint et crée le player dessus"""
        super().__init__()
        
        if StageManager().music_state:
            
            self.music_init()


        self.map = Map.load_save(map)                   #chargement de la map
        spawnpoint = self.map.get_actor(ActorSpawnpoint) #et de l'acteur
        if spawnpoint is not None:                      # gère l'existance de spawnpoint
            self.player = ActorPlayer()
            self.player.rect.topleft = spawnpoint.rect.topleft
            self.map.add_actor(self.player)
        else:
            raise NotImplementedError("Erreur la map n'a pas de spawnpoint!")

        # Ensuite ajout de la barre de vie

        self.gui_lifebar = ActorGUIBar(ratio=self.player.hp_max / self.player.hp, color=(255, 0, 0, 255))
        self.gui_lifebar.rect.x = 24
        self.gui_lifebar.rect.y = 24
        self.map.add_actor(self.gui_lifebar)

    def update(self):
        super().update()

        self.gui_lifebar.ratio = self.player.hp / self.player.hp_max
        
    def music_init(self, map_name = "default"):
        if not StageManager().music_state:
            return None
        

        if map_name in MUSIC_MAP.keys():
            pygame.mixer.music.load(MUSIC_MAP[map_name])
            pygame.mixer.music.play()



    def init(self):
        super().init()

    def run(self):
        super().run()

    def handle_userevent(self, event):      #Gère l'usage de porte -> charge nouvelle map et déplace personnage
        if event.name == EVENT_TP: # un nouveau rect pour le perso, une nouvelle map pour le Stage
            actor = event.actor
            actor.rect.x = int(event.spawn_pos.x)
            actor.rect.y = int(event.spawn_pos.y)

            self.unload_gui_and_player()
            self.map.save_in_game()

            self.map = Map.load_save(event.map_name)
            
            self.music_init(event.map_name)
            
            self.map.add_actor(event.actor)
            

            self.load_gui_and_player()  #soit on enlève celui-ci, soit celui du load_gui_and_player()
        
        elif event.name == EVENT_GAME_OVER:
            print("EVENT_GAME_OVER reçu par Stage Level")
            StageManager().push(StageGameOver())
            self.state = StageState.QUIT
            

    def load_gui_and_player(self): # gui = graphical user interface
        """Lalala la fonction est dans le titre..."""
        #self.map.add_actor(self.player)
        self.map.add_actor(self.gui_lifebar)

    def unload_gui_and_player(self):
        """Pour éviter d'avoir 12.000.000.000 de GUI :)"""
        self.map.remove_actor(self.player)
        self.map.remove_actor(self.gui_lifebar)
