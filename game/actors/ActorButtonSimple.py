from api.ActorButton import ActorButton
from api.ActorButton import BUTTON_STATE


class ActorButtonSimple(ActorButton):
    def __init__(self, files_prefix, callback_fun, *args, **kwargs):
        super().__init__(files_prefix=files_prefix)

        self.callback_fun = callback_fun
        self.should_update = True
        self.args = args
        self.kwargs = kwargs

    def update(self):
        super().update()

        if self.button_state == BUTTON_STATE.PRESSED:
            self.execute()
            self.button_state = BUTTON_STATE.NORMAL

    def execute(self):
        super(ActorButtonSimple, self).execute()
        self.callback_fun(*self.args, **self.kwargs)