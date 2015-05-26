import pygame, sys, random
from friend import Friend
from player import Browser
from BackGround import BackGround

pygame.init()

clock = pygame.time.Clock()

width = 800 
height = 600
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)

friends = pygame.sprite.Group()
players = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Friend.containers = (all, friends)
BackGround.containers = (all, backgrounds)
Browser.containers = (all, players)

BackGround("rsc/bgorg.jpg")

run = True
while True:
    player = Browser((200,200))
    friends = Friend ((300,300))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.go("up")
                if event.key == pygame.K_d:
                    player.go("right")
                if event.key == pygame.K_s:
                    player.go("down")
                if event.key == pygame.K_a:
                    player.go("left")
                if event.key == pygame.K_UP:
                    friends.go("up")
                if event.key == pygame.K_RIGHT:
                    friends.go("right")
                if event.key == pygame.K_DOWN:
                    friends.go("down")
                if event.key == pygame.K_LEFT:    
                    friends.go("left")
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("stop up")
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.go("stop right")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.go("stop down")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.go("stop left")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    friends.go("stop up")
                if event.key == pygame.K_RIGHT:
                    friends.go("stop right")
                if event.key == pygame.K_DOWN:
                    friends.go("stop down")
                if event.key == pygame.K_LEFT:
                    friends.go("stop left")        
            
        all.update(width, height)
        
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
