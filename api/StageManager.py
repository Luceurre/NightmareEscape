from api.StageState import StageState
from api.Stage import Stage


class StageManager():
    """Singleton object - Permet la gestion des Stages"""

    singleton = None

    class __StageManager():
        def __init__(self):
            self.stack = []         # liste des stages en cour
            self.music_state = True  # Variable définissant si la musique doit être jouer ( True ) ou non (False ), à appeler à chaque fois qu'on lance une musique

        def update(self):
            for object in self.stack:
                object.update()
                object.draw()

            return self.is_empty

        def push(self, object):
            """ A appeler pour lancer une nouvelle scène"""
            if (object not in self.stack and isinstance(object, Stage)):
                self.stack.append(object)

        def pop(self, index):
            """ retire le stage """
            return self.stack.pop(index)

        def exit(self):
            """ Pour quitter le StageManager, donc le jeu"""
            self.stack = []

        def __iter__(self):
            return iter(self.stack)

        @property
        def is_empty(self):
            return len(self.stack) == 0

    def __new__(cls):
        if (cls.singleton == None):
            cls.singleton = cls.__StageManager()

        return cls.singleton
