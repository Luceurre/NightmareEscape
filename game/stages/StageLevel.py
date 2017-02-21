from api.Map import Map
from api.StageAutoManage import StageAutoManage
from game.actors.ActorCollidable import ActorCollidable
from game.actors.ActorPlayer import ActorPlayer
from game.actors.ActorSpawnpoint import ActorSpawnpoint
from game.actors.ActorWall import ActorWall
from game.stages.StageHandleConsole import StageHandleConsole


class StageLevel(StageHandleConsole):
    def __init__(self, level = 1):
        super().__init__()

        self.map = Map.load("level_" + str(level))
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