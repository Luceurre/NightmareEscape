import pygame


class Timer:
    def __init__(self, time, callback_function, repeat=False, how_many=0, infinite=False, *args, **kwargs):
        self.now = pygame.time.get_ticks()
        self.time = time
        self.callback_function = callback_function
        self.repeat = repeat
        self.how_many = how_many
        self.infinite = infinite
        self.args = args
        self.kwargs = kwargs

        self.active = True

    def update(self):
        if pygame.time.get_ticks() - self.now >= self.time and self.active:
            self.callback_function(self.args, self.kwargs)
            self.how_many -= 1
            if (self.how_many == 0 and not self.infinite) or self.repeat == False:
                self.active = False
                return True


            self.now = pygame.time.get_ticks()
            return False
