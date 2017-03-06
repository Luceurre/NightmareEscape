from api.ActorButton import ActorButton
from api.StageManager import StageManager
from game.stages.StageMenuSetting import StageMenuSetting


class ActorButtonSetting(ActorButton):
    def __init__(self):
        super().__init__(files_prefix="button_setting")

    def execute(self):
        StageManager().push(StageMenuSetting())
