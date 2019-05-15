import pygame
from Drawable import Drawable

class Block(Drawable):
    def __init__(self, position, visible):
        super().__init__(position,visible)
        self.__ballColor = ballColor
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.__ballColor, (position, 10,20))


        
