import pygame.mixer

from api.Map import Map
from game.actors.ActorPlayer import ActorPlayer
from game.actors.ActorSpawnpoint import ActorSpawnpoint
from game.stages.StageHandleConsole import StageHandleConsole
from game.utils.Constants import EVENT_TP


class StageLevel(StageHandleConsole):
    def __init__(self, map="level_0"):
        super().__init__()
        pygame.mixer.music.load("music/CityofIntrigues.wav")
        pygame.mixer.music.play()
        pygame.mixer.music.queue("music/CommandingtheFury.wav")

        self.map = Map.load_save(map)
        spawnpoint = self.map.get_actor(ActorSpawnpoint)
        if spawnpoint is not None:
            player = ActorPlayer()
            player.rect.topleft = spawnpoint.rect.topleft
            self.map.add_actor(player)
        else:
            self.info("Erreur la map n'a pas de spawnpoint!")

    def init(self):
        super().init()

    def run(self):
        super().run()

    def handle_userevent(self, event):
        if event.name == EVENT_TP:
            actor = event.actor
            actor.rect.x = int(event.spawn_pos.x)
            actor.rect.y = int(event.spawn_pos.y)
            self.map.remove_actor(actor)
            self.map.save()  # devrait appeler save_in_game mais bon en attendant...
            self.map = Map.load_save(event.map_name)
            self.map.add_actor(event.actor)
