from game.actors.ActorTile import ActorTile


class ActorTileCollidable(ActorTile):
    def __init__(self, path, pos, width, height):
        super().__init__(path, pos, width, height)
        self.collidable = True

    def reload(self):
        super().reload()

        self.collidable = True

    
    def interact(self, actor):    
        return (actor.collidable and self.collidable)

