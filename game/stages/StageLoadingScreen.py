import pygame
from api.Stage import Stage, StageState
from api.StageAutoManage import StageAutoManage
from api.StageManager import StageManager
from game.actors.ActorLoadingScreen import ActorLoadingScreen
from game.stages.StageLevel import StageLevel
from game.stages.StageMainMenu import StageMainMenu
from game.utils.Loader import Loader


class StageLoadingScreen(StageAutoManage):
    def init(self):
        self.loading_screen = ActorLoadingScreen()
        self.map.add_actor(self.loading_screen)
        self.loading_thread = Loader()
        self.loading_thread.start()

    def run(self):
        super().run()

        if self.loading_screen.finish and self.loading_thread.finish:
            self.state = StageState.QUIT

    def quit(self):
        StageManager().push(StageMainMenu())

    def handle_keydown(self, unicode, key, mod):
        self.loading_screen.finish = True
        return True


