from operator import attrgetter

import pygame

from api.EventHandler import EventHandler
from api.Logger import Logger
from api.Map import Map
from api.StageState import StageState


class Stage(EventHandler, Logger):
    
    """ Class correspondant à une scène ( ou plutôt un acte )  de théâtre ( scène du menu, scène de l'éditeur, scène de chargement un peu une entre-scène, etc
    Ici sont appelées les boucles visant à actualiser touts les évènements, les acteurs ( oui encore du théâtre , correspond soit à un acteur ethymologique, comme le joueur
    , soit peut être à un décor , un meuble, un objet qui s'affiche à l'écran ou avec lequel on peut interragir)
    
    Donc en fait est le cadre permettant la transmission des évènements à une map, ou plus précisément à tout les acteurs de la map qui réagissent delon ces évènements
    
     """
    def __init__(self):
        self.state = StageState.INIT
        self.map = Map()
        self.timers = []

        self.screen = pygame.display.get_surface()
        self.rect = pygame.Rect(0, 0, self.screen.get_width(), self.screen.get_height())
        self.draw_hit_box = False

    def update(self):
        """Ici se passe toute la logique de la scène"""

    def draw(self):
        """Ici se passe tout ce qui est affiché à l'écran"""

        if self.draw_hit_box:
            for actor in self.map.actors:
                pygame.gfxdraw.rectangle(self.screen, actor.rect, (0, 255, 0))

    # Callbacks functions (StateManager)

    def resume(self):
        # Called when StageState changes from PAUSE to RUN
        pass

    def quit(self):
        # Called when StageState is QUIT (should be called once per instance)
        pass


    def init(self):
        # Called when StageState is INIT (should be called once per instance)
        pass

    def run(self):
        # Called each tick when StageState is RUN
        pass

    def pause(self):
        # Called each tick when StageState is PAUSE
        pass

    def events_loop(self):
        """ double boucle: pour chaque evènement, cherche si un acteur ( ou le stage ) le "gère" """
        actors_sorted = sorted(self.map.actors, key=attrgetter('handle_event', 'handle_event_priority'), reverse=True)

        for event in pygame.event.get():
            if not self.handle(event):
                for actor in actors_sorted:
                    if not actor.handle_event:
                        break
                    elif actor.handle(event):
                        break

    def draw_actors(self):
        for actor in sorted(self.map.actors, key=attrgetter('should_draw', 'z'), reverse=True):
            if not actor.should_draw:
                break
            else:
                actor.draw(self.screen)

    def update_actors(self):
        for actor in sorted(self.map.actors, key=attrgetter('should_update'), reverse=True):
            if not actor.should_update:
                break
            else:
                actor.update()

    def add_timer(self, timer):
        self.timers.append(timer)

    def update_timers(self):
        for index, timer in enumerate(self.timers):
            if timer.update():
                self.timers.pop(index)

    def remove_actor(self, actor):
        if actor in self.map.actors:
            self.map.actors.remove(actor)
            del actor
        else:
            self.warning("Tu essayes de détruire un Actor qui n'existe pas Renaud...")