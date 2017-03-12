from api.StageMenu import StageMenu
from game.actors.ActorButtonEdit import ActorButtonEdit
from game.actors.ActorButtonQuit import ActorButtonQuit
from game.actors.ActorButtonSetting import ActorButtonSetting
from game.actors.ActorButtonStart import ActorButtonStart
        

class StageMainMenu(StageMenu):
    def __init__(self):
        super().__init__()

    def init(self):
        self.map.add_actor(ActorButtonStart())
        self.map.add_actor(ActorButtonQuit())
        self.map.add_actor(ActorButtonEdit())
        self.map.add_actor(ActorButtonSetting())

        height = self.screen.get_height() / (len(self.map.actors) + 2)

        for index, button in enumerate(self.map.actors):
            button.set_centered_x(self.screen.get_width())
            button.rect.y = (index + 1) * height

