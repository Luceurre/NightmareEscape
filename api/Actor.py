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

    ID = 0
    TYPE = "ACTOR"
    REGISTERED = False

    @classmethod
    def register(cls):
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
        self.map = None  # On bypass notre modèle de communication entre acteurs parce que c'est juste pas pratique. -> modèle vue/controller

    def draw(self, screen):
        # L'Actor doit être dessiné ici, si c'est un Actor avec une image, utilise ActorSprite
        pass

    def update(self):
        # L'Actor doit être mis à jour ici -> Mouvement, Collision, etc...
        pass

    def add_timer(self, timer):
        self.timers.append(timer)

    def update_timers(self):
        for index, timer in enumerate(self.timers):
            if timer.update():
                self.timers.pop(index)

    # Quand la map se charge, ou l'acteur -> permet d'éviter la sauvegarde d'élèments inutile et les bugs pickle
    def reload(self, map):
        self.map = map

    # Quand on sauvegarde...
    def unload(self):
        del self.map
        pass

