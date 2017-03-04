# Juste quelques fonctions pour l'aide au traitement d'images
import copy

import pygame

image_list = {}


def get_real_rect(surface):
    width = surface.get_width()
    height = surface.get_height()

    x_min = width
    x_max = 0
    y_min = height
    y_max = 0

    for x in range(width):
        for y in range(height):
            if surface.get_at((x, y))[3] != 0:
                if x < x_min:
                    x_min = x
                elif x > x_max:
                    x_max = x

                if y < y_min:
                    y_min = y
                elif y > y_max:
                    y_max = y

    return pygame.Rect(x_min, y_min, x_max - x_min + 1, y_max - y_min + 1)


def load_image(path, auto_rect=True):
    if path in image_list.keys():
        return copy.copy(image_list[path])
    else:
        image = pygame.image.load(path).convert_alpha()
        if auto_rect:
            rect = get_real_rect(image)
            return image.subsurface(rect)
        else:
            return image


def shadowizer(surface: pygame.Surface):
    new_surface = pygame.transform.rotozoom(surface, -45, 1)
    for x in range(new_surface.get_width()):
        for y in range(new_surface.get_height()):
            if new_surface.get_at((x, y))[3] != 0:
                new_surface.set_at((x, y), (0, 0, 0, 95))

    return new_surface
