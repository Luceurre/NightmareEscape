from api.ActorButton import ActorButton


class ActorButtonReturn(ActorButton):
    def __init__(self, next_stage):
        super().__init__(files_prefix="button_return")

        self.next_stage = next_stage