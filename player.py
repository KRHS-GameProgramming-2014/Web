import pygame, math

class Browser(pygame.sprite.Sprite):
    def __init__(self, pos = [0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("rsc/browser.png")
        self.rect = self.image.get_rect()
        self.maxSpeed = 10
        self.speedx = 0
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.place(pos)
        self.didBounceX = False
        self.didBounceY = False
        self.living = True
        
    def place(self, pos):
        self.rect.center = pos
        
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        self.didBounceX = False
        self.didBounceY = False
        self.move()
        self.collideWall(width, height)
        
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def collideWall(self, width, height):
        if not self.didBounceX:
            #print "trying to hit Wall"
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = -self.speedx
                self.didBounceX = True
                #print "hit xWall"
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = -self.speedy
                self.didBounceY = True
                #print "hit xWall"
    #def collidefriend(self, other):
        #if not self.invincible:
            #if self!= other:
                ##print "trying to hit friend"
    
    def go(self, direction):
        if direction == "up":
            self.facing = "up"
            self.changed = True
            self.speedy = -self.maxSpeed
        elif direction == "stop up":
            self.speedy = 0
        elif direction == "down":
            self.facing = "down"
            self.changed = True
            self.speedy = self.maxSpeed
        elif direction == "stop down":
            self.speedy = 0
            
        if direction == "right":
            self.facing = "right"
            self.changed = True
            self.speedx = self.maxSpeed
        elif direction == "stop right":
            self.speedx = 0
        elif direction == "left":
            self.facing = "left"
            self.changed = True
            self.speedx = -self.maxSpeed
        elif direction == "stop left":
            self.speedx = 0

    def distance(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
