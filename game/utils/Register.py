from api.Logger import Logger


class Register:
    singleton = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(Register.singleton, Register.__Register):
            Register.singleton = Register.__Register()

        return Register.singleton

    class __Register(Logger):
        # Enregister par TYPE, ID
        def __init__(self):
            self.__stack = {}

        def add(self, type, id, object):
            if type not in self.__stack.keys():
                self.__stack[type] = {}

            if id not in self.__stack[type].keys() and object not in self.__stack[type].values():
                self.__stack[type][id] = object
            else:
                self.warning("Tu essayes d'enregister deux fois le même objet ou au même id")

        def get(self, type, id):
            if type not in self.__stack.keys() or id not in self.__stack[type].keys():
                self.info("L'objet n'existe pas!")
                return None
            else:
                return self.__stack[type][id]

        def add_sprite(self, id, sprite):
            self.add("SPRITE", id, sprite)

        def get_sprite(self, id):
            return self.get("SPRITE", id)

        def add_actor(self, id, actor):
            self.add("ACTOR", id, actor)

        def get_actor(self, id):
            return self.get("ACTOR", id)

        def get_actor_by_name(self, name):
            for actor in self.__stack["ACTOR"].values():
                if actor.NAME == name:
                    return actor


