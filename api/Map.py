import pickle

from api.Actor import Actor
from api.EnumTeam import EnumTeam
from api.Logger import *


class Map(Logger):
    """Classe permettant le dialogue entre les Actors et le Stage.
    Contient quelques méthodes permettant un dialogue précis et rapide.
    Permet également la sauvegarde grossière du jeu.
    Utiliser Map.load(name) pour l'instancier."""

    RESSOURCES_PATH = "ressources/"
    SAVES_PATH = "saves/"

    def __init__(self):
        self.name = ""
        self.actors = []
        "self.sounds = []"
        self.stable = True  # Je voulais coder un système qui évite de re-trier les tableaux tant que map.actors n'est
        # pas modifié mais je ne pense pas que c'est pertinent. Renaud ton avis ?

        # Supprimé car apparement d'aucune utilité ?
        # self.rect = pygame.Rect(0, 0, pygame.display.get_surface().get_width(),
        #                        pygame.display.get_surface().get_height())

    def save(self):
        # Sauvegarde la Map dans le fichier 'name' + .map
        
        
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

    def save_in_game(self):
        # Sauvegarde la Map dans le fichier 'name' + .map
        
        
        self.info("Saving...")
        file = open("saves/" + self.name + ".map", 'wb')
        
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

    def get_actors_collide(self, rect, actors_a_eviter=[]):
        """Renvoie la liste des Actors appartenant à Map dont le rect est en collision avec rect. Le paramètre
        actor_a_eviter permet d'éviter de renvoyer l'Actor à qui appartient le rect car en effet celui est forcément
        en collision avec lui-même. #up : actor_a_eviter sous forme d'une liste, car sinon n'a aucun sens (car sinon on ne peut mettre que self)

        Renvoie [] si aucun Actor n'est trouvé."""

        actors = []
        for actor in self.actors:
            ajouter = True
            for ActeurAEviter in actors_a_eviter:
                if ActeurAEviter == actor:
                    ajouter = False
            if actor.rect.colliderect(rect) and ajouter:
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

    def get_closest_ennemi(self, rect, range=10 ** 8, ennemi_team=EnumTeam.PLAYER_TEAM):
        """Renvoie l'Actor de team opposé à team le plus proche de la position."""

        min_distance = range ** 2
        closest_ennemi = None

        (x, y) = rect.center

        for actor in self.actors:
            distance = (x - actor.rect.centerx) ** 2 + (y - actor.rect.centery) ** 2
            if distance < min_distance and actor.team == ennemi_team and actor.etre_vivant:
                min_distance = distance
                closest_ennemi = actor

        return closest_ennemi


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

    def __iter__(self):
        """Fait que :
        for i in map.actors <=> for i in map
        Permet de rendre self.actors protected voire private ?"""

        return self.actors

    def reload(self):
        """Permet de recharger l'ensemble des attributs de Map qui ne sont pas supportés par Pickle, comme par exemple
        les sprites des Actors."""

        for actor in self.actors:
            actor.reload()

    def unload(self):
        """Permet de supprimer l'ensemble des attributs de Map qui ne sont pas supportés par Pickle."""

        for actor in self.actors:
            actor.unload()

    @classmethod
    def load(cls, path):
        """Charge la Map 'name' avec Pickle, renvoie une instance de Map, si le fichier ressources/'name'.map
        n'existe pas, une nouvelle Map est créée dont le nom est 'name'. Il faudrait modifier cette méthode pour
        pouvoir charger des sauvegardes également!

        Le paramètre 'name' est une chaine de caractères."""

        file = open(path + ".map", mode='br')
        map = pickle.Unpickler(file).load()
        map.reload()

        return map

    @classmethod
    def load_editor(cls, name):
        """Charge la Map 'name' du dossier RESSOURCES_PATH. Renvoie une map vide portant le nom 'name' si le fichier
        n'existe pas."""

        try:
            map = cls.load(cls.RESSOURCES_PATH + name)
        except FileNotFoundError:
            map = Map()
            map.name = name

        return map

    @classmethod
    def load_save(cls, name):
        """Charge la Map 'name' du dossier SAVES_PATH. Le fichier provenant du dossier RESSOURCES_PATH est renvoyer si
        le premier n'est pas trouvé."""

        try:
            map = cls.load(cls.SAVES_PATH + name)
        except FileNotFoundError:
            map = cls.load_editor(name)

        return map
