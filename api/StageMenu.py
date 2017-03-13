import pygame.mixer

from api.ActorButton import ActorButton, BUTTON_STATE
from api.StageAutoManage import StageAutoManage
from api.StageState import StageState


class StageMenu(StageAutoManage):
    def __init__(self):
        super().__init__()
        self.pressed_button = None

    def run(self):
        super().run()

        for actor in self.map.actors:
            if isinstance(actor, ActorButton):
                if actor.button_state == BUTTON_STATE.PRESSED:
                    self.state = StageState.QUIT
                    self.pressed_button = actor

    def quit(self):
        super().quit()


        self.pressed_button.execute()
