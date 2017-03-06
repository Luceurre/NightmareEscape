from api.ActorSprite import ActorSprite


class ActorCollidable(ActorSprite):
    def __init__(self):
        super().__init__()

        self.collidable = True

    def reload(self):
        super().reload()

        self.collidable = True
