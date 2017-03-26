from threading import Thread

from game.actors.ActorArrowPlayer import ActorArrowPlayer
from game.actors.ActorArrowSlime import ActorArrowSlime
from game.actors.ActorBlock import ActorBlock
from game.actors.ActorDoor import ActorDoor, ActorDoorWin
from game.actors.ActorPlayer import ActorPlayer
from game.actors.ActorPuzzleSolution import ActorPuzzleSolution
from game.actors.ActorRock import ActorRock
from game.actors.ActorSlime import ActorSlime
from game.actors.ActorSpawnpoint import ActorSpawnpoint
from game.actors.ActorWall import ActorWall


class Loader(Thread):
    """ On enregistre dans run tout les acteurs dont on veut pouvoir les sélectionner via l'invite de commande de l'éditeur"""

    def __init__(self):
        super().__init__()

        self.finish = False

    def run(self):
        # Loading stuff here

        ActorWall.register()
        ActorArrowPlayer.register()
        ActorArrowSlime.register()
        ActorPlayer.register()
        ActorRock.register()
        ActorSpawnpoint.register()
        ActorDoor.register()
        ActorPuzzleSolution.register()
        ActorBlock.register()
        ActorSlime.register()
        ActorDoorWin.register()

        self.finish = True

