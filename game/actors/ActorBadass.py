class ActorBadass(ActorSprite):
	def load_sprite(self):
		self.sprite = pygame.image.load("badass.png").convert()
		
	def update(self):
		actor = self.map.get_player()
		
		dir = Vector(actor.rect.x - self.rect.x, actor.rect.y - self.rect.y)
		dir.normalize()
		
		self.rect.x += self.velocity * dir.x
		self.rect.y += self.velocity * dir.y