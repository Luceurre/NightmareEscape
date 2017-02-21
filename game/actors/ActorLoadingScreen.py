import pygame
from api.ActorSprite import ActorSprite
from api.Timer import Timer
from game.utils.SurfaceHelper import load_image


class ActorLoadingScreen(ActorSprite):
    def __init__(self):
        super().__init__()
        self.sprite = load_image("assets/loading_screen.bmp")
        self.sprite.set_alpha(0)
        self.should_update = True
        self.handle_event = True
        timer = Timer(5, self.animate_part_1, repeat=True, how_many=102)
        self.add_timer(timer)
        self.finish = False

    def update(self):
        self.update_timers()

    def animate_part_1(self, *args, **kwargs):
        self.sprite.set_alpha(self.sprite.get_alpha() + 5)

        if self.sprite.get_alpha() >= 255:
            self.timers.pop(0)
            self.add_timer(Timer(1500, self.animate_part_2, repeat=False))


    def animate_part_2(self, *args, **kwargs):
        self.add_timer(Timer(5, self.animate_part_3, repeat=True, infinite=True))

    def animate_part_3(self, *args, **kwargs):
        self.sprite.set_alpha(self.sprite.get_alpha() - 5)

        if self.sprite.get_alpha() <= 0:
            self.finish = True
            self.timers.pop(0)



    def handle_keydown(self, unicode, key, mod):
        self.rect.x += 5

        return True