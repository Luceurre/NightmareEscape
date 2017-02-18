import pygame

from api.EnumAuto import EnumAuto
from api.Map import Map
from api.StageAutoManage import StageAutoManage
from api.StageManager import StageManager
from api.StageState import StageState
from game.stages.StageConsole import StageConsole
from game.stages.StageHandleConsole import StageHandleConsole
from game.utils.Register import Register
from game.utils.Vector import Vector

class EDIT_MODE(EnumAuto):
    PICK = ()
    MOVE = ()
    REMOVE = ()

class StageEditMode(StageHandleConsole):
    def __init__(self):
        super().__init__()

        self.mouse_pos = Vector(0, 0)
        self.object_pick_id = 0
        self.object_pick = None

        self.is_paused = True
        self.mode = EDIT_MODE.PICK

    def draw(self):
        super().draw()

        if self.object_pick != None:
            self.screen.blit(self.object_pick.sprite, (self.mouse_pos.x, self.mouse_pos.y))

    def update(self):
        if self.is_paused == False:
            super().update()

    def execute(self, command):
        commands = command.split(sep=" ")
        bug = False

        try:
            if commands[0] == "map":
                if commands[1] == "load":
                    self.map = Map.load(commands[2])
                elif commands[1] == "save":
                    self.map.save()
                elif commands[1] == "print":
                    self.map.info("Je suis : " + self.map.name)
                else:
                    bug = True
            elif commands[0] == "pick":
                self.object_pick_id = int(commands[1])
                class_name = Register().get_actor(self.object_pick_id)
                if class_name != None:
                    self.object_pick = class_name()
                else:
                    self.object_pick = None
            elif commands[0] == "pause":
                self.is_paused = True
            elif commands[0] == "unpause":
                self.is_paused = False
            elif commands[0] == "mode":
                if commands[1] == "get":
                    self.info(self.mode)
                elif commands[1] == "set":
                    if commands[2] == "pick":
                        self.mode = EDIT_MODE.PICK
                    elif commands[2] == "move":
                        self.mode = EDIT_MODE.MOVE
                    elif commands[2] == "remove":
                        self.mode = EDIT_MODE.REMOVE
                    else:
                        bug = True
                else:
                    bug = True
            elif commands[0] == "print":
                print(self.__getattribute__(commands[1]))
                print(self.__getattribute__(commands[1]).__getattribute__(commands[2]))
            else:
                bug = True
        except:
            bug = True

        if bug:
            print("\"", command, "\"", " est une commande inconnue", sep="")

    def handle_mouse(self, pos, rel, buttons):
        self.mouse_pos.x = pos[0]
        self.mouse_pos.y = pos[1]

        return True

    def handle_mouse_button_down(self, pos, button):
        if self.object_pick != None:
            actor = Register().get_actor(self.object_pick_id)()
            actor.rect.x = pos[0]
            actor.rect.y = pos[1]
            self.add_actor(actor)
