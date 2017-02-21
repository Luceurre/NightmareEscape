from api.ActorEvent import ActorEvent


class ActorSpawnpoint(ActorEvent):

    ID = 6
    NAME = "SPAWNPOINT"
    def __init__(self):
        super().__init__((64, 64))