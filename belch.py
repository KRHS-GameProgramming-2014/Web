import math,sys,pygame

class Belch():
    def __init__(self,player):
        #self.speed = [0,1]
        self.damage = 10
        self.surface = pygame.image.load("rsc/fatpriest/belch.png")
        self.rect = self.surface.get_rect()
        self.place(player.rect.center)
        self.radius = 30
        
    def place(self, pt):
        self.rect.center = pt
        
    def go(self, player):
        self.place([player.rect.center[0]+0, player.rect.center[1]-30])