from api.EnumAuto import EnumAuto
from api.EventHandler import EventHandler
from api.Logger import Logger
from game.utils.Register import Register


class HANDLE_EVENT_PRIORITY(EnumAuto):
    VERY_LOW = ()
    LOW = ()
    NORMAL = ()
    HIGH = ()
    VERY_HIGH = ()

    def __lt__(self, other):
        return self.value < other.value


class Actor(EventHandler, Logger):
    """Le couteau suisse des classes. Permet la réunion entre l'image et la logique. Possède également quelques
    méthodes pratiques pour la sauvegarde, la communication, l'édition, etc..."""

    ID = 0  # à supprimer ! le système de NAME est bien plus cohérent.
    TYPE = "ACTOR"
    REGISTERED = False
    NAME = ""

    @classmethod
    def register(cls):
        """Utiliser cette méthode pour rendre votre Actor visible dans l'éditeur.
        Tips: à utiliser dans game.utils.Loader, cette classe est là pour ça!"""
        if cls.REGISTERED:
            return False
        else:
            Register().add_actor(cls.ID, cls)
            cls.REGISTERED = True
            return True

    def __init__(self):
        self.handle_event = False
        self.handle_event_priority = HANDLE_EVENT_PRIORITY.NORMAL
        self.should_draw = False
        self.z = 0
        self.should_update = False
        self.timers = []
        self.map = None  # C'est le lien entre les Actors et le Stage.

    def draw(self, screen):
        """L'Actor doit être dessiné ici, si c'est un Actor avec une image, utilise ActorSprite"""
        pass

    def update(self):
        """L'Actor doit être mis à jour ici -> Mouvement, Collision, etc..."""
        pass

    def add_timer(self, timer):
        self.timers.append(timer)

    def update_timers(self):
        for index, timer in enumerate(self.timers):
            if timer.update():
                self.timers.pop(index)

    def reload(self):
        """Quand la map se charge, ou l'acteur -> permet d'éviter la sauvegarde d'élèments inutile et les bugs pickle"""
        pass

    def unload(self):
        """Suppression de  l'ensemble des attributs non supporté par Pickle."""

        # Je le remets ici en commentaire pour ne pas chercher trop longtemps si ça ne fonctionne plus.
        # del self.map
        pass
