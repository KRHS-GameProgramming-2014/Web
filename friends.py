import pygame, math

class friend():
    def __init__(self, image, speed = [0,0], pos = [0,0]):
        #if friend == "kik":
            #self.image = pygame.image.load ""
            #self.color = color
            #self.value = 
        #if friend == "twitter":
            #self.image == pygame.image.load ""
            #self.color = color
            #self.value = 

    def collidefriend(self, other):
        if self != other:
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        if not self.didBounceX:
                            self.speedx = -self.speedx
                            self.didBouncex = True
                        if not self.didBounceY:
                            self.speedy = -self.speedy
                            self.didBounceY = True
                            #print "hit friend"
                            
    def collidebrowser(self, other):
        if self != other:
            if collidebrowser 
            

