from api.ActorSprite import ActorSprite


class ActorCollidable(ActorSprite):
    def __init__(self):
        super().__init__()

        self.collidable = True

    def reload(self):
        super().reload()

        self.collidable = True

    def interact(self, actor):    
        return (actor.collidable and self.collidable)
