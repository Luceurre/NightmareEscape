from game.actors.ActorTile import ActorTile


class ActorTileCollidable(ActorTile):
    def reload(self):
        super().reload()

        self.collidable = True
