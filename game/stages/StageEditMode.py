import copy
import types

import pygame
import sys

from api.EnumAuto import EnumAuto
from api.Map import Map
from api.StageAutoManage import StageAutoManage
from api.StageManager import StageManager
from api.StageState import StageState
from game.actors.ActorBackground import ActorBackground
from game.actors.ActorSimpleLife import ActorSimpleLife
from game.stages.StageConsole import StageConsole
from game.stages.StageHandleConsole import StageHandleConsole
from game.utils.Grid import Grid
from game.utils.Register import Register
from game.utils.Vector import Vector

class EDIT_MODE(EnumAuto):
    PICK = ()
    MOVE = ()
    REMOVE = ()
    NONE = ()

class StageEditMode(StageHandleConsole):
    def __init__(self):
        super().__init__()

        self.mouse_pos = Vector(0, 0)
        self.object_pick = None

        self.is_paused = True
        self.mode = EDIT_MODE.PICK
        self.grid = Grid()

        self.draw_hit_box = False

    def draw(self):
        super().draw()

        if self.mode == EDIT_MODE.PICK:
            if self.object_pick != None:
                self.screen.blit(self.object_pick.sprite, (self.mouse_pos.x, self.mouse_pos.y))

        self.grid.draw(self.screen)

    def update(self):
        if self.is_paused == False:
            super().update()

    def execute(self, command):
        super().execute(command)

        commands = command.split(sep=" ")
        bug = False

        if commands[0] == "map":
            if commands[1] == "load":
                self.map = Map.load(commands[2])
            elif commands[1] == "save":
                self.map.save()
            elif commands[1] == "print":
                self.map.info("Je suis : " + self.map.name)
            elif commands[1] == "type":
                if commands[2] == "print":
                    self.info(self.map.type)
                elif commands[2] == "set":
                    self.map.type = commands[3]
                else:
                    bug = True
            else:
                bug = True
        elif commands[0] == "pick":
            try:
                id = int(commands[1])
            except:
                id = commands[1]

            if isinstance(id, type("")):
                class_name = Register().get_actor_by_name(id)
            else:
                class_name = Register().get_actor(id)
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
        elif commands[0] == "grid":
            if commands[1] == "turn":
                if commands[2] == "on":
                    self.grid.should_draw = True
                elif commands[2] == "off":
                    self.grid.should_draw = False
                else:
                    bug = True
            elif commands[1] == "set":
                print(commands[2])
                self.grid.size = int(commands[2])
            else:
                bug = False

        elif commands[0] == "actor":
            if commands[1] != "":
                self.object_pick = ActorSimpleLife(commands[1])
            else:
                bug = True
        else:
            bug = True

        if bug:
            print("\"", command, "\"", " est une commande inconnue", sep="")

    def handle_mouse(self, pos, rel, buttons):
        self.mouse_pos.x = pos[0]
        self.mouse_pos.y = pos[1]

        return True

    def handle_mouse_button_down(self, pos, button):
        if self.mode == EDIT_MODE.REMOVE:
            actor = self.map.get_actor_at(pos[0], pos[1])
            if actor != None:
                self.map.remove_actor(actor)
        elif self.mode == EDIT_MODE.PICK:
            if self.object_pick != None:
                actor = copy.deepcopy(self.object_pick)

                if self.grid.should_draw:
                    actor.rect.x = pos[0] - (pos[0] % self.grid.size)
                    actor.rect.y = pos[1] - (pos[1] % self.grid.size)
                else:
                    actor.rect.x = pos[0]
                    actor.rect.y = pos[1]
                self.map.add_actor(actor)
        elif self.mode == EDIT_MODE.MOVE:
            actor = self.map.get_actor_at(pos[0], pos[1])
            if actor != None:
                self.map.remove_actor(actor)
            self.mode = EDIT_MODE.PICK
            self.object_pick = type(actor)()

