import pygame

from api.StageAutoManage import StageAutoManage
import os

from api.StageManager import StageManager
from api.StageState import StageState
from game.actors.ActorSimpleLife import ActorSimpleLife
from game.actors.ActorTile import ActorTile
from game.stages.StageHandleConsole import StageHandleConsole
from game.utils.Grid import Grid
from game.utils.SurfaceHelper import load_image
from game.utils.Vector import Vector

TILE_PATH = "tilesets/"


class StageTileSelector(StageHandleConsole):
    def __init__(self):
        super().__init__()

        self.tileset_files = []
        for file in os.listdir(TILE_PATH):
            if os.path.isfile(TILE_PATH + file):
                self.tileset_files.append(TILE_PATH + file)

        self.tile_picked = None
        self.grid = Grid()
        self.grid.should_draw = True
        self.grid.size = 48
        self.tileset_no = 0

        if not self.tileset_files:
            self.info("No tileset found.")
            self.state = StageState.QUIT
        else:
            self.map.add_actor(self.grid)
            self.map.add_actor(ActorSimpleLife("../" + self.tileset_files[self.tileset_no]))

    def draw(self):
        self.screen.fill((0, 0, 0, 255))
        super().draw()

    def handle_mouse_button_down(self, pos, button):
        try:
            self.state = StageState.QUIT
            self.tile_picked = ActorTile(self.tileset_files[self.tileset_no], Vector(pos[0] - pos[0] % self.grid.size, pos[1] - pos[1] % self.grid.size), self.grid.size)

            return True
        except ValueError:
            self.info("Tu n'as pas cliqué sur une image!")

    def handle_keydown(self, unicode, key, mod):
        handle = super().handle_keydown(unicode, key, mod)

        if key == pygame.K_RIGHT:
            self.tileset_no = (self.tileset_no + 1) % len(self.tileset_files)
            self.map.actors.pop()
            self.map.add_actor(ActorSimpleLife("../" + self.tileset_files[self.tileset_no]))

            handle = True
        elif key == pygame.K_LEFT:
            self.tileset_no = (self.tileset_no - 1) % len(self.tileset_files)
            self.map.actors.pop()
            self.map.add_actor(ActorSimpleLife("../" + self.tileset_files[self.tileset_no]))
        else:
            try:
                self.tileset_no = int(unicode) % len(self.tileset_files)
                self.map.actors.pop()
                self.map.add_actor(ActorSimpleLife("../" + self.tileset_files[self.tileset_no]))

                handle = True
            except:
                handle = False

        return handle

    def execute(self, command):
        super().execute(command)

        commands = command.split(sep=" ")
        try:
            if commands[0] == "grid":
                if commands[1] == "size":
                    self.grid.size = int(commands[2])
        except:
            self.info("Commande inconnue.")

    def quit(self):
        StageManager().stack[-1].state = StageState.RESUME
