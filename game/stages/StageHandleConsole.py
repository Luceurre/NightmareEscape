from api.StageAutoManage import StageAutoManage
from api.StageManager import StageManager
from api.StageState import StageState
from game.stages.StageConsole import StageConsole


class StageHandleConsole(StageAutoManage):
    def execute(self, command):
        pass

    def pause(self):
        self.draw()

    def handle_keydown(self, unicode, key, mod):
        if unicode == 'c':
            self.state = StageState.PAUSE
            StageManager().push(StageConsole(self))