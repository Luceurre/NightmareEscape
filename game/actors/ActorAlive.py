from api.ActorSprite import ActorSprite
from game.utils.Constants import EVENT_EXPLOSION


class ActorAlive(ActorSprite):
    """Un Actor regroupant quelques méthodes et attributs communs à tous les êtres vivants"""
    def __init__(self):
        super().__init__()

        self.should_update = True
        self.should_draw = True
        self.damage = 0
        self.hp = 1
        self.collidable = True
        self.invicible = False
        self.handle_event = True

    def reload(self):
        super().reload()

        self.invicible = False  # Pour régler le bug sur le slime

    def interact(self, actor):
        # Pour éviter que le Joueur prenne des dégâts de ses propres projectiles :)

        to_return = False
        to_return = super().interact(actor)
        if self.team.get_ennemi() == actor.team:
            self.hp -= actor.damage

            return (self.collidable and actor.collidable) or to_return
        else:
            return to_return


    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, heal_point):
        if self.invicible:
            return
        self._hp = heal_point
        if self._hp <= 0:
            self.die()

    def die(self):
        pass

    def handle_userevent(self, event):
        if event.name == EVENT_EXPLOSION:
            if self.team.get_ennemi() == event.team and (event.pos.x - self.rect.x) ** 2 + (event.pos.y - self.rect.y) ** 2 <= event.radius ** 2:
                self.hp -= event.damage
            elif self.team == event.team and (event.pos.x - self.rect.x) ** 2 + (event.pos.y - self.rect.y) ** 2 <= event.radius ** 2:
                self.hp -= event.damage / 4