import pygame

from api.StageAutoManage import StageAutoManage
from api.StageState import StageState


class StageConsole(StageAutoManage):
    def __init__(self, previous_stage):
        super().__init__()

        self.console = ""
        self.font = pygame.font.Font("freesansbold.ttf", 15)
        self.previous_stage = previous_stage

    def draw(self):
        super().draw()

        self.screen.blit(self.font.render(self.console, True, (255, 0, 255)), (0, 0))

    def quit(self):
        super().quit()

        self.previous_stage.state = StageState.RESUME
        self.previous_stage.execute(self.console)

    def handle_keydown(self, unicode, key, mod):
        if key == pygame.K_RETURN:
            self.state = StageState.QUIT
        elif key == pygame.K_BACKSPACE:
            self.console = self.console[:-1]
        else:
            self.console += unicode

