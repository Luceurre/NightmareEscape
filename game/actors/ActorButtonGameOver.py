from api.ActorButton import ActorButton
from api.StageManager import StageManager 
import game.stages.StageMainMenu



class ActorButtonGOmenu(ActorButton):
    def __init__(self):
        super().__init__(files_prefix="button_GOmenu", hov=False)

        #self.next_stage = next_stage
        
    def execute(self):
        super().execute()
        
        StageManager().push(game.stages.StageMainMenu.StageMainMenu())
        
class ActorButtonGOquit(ActorButton):
    def __init__(self):
        super().__init__(files_prefix="button_GOquit", hov=False)

        #self.next_stage = next_stage
        
    def execute(self):
        super().execute()
        
        StageManager().exit()
        
        