import enum


class StageState(enum.Enum): #Pour gérer l'état des stage de façon propre
    RUN = 0,
    PAUSE = 1,
    QUIT = 2,
    RESUME = 3,
    INIT = 4
