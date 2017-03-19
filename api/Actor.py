from api.EnumAuto import EnumAuto
from api.EnumTeam import EnumTeam
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
    méthodes pratiques pour la sauvegarde, la communication, l'édition, etc...
    
    PS: sinon on peut se référé à la description du but d'un acteur dans le Stage"""

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
        self.handle_event = False   # coule de source
        self.handle_event_priority = HANDLE_EVENT_PRIORITY.NORMAL
        self.should_draw = False    # Savoir si l'actuer doit être dessiné sur l'écran durant la boucle draw
        self.z = 0                  # Pour savoir l'ordre dans lequel sont dessiné les acteurs (ex : pour pas que le sol se retrouve au dessus du joueur )
        self.should_update = False  # Variable: est changée durant la boucle event, pour ensuite que l'acteur soit maj durant la boucle update
        self.timers = []
        self.map = None  # C'est le lien entre les Actors et le Stage.
        self.team = EnumTeam.NEUTRAL_TEAM  # Permet de savoir si deux Actors sont ennemies

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

    def interact(self, actor):
        """Nouvelle fonction permettant le dialogue entre 2 Actors.
        Exemple: L'ActorPlayer se déplace, il va demander à tous les Actors qu'ils croisent si ils intéragissent avec
        lui. Dans le cas d'un mur, True est renvoyé et l'ActorPlayer ne se déplace pas, dans le cas d'une boite à pousser
        True est également renvoyé mais la boite peut tout de même faire se déplacer l'ActorPlayer en overridant son
        déplacement.

        Prend une instance d'Actor en paramètre, renvoie True quand il y a une intéraction quelqueconque, False sinon."""

        return False
