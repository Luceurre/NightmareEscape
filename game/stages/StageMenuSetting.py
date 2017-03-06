from api.StageMenu import StageMenu
from game.actors.ActorButtonSettingKeys import ActorButtonSettingKeys


class StageMenuSetting(StageMenu):
    def init(self):
        self.map.add_actor(ActorButtonSettingKeys())
        # self.map.add_actor(ActorButtonReturn(StageMainMenu))

        self.map.actors[0].set_centered(height=self.rect.width / 2)
        # self.map.actors[1].set_centered(height=self.rect.height * 2)
