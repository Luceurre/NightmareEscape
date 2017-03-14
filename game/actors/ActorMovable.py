import copy
import pygame



from api.ActorSprite import ActorSprite
from game.utils.Direction import DIRECTION


import game.utils.SurfaceHelper

from game.actors.ActorPlayer import ActorPlayer
#from game.actors.ActorPuzzleSolution import ActorPuzzleSolution
#from game.actors.ActorDoor import ActorDoor
#from pygame.examples.scaletest import SpeedTest




class ActorMovable(ActorSprite):                # A passer probablement sur ActorAnimation
    def __init__(self):
        super().__init__()
        
        #déplacement
        
        self.has_moved = False
        self.speed = 1  # En pixel par déplacement   _____ MAIS : si trop bas par rapport au perso, enlève fluidité au personnage
        
        #collision
        self.collidable = True
        
        self.map = None
        
    def reload(self):
        super().reload()
        
        self.collidable = True
        
    def interact(self, actor):
        if isinstance(actor, ActorPlayer):
            x , y = 0, 0
            cote_collision = game.utils.SurfaceHelper.get_side_colliderect(self.rect, actor.rect, actor.speed)
            
            #direction_collision = opposite(cote_collision)
            
            if cote_collision == DIRECTION.HAUT:                    # ici on inverse déplacement car coté collision est vers le joueur
                y = 1
            elif cote_collision == DIRECTION.BAS:
                y = -1
            elif cote_collision == DIRECTION.DROITE:
                x = -1
            elif cote_collision == DIRECTION.GAUCHE:
                x = 1
                
            #self.rect.x += x * self.speed
            #self.rect.y += y * self.speed
                        
            #self.move(direction_collision.x * self.speed, direction_collision.y * self.speed, [self, actor])   #ne marche pas, doit être dû à enum
            
            self.move(x * self.speed, y * self.speed, [actor])
            
            """"En soi renvoie True si self bouge, mais ce True n'est pas récupéré.... Je n'ai pas enlevé ce booléen, car si je ne me sert pas du has_moved, c'est parceque
            l'objet n'a pas vraiment de vitesse: il ne bouge que si ActorPlayer bouge vers lui"""
            
        #elif isinstance(actor, ActorPuzzleSolution):
        #    for actor in self.map.actors:
        #        if isinstance(actor, ActorDoor):
        #            actor.open()
        """Est appelé avec la fonction interact de PuzzleSolution"""
            

        return (actor.collidable and self.collidable)
    
            
            
            
    def move(self, x=0, y=0, collisionable = []):           #collisionable est une liste des acteurs dont on ne gère pas la collision avec self ( oui c'est de l'anglais de cuisine, mea culpa)
    
        """Return True if the Actor moved, False otherwise"""

        if x == 0 and y == 0:
            return False

        rect = copy.copy(pygame.Rect(self.rect))
        rect.x += x
        rect.y += y

        rect.y += rect.h - self.depth
        rect.h = self.depth

        actors = self.map.get_actors_collide(rect, collisionable)

        """
        remove_indexes = []

        for index, actor in enumerate(actors):
            if not actor.collidable:
                remove_indexes.append(index)

        for i, index in enumerate(remove_indexes):
            actors.pop(index - i)
        """

        a_interagi = False
        for actor in actors:
            if isinstance(actor, ActorPlayer):
                b = False
            else:
                b = actor.interact(self)
                
            if not a_interagi and b:
                a_interagi = True

        if not a_interagi:
            self.rect.x += x
            self.rect.y += y

            return True
        else:
            return False
            