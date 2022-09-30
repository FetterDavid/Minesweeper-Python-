import pygame
import os

class Button():

    def __init__(self,tableSize,windowWidth):
        self.size = windowWidth // tableSize 
        self.image = pygame.image.load(os.path.join("Assets","button.png"))
        self.images = pygame.transform.scale(self.image,(self.size,self.size))

    