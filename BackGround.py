import pygame, math

class BackGround(pygame.sprite.Sprite):
	def __init__(self, image):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
