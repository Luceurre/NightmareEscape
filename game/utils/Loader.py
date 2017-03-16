from threading import Thread

from game.actors.ActorArrow import ActorArrow
from game.actors.ActorBlock import ActorBlock
from game.actors.ActorDoor import ActorDoor
from game.actors.ActorPlayer import ActorPlayer
from game.actors.ActorPuzzleSolution import ActorPuzzleSolution
from game.actors.ActorRock import ActorRock
from game.actors.ActorSlime import ActorSlime
from game.actors.ActorSpawnpoint import ActorSpawnpoint
from game.actors.ActorWall import ActorWall


class Loader(Thread):

    def __init__(self):
        super().__init__()

        self.finish = False

    def run(self):
        # Loading stuff here

        ActorWall.register()
        ActorArrow.register()
        ActorPlayer.register()
        ActorRock.register()
        ActorSpawnpoint.register()
        ActorDoor.register()
        ActorPuzzleSolution.register()
        ActorBlock.register()
        ActorSlime.register()

        self.finish = True

