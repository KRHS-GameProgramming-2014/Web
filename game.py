import pygame, sys, random
from Friends import friend
from Player import browser

pygame.init()

clock = pygame.time.Clock()

width = 800 
height = 600
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)

bgImage = pygame.image.load("rsc/bgorg.jpg")





    bgColor = r,g,b
            screen.fill(bgColor)
            screen.blit(bgImage, bgRect)

    pygame.display.flip()
            clock.tick(60)
