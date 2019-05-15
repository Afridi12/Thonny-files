import pygame
import abc

class Drawable(metaclass = abc.ABCMeta):
    def __init__(self, x, y, position, visible):
        self.__x = x
        self.__y = y
        self.__position = position
        self.__visible = visible
        
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getPosition(self):
        return (self.__x, self.__y)
    
    @abc.abstractmethod
    def get_Position(self):
        pass
    
    @abc.abstractmethod
    def draw(self, surface):
        pass
    
    @abc.abstractmethod
    def get_rect(self):
        pass
    
    def visible(self, disc):
        if disc == True:
            disc.draw()
        else:
            return disc
        
    
        