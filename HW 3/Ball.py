import pygame
from Drawable import Drawable

class Ball(Drawable):
    def __init__(self, x=0, y=0, ballColor = (255,0,0)):
        super().__init__(x,y)
        self.__ballColor = ballColor
    
    def getRec(self):
        rec = pygame.mouse.get_rect()
        return rec
    
    def draw(self, surface):
        rec = getRec()
        pygame.draw.circle(surface, self.__ballColor, rec, 1)



    
        
            
