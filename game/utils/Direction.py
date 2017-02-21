# Barycentre RPZ
from enum import Enum

from game.utils.Vector import Vector


class DIRECTION(Enum):
    HAUT = Vector(0, -1)
    BAS = Vector(0, 1)
    DROITE = Vector(1, 0)
    GAUCHE = Vector(-1, 0)
    NONE = Vector(0, 0)

