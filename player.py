import pygame, math

class browser():
    def __init__(self, image, speed = [0,0], pos = [0,0]):
     
        self.living = True
        
    def place(self, pos):
        self.rect.center = pos
        
    def update(self, width, height):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.move()
        self.collideWall(width, height)
        
    def move(self):
        self.rect = self.rect.move(self.speed)
