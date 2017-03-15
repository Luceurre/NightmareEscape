from api.ActorEvent import ActorEvent


class ActorSpawnpoint(ActorEvent):

    ID = 6
    NAME = "SPAWNPOINT"
    def __init__(self, size = (96,96)):
        super().__init__(size)