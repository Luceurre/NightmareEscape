from api.StageManager import StageManager
from api.StageState import StageState

from api import Stage
from test.StageMenu import StageMenu


class StageInit(Stage.Stage):
    def init(self):
        StageManager().push(StageMenu(self.screen))
        self.state = StageState.QUIT

        self.warning("Ton programme ne fait actuellement rien...")
