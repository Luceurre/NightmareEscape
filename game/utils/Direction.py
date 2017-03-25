# Barycentre RPZ
from enum import Enum

import math

from game.utils.Vector import Vector


class DIRECTION(Enum):
    HAUT = Vector(0, -1)
    BAS = Vector(0, 1)
    DROITE = Vector(1, 0)
    GAUCHE = Vector(-1, 0)
    NONE = Vector(0, 0)

    
    @classmethod
    def opposite(cls, direction):    #renvoie la direction opposée, ou lève une erreur
        try:
            if direction == cls.HAUT:
                return cls.BAS
            elif direction == cls.BAS:
                return cls.HAUT
            elif direction == cls.GAUCHE:
                return cls.DROITE
            elif direction == cls.DROITE:
                return cls.GAUCHE
            elif direction == cls.NONE:
                return cls.NONE
            else:
                raise ValueError("le vecteur n'est pas une direction")
        except ValueError:
            raise ValueError
        
        

