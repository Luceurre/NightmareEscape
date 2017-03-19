import pygame.mixer

from api.ActorButton import ActorButton, BUTTON_STATE
from api.StageAutoManage import StageAutoManage
from api.StageState import StageState


class StageMenu(StageAutoManage):
    """
    run hérité, ajout en plus d'une fonctionnalité propre: cherche les acteurs de map qui sont des boutton pressés, les exécute, ou bien quitte la scène et les exécute
    """
    
    def __init__(self):
        super().__init__()
        self.pressed_button = None

    def run(self):
        
        super().run()

        for actor in self.map.actors:
            if isinstance(actor, ActorButton):
                if actor.button_state == BUTTON_STATE.PRESSED:
                    if actor.button_job_leave:  # à definir au niveau du boutton : si True, lorsque boutton est exécuté, scène est quittée
                        self.state = StageState.QUIT
                        self.pressed_button = actor
                    else:
                        actor.execute()
                    
    def quit(self):
        super().quit()


        self.pressed_button.execute()
