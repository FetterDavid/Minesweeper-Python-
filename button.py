import pygame
import os
pygame.font.init()

class Button():

    def __init__(self,tableSize,windowWidth,position,index):
        self.position = position
        self.index = index
        self.size = windowWidth // tableSize 
        self.coverImg = pygame.transform.scale(pygame.image.load(os.path.join("Assets","button.png")),(self.size,self.size))
        self.mineImg = pygame.transform.scale(pygame.image.load(os.path.join("Assets","buttonRed.png")),(self.size,self.size))
        self.emptyImg = pygame.transform.scale(pygame.image.load(os.path.join("Assets","buttonGreen.png")),(self.size,self.size))
        self.flagImg = pygame.transform.scale(pygame.image.load(os.path.join("Assets","buttonFlag.png")),(self.size,self.size))
        self.clicked = False
        self.isMine = False
        self.nearMines = 0
        self.nearMinesText = pygame.font.SysFont("monospace", 50, bold=True)

    def CheckForInput(self,mousePos):
        if mousePos[0] in range(self.position[0],self.position[0]+self.size) and mousePos[1] in range(self.position[1],self.position[1]+self.size):
            return True
        return False

    def SetToMine(self):
        self.isMine = True



    