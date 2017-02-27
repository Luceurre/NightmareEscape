import pygame

from game.actors.ActorCollidable import ActorCollidable

class ActorWall_1(ActorCollidable):
	
	ID = 5
	NAME = "Wall_1"
	
	def load_sprite(self):
		super().load_sprite()
		
		self.sprite = pygame.image.load("assets/Wall1.png").convert()

