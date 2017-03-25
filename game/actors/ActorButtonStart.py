import pygame

from api.ActorButton import ActorButton, BUTTON_STATE
from api.StageManager import StageManager
import game.stages.StageLevel


class ActorButtonStart(ActorButton):
    def __init__(self):
        super().__init__(files_prefix="button_start", label="start")

    def execute(self):
        StageManager().push(game.stages.StageLevel.StageLevel())