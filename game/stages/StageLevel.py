from api.Map import Map
from api.StageAutoManage import StageAutoManage
from game.actors.ActorCollidable import ActorCollidable
from game.actors.ActorPlayer import ActorPlayer
from game.actors.ActorWall import ActorWall
from game.stages.StageHandleConsole import StageHandleConsole


class StageLevel(StageHandleConsole):
    def __init__(self, level = 0):
        super().__init__()

        self.player = ActorPlayer()

    def init(self):
        super().init()

        self.map.add_actor(self.player)
        for i in range(2):
            self.map.add_actor(ActorWall())

        self.map.actors[1].rect.x = 200
        self.map.actors[2].rect.y = 200

    def run(self):
        super().run()