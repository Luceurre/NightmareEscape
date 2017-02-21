import pickle
import os
#import api.ActorSprite
import pygame

from api.Logger import *


class Map(Logger):
    def __init__(self):
        self.name = ""
        self.actors = []
        self.rect = pygame.Rect(0, 0, pygame.display.get_surface().get_width(), pygame.display.get_surface().get_height())
        self.type = ""
        self.background = None

    def save(self):
        # Sauvegarde la Map dans le fichier 'name' + .map

        self.info("Saving...")

        file = open("ressources/" + self.name + ".map", 'wb')
        self.unload()

        pickle.dump(self, file)
        self.reload()

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

    def add_actor(self, actor):
        if actor not in self.actors:
            actor.map = self
            self.actors.append(actor)
        else:
            self.log("Tu as deux fois le même Actor! Check si tu as pas une erreur quelque part Renaud...", LOG_LEVEL.ERROR)

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

    def reload(self):
        for actor in self.actors:
            actor.reload(self)

    def unload(self):
        for actor in self.actors:
            actor.unload()

    @classmethod
    def load(cls, name):
        # Charge la Map 'name' avec Pickle, renvoie une instance de Map

        map = None

        try:
            file = open("ressources/" + name + ".map", mode='br')
            map =  pickle.Unpickler(file).load()
        except:
            map = Map()
            map.name = name

        map.reload()

        return map


