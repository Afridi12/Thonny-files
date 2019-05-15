import pygame
from Drawable import Drawable
import Ball
from Block import Block

pygame.init()

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
screenSize = (1000,800)
gravity = 6.67
R = 0.7
eta = 0.5

screen = pygame.display.set_mode(screenSize)

screen.fill(white)

pygame.display.update()

clock = pygame.time.Clock()
fps = 60
rateGrav = gravity/fps
running = True
overall_speed = rateGrav


