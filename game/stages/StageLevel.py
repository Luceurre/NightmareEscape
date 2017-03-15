import pygame.mixer

from api.Map import Map
from game.actors.ActorGUIBar import ActorGUIBar
from game.actors.ActorPlayer import ActorPlayer
from game.actors.ActorSpawnpoint import ActorSpawnpoint
from game.stages.StageHandleConsole import StageHandleConsole
from game.utils.Constants import EVENT_TP
from game.utils.Sounds import MUSIC_MAP


class StageLevel(StageHandleConsole):
    def __init__(self, map="level_0"):
        super().__init__()
        pygame.mixer.music.load("music/CommandingtheFury.wav")
        pygame.mixer.music.play()
        self.music_init()


        self.map = Map.load_save(map)
        spawnpoint = self.map.get_actor(ActorSpawnpoint)
        if spawnpoint is not None:
            self.player = ActorPlayer()
            self.player.rect.topleft = spawnpoint.rect.topleft
            self.map.add_actor(self.player)
        else:
            raise NotImplementedError("Erreur la map n'a pas de spawnpoint!")

        self.gui_lifebar = ActorGUIBar(ratio=self.player.hp_max / self.player.hp, color=(255, 0, 0, 255))
        self.gui_lifebar.rect.x = 24
        self.gui_lifebar.rect.y = 24
        self.map.add_actor(self.gui_lifebar)

    def update(self):
        super().update()

        self.gui_lifebar.ratio = self.player.hp / self.player.hp_max
        
    def music_init(self):
        if not pygame.mixer.music.get_busy():
        
            pygame.mixer.music.load("music/CommandingtheFury.wav")
            pygame.mixer.music.play()
        
        
        pygame.mixer.music.queue("music/CityofIntrigues.wav")
        pygame.mixer.music.queue("music/OurPath.wav")
            


    def init(self):
        super().init()

    def run(self):
        super().run()

    def handle_userevent(self, event):      #Gère l'usage de porte -> charge nouvelle map et déplace personnage
        if event.name == EVENT_TP:
            actor = event.actor
            actor.rect.x = int(event.spawn_pos.x)
            actor.rect.y = int(event.spawn_pos.y)
            self.map.remove_actor(actor)
            self.map.save_in_game()
            self.map = Map.load_save(event.map_name)
            try :
                pygame.mixer.music.load(MUSIC_MAP[event.map_name])
                pygame.mixer.music.play()
            except:
                pass
            self.music_init()
            self.map.add_actor(event.actor)
