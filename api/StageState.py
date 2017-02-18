import enum


class StageState(enum.Enum):
    RUN = 0,
    PAUSE = 1,
    QUIT = 2,
    RESUME = 3,
    INIT = 4
