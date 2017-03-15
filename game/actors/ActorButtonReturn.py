from api.ActorButton import ActorButton
from api.StageManager import StageManager 
import game.stages.StageMainMenu



class ActorButtonReturn(ActorButton):
    def __init__(self):
        super().__init__(files_prefix="button_return")

        #self.next_stage = next_stage
        
    def execute(self):
        super().execute()
        
        StageManager().push(game.stages.StageMainMenu.StageMainMenu())
        
        