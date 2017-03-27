import pygame

from api.ActorSprite import ActorSprite


class ActorText(ActorSprite):
    def __init__(self, text, font=None, color=(255, 255, 255)):
        super().__init__(False)

        self.text = text
        if font is None:
            self.font = pygame.font.Font("freesansbold.ttf", 15)
        else:
            self.font = font
        self.color = color
        self.rect.size = self.font.size(self.text)

    def draw(self, screen):
        screen.blit(self.font.render(self.text, True, self.color), self.rect.pyrect)