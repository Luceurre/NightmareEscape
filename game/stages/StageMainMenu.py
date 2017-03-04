from api.ActorButton import BUTTON_STATE, ActorButton
from api.StageAutoManage import StageAutoManage
from api.StageManager import StageManager
from api.StageMenu import StageMenu
from api.StageState import StageState
from game.actors.ActorButtonQuit import ActorButtonQuit
from game.actors.ActorButtonStart import ActorButtonStart
from game.actors.ActorButtonEdit import ActorButtonEdit
from game.stages.StageLevel import StageLevel


class StageMainMenu(StageMenu):
    def __init__(self):
        super().__init__()

    def init(self):
        self.map.add_actor(ActorButtonStart())
        self.map.add_actor(ActorButtonQuit())
        self.map.add_actor(ActorButtonEdit())
        self.map.add_actor(ActorButton(files_prefix="button_setting", label="setting"))

        height = self.screen.get_height() / (len(self.map.actors) + 2)

        for index, button in enumerate(self.map.actors):
            button.set_centered_x(self.screen.get_width())
            button.rect.y = (index + 1) * height

