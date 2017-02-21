from api.StageAutoManage import StageAutoManage
from api.StageManager import StageManager
from api.StageState import StageState
from game.stages.StageConsole import StageConsole


class StageHandleConsole(StageAutoManage):
    def execute(self, command):
        commands = command.split(sep=" ")

        if commands[0] == "debug":
            pass
        elif commands[0] == "hitbox":
            self.draw_hit_box = not self.draw_hit_box
        elif commands[0] == "print":
            print(self.__getattribute__(commands[1]))
            print(self.__getattribute__(commands[1]).__getattribute__(commands[2]))

    def pause(self):
        self.draw()

    def handle_keydown(self, unicode, key, mod):
        if unicode == 'c':
            self.state = StageState.PAUSE
            StageManager().push(StageConsole(self))