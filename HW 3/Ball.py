import pygame
from Drawable import Drawable

class Ball(Drawable):
    def __init__(self, x, y, radius, ballColor = (255,0,0)):
        super().__init__(x,y)
        self.__ballColor = ballColor
        self.__radius = radius
    def get_rect(self):
        rec = self.getPosition()
        return pygame.Rect( [(super.getX()-self.__radius), (super.getY()-self.__radius),(self.__radius+self.__radius),(self.__radius+self.__radius)] )
 
    
    def draw(self, surface):
        rec = self.getPosition()
        pygame.draw.circle(surface, self.__ballColor, rec, self.__radius)



    
        
            
