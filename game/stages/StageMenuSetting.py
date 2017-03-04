from game.actors.ActorButtonReturn import ActorButtonReturn
from game.actors.ActorButtonSettingKeys import ActorButtonSettingKeys
from game.stages.StageMainMenu import StageMainMenu
from test.StageMenu import StageMenu


class StageMenuSetting(StageMenu):
    def init(self):
        self.map.add_actor(ActorButtonSettingKeys())
        self.map.add_actor(ActorButtonReturn(StageMainMenu))

        self.map.actors[0].set_centered(height=self.rect.width / 2)
        self.map.actors[1].set_centered(height=self.rect.height * 2)