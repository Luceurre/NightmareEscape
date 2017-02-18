from api.ActorButton import ActorButton
from api.StageManager import StageManager
from game.stages.StageEditMode import StageEditMode


class ActorButtonEdit(ActorButton):
    def __init__(self):
        super().__init__(files_prefix="button_edit", label="edit")

    def execute(self):
        StageManager().push(StageEditMode())
