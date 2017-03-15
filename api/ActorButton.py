import enum

import pygame

from api.ActorSprite import ActorSprite
from api.EnumAuto import EnumAuto


class BUTTON_STATE(EnumAuto):
    NORMAL = ()
    HOVERED = ()
    PRESSED = ()

class ActorButton(ActorSprite):
    def __init__(self, sprites=None, files_prefix="", label=""):
        super().__init__()
        
        self.button_job_leave = True


        self.button_state = BUTTON_STATE.NORMAL
        self.previous_button_state = BUTTON_STATE.NORMAL
        self.handle_event = True

        # Loading sprites

        if sprites is not None:
            self.sprites = sprites
        elif files_prefix != "":
            self.sprites = {BUTTON_STATE.NORMAL: pygame.image.load("assets/" + files_prefix + "_normal.png").convert_alpha(),
                            BUTTON_STATE.PRESSED: pygame.image.load("assets/" + files_prefix + "_pressed.png").convert_alpha(),
                            BUTTON_STATE.HOVERED: pygame.image.load("assets/" + files_prefix + "_hovered.png").convert_alpha()}

        self.label = label


    def handle_mouse(self, pos, rel, buttons):
        if self.rect.collidepoint(pos[0], pos[1]):
            if self.button_state != BUTTON_STATE.PRESSED:
                self.update_button_state(BUTTON_STATE.HOVERED)
        else:
            self.update_button_state(BUTTON_STATE.NORMAL)

    def handle_mouse_button_down(self, pos, button):
        if self.rect.collidepoint(pos[0], pos[1]) and button == 1:
            self.update_button_state(BUTTON_STATE.PRESSED)

    def update_button_state(self, new_state):
        self.previous_button_state = self.button_state
        self.button_state = new_state

        self.sprite = self.sprites[self.button_state]

    @property
    def sprites(self):
        return self._sprites

    @sprites.setter
    def sprites(self, sprites):
        self._sprites = sprites
        self.sprite = sprites[self.button_state]

    # Quelques méthodes utiles :

    def did_change(self):
        return self.button_state == self.previous_button_state

    def execute(self):
        pass