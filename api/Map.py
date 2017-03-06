import pickle

import pygame

from api.Actor import Actor
from api.Logger import *


class Map(Logger):
    def __init__(self):
        self.name = ""
        self.actors = []
        self.rect = pygame.Rect(0, 0, pygame.display.get_surface().get_width(),
                                pygame.display.get_surface().get_height())
        self.type = ""
        self.background = None

    def save(self):
        # Sauvegarde la Map dans le fichier 'name' + .map
        # à modifier ! 2 cas : l'éditeur d'une part, la sauvegarde du joueur d'autre part!
        self.info("Saving...")
        file = open("ressources/" + self.name + ".map", 'wb')

        # On enlève tout les attributs de Map qui ne peuvent pas être "Pickle"
        self.unload()

        # Code enlevé parce que l'utilisation abusée des try/except ne permet pas la gestion des erreurs de façon propre
        """
        self.info("Erreur lors de la sauvegarde la carte!")
        print("Unexpected error:", sys.exc_info()[0])
        """

        pickle.dump(self, file)
        # Puis on les recharges parce que le jeu ne peut pas fonctionner sans eux!
        self.reload()

    def unload_sprites(self):
        """Appelle la méthode unload_sprite() de tous les Actors de la map

        Cette méthode doit être appelée avant la sauvegarde de la Map, car les sprites des Actors sont de type
        pygame.Surface et ne sont pas supportés par Pickle."""
        for actor in self.actors:
            actor.unload_sprite()

    def get_actor_at(self, x, y):
        """Renvoie l'Actor appartenant à Map ayant le z le plus petit (affiché en priorité)
        dont le point de coordonnés (x, y) est en collision avec son rect.

        Renvoie None si aucun Actor n'est trouvé."""

        for actor in self.actors:
            if actor.rect.collidepoint(x, y):
                return actor

        return None

    def get_actors_at(self, x, y):
        """Fait la même chose que get_actor_at mais renvoie la liste de tous les Actors appartenant à Map dont le
        rect est en collision avec le point (x, y).

        Renvoie [] si aucun Actor n'est trouvé."""

        actors = []
        for actor in self.actors:
            if actor.rect.collidepoint(x, y):
                actors.append(actor)

        return actors

    def get_actors_collide(self, rect, actor_a_eviter=None):
        """Renvoie la liste des Actors appartenant à Map dont le rect est en collision avec rect. Le paramètre
        actor_a_eviter permet d'éviter de renvoyer l'Actor à qui appartient le rect car en effet celui est forcément
        en collision avec lui-même.

        Renvoie [] si aucun Actor n'est trouvé."""

        actors = []
        for actor in self.actors:
            if actor.rect.colliderect(rect) and actor_a_eviter != actor:
                actors.append(actor)

        return actors

    def get_actor(self, class_name):
        """Renvoie le premier Actor (toujours trié par z du plus petit au plus grand) appartenant à Map dont le
        type est le paramètre class_name.

        Exemple: map.get_actor(ActorPlayer) et non map.get_actor(ActorPlayer())

        Renvoie None si aucun Actor n'est trouvé et renvoie une instance de class_name sinon."""

        for actor in self.actors:
            if type(actor) == class_name:
                return actor

        return None

    def add_actor(self, actor):
        """Ajoute une instance d'Actor à la Map, l'Actor devient alors recensé et est disponible dans toutes les
        méthodes de Map.
        La méthode check que l'actor n'est pas déjà enregistré et que c'est bien une instance d'Actor. Lève l'erreur
        ValueError dans ces cas."""

        if isinstance(actor, Actor):
            if actor not in self.actors:
                actor.map = self
                self.actors.append(actor)
            else:
                raise ValueError("L'Actor est déja enregistrée dans cette instance de Map!")
        else:
            raise ValueError("Le paramètre n'est pas une instance d'Actor!")

    def remove_actor(self, actor):
        try:
            self.actors.remove(actor)
        except:
            self.warning("L'acteur que tu veux supprimer n'existe pas")

    def is_at(self, rect, type=Actor):
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
            actor.reload()
            actor.map = self

    def unload(self):
        for actor in self.actors:
            actor.unload()

    @classmethod
    def load(cls, name):
        """Charge la Map 'name' avec Pickle, renvoie une instance de Map, si le fichier ressources/'name'.map
        n'existe pas, une nouvelle Map est créée dont le nom est 'name'. Il faudrait modifier cette méthode pour
        pouvoir charger des sauvegardes également!

        Le paramètre 'name' est une chaine de caractères."""

        try:
            file = open("ressources/" + name + ".map", mode='br')
            map = pickle.Unpickler(file).load()
        except:
            map = Map()
            map.name = name

        map.reload()

        return map
