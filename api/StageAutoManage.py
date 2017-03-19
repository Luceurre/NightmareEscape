from api.Stage import Stage


class StageAutoManage(Stage):
    """
    Une surcouche de Stage, 
    """
    def __init__(self):
        super().__init__()

        self.auto_manage = True

    def run(self):
        super().run()

        if self.auto_manage:
            # En gros, Les trois loop gérant les acteurs et les évènements, cf Stage
            self.events_loop()

            self.update()
            self.draw()

    def update(self):
        super().update()

        if self.auto_manage:
            self.update_timers()
            self.events_loop()
            self.update_actors()

    def draw(self):
        super().draw()

        if self.auto_manage:
            self.draw_actors()