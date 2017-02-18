import pickle
import os
#import api.ActorSprite
from api.Logger import *


class Map(Logger):
    def __init__(self):
        self.name = ""
        self.actors = []

    def save(self):
        # Sauvegarde la Map dans le fichier 'name' + .map
        file = open("ressources/" + self.name + ".map", 'wb')



        pickle.dump(self, file)

    def unload_sprites(self):
        for actor in self.actors:
            actor.unload_sprite()

    def get_at(self, rect):
        rects = (actor.rect for actor in sorted(self.actors, key=lambda actor: isinstance(actor, object), reverse=True))
        return rect.collidelistall(rects)

    def get_actor_at(self, x, y):
        for actor in self.actors:
            if actor.rect.collidepoint(x, y):
                return actor

        return None

    def remove_actor(self, actor):
        try:
            self.actors.remove(actor)
        except:
            self.warning("L'acteur que tu veux supprimer n'existe pas")

    def is_at(self, rect, type=object):
        # rects = [actor.rect for actor in sorted(self.actors, key=lambda actor: isinstance(actor, type), reverse=True)]
        rects = []
        for actor in self.actors:
            if isinstance(actor, type):
                rects.append(actor.rect)

        return rect.collidelist(rects)

    def __iter__(self):
        return self.actors

    @classmethod
    def load(cls, name):
        # Charge la Map 'name' avec Pickle, renvoie une instance de Map
        try:
            file = open("ressources/" + name + ".map", mode='br')
            return pickle.Unpickler(file).load()
        except:
            map = Map()
            map.name = name
            return map


