from api.Actor import HANDLE_EVENT_PRIORITY
from api.StageAutoManage import StageAutoManage
from api.StageManager import StageManager

from api import Stage
from test.ActorAnimationTest import ActorAnimationTest
from test.ActorButtonTest import ActorButtonTest
from test.ActorPlayerTest import ActorPlayerTest
from test.ActorTest import ActorTest


class StageMenu(StageAutoManage):
    def init(self):
        for i in range(1):
            self.add_actor(ActorButtonTest())

        #self.add_actor(ActorAnimationTest())
        self.add_actor(ActorPlayerTest())

        #self.actors[1].rect.x = 300

    def handle_keydown(self, unicode, key, mod):
        if (key == 27):
            StageManager().exit()
