import pygame

import api.StageManager


class EventHandler():
    def handle(self, event):
        if event.type == pygame.KEYDOWN:
            return self.handle_keydown(event.unicode, event.key, event.mod)
        elif event.type == pygame.KEYUP:
            return self.handle_keyup(event.key, event.mod)
        elif event.type == pygame.MOUSEMOTION:
            return self.handle_mouse(event.pos, event.rel, event.buttons)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            return self.handle_mouse_button_down(event.pos, event.button)
        elif event.type == pygame.MOUSEBUTTONUP:
            return self.handle_mouse_button_up(event.pos, event.button)
        elif event.type == pygame.QUIT:
            api.StageManager.StageManager().exit()
            return True
        elif event.type == pygame.USEREVENT:
            return self.handle_userevent(event)
        else:
            return False

    def handle_keydown(self, unicode, key, mod):
        return False

    def handle_keyup(self, key, mod):
        return False

    def handle_mouse(self, pos, rel, buttons):
        return False

    def handle_mouse_button_down(self, pos, button):
        return False

    def handle_mouse_button_up(self, pos, button):
        return False

    def handle_userevent(self, event):
        return False
