from game.actors.ActorTile import ActorTile


class ActorTileCollidable(ActorTile):
    def reload(self):
        super().reload()

        self.collidable = True

    
    def interact(self, actor):    
        return (actor.collidable and self.collidable)

