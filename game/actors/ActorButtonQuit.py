from api.ActorButton import ActorButton
from api.StageManager import StageManager


class ActorButtonQuit(ActorButton):
    def __init__(self):
        super().__init__(files_prefix="button_quit", label="quit")

    def execute(self):
        StageManager().exit()