import pygame

from api.ActorButton import ActorButton, BUTTON_STATE
from api.StageManager import StageManager
from game.stages.StageLevel import StageLevel


class ActorButtonStart(ActorButton):
    def __init__(self):
        super().__init__(files_prefix="button_start", label="start")

    def execute(self):
        StageManager().push(StageLevel())