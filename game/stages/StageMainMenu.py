from api.ActorButton import BUTTON_STATE, ActorButton
from api.StageAutoManage import StageAutoManage
from api.StageManager import StageManager
from api.StageState import StageState
from game.actors.ActorButtonQuit import ActorButtonQuit
from game.actors.ActorButtonStart import ActorButtonStart
from game.actors.ActorButtonEdit import ActorButtonEdit
from game.stages.StageLevel import StageLevel


class StageMainMenu(StageAutoManage):
    def __init__(self):
        super().__init__()
        self.pressed_button = None

    def init(self):
        self.add_actor(ActorButtonStart())
        self.add_actor(ActorButtonQuit())
        self.add_actor(ActorButtonEdit())
        self.add_actor(ActorButton(files_prefix="button_setting", label="setting"))

        height = self.screen.get_height() / (len(self.map.actors) + 2)

        for index, button in enumerate(self.map.actors):
            button.set_centered_x(self.screen.get_width())
            button.rect.y = (index + 1) * height

    def run(self):
        super().run()

        for actor in self.map.actors:
            if isinstance(actor, ActorButton):
                if actor.button_state == BUTTON_STATE.PRESSED:
                    self.state = StageState.QUIT
                    self.pressed_button = actor
    def quit(self):
        del self.map

        self.pressed_button.execute()
