import pygame
import os

PLAY_IMG = pygame.image.load(os.path.join("Assets","play.png"))
WIN_IMG = pygame.image.load(os.path.join("Assets","win.png"))
DEAD_IMG = pygame.image.load(os.path.join("Assets","dead.png"))


class GameButton():

    def __init__(self, tableSize, position):
        self.position = [int(position[0]),int(position[1])]
        self.size = int(tableSize) 
        self.playImg = pygame.transform.scale(PLAY_IMG,(self.size,self.size))
        self.winImg = pygame.transform.scale(WIN_IMG,(self.size,self.size))
        self.deadImg = pygame.transform.scale(DEAD_IMG,(self.size,self.size))


    def CheckForInput(self,mousePos):
        if mousePos[0] in range(self.position[0],self.position[0]+self.size) and mousePos[1] in range(self.position[1],self.position[1]+self.size):
            return True
        return False

def SetWin(win,button):
    win.blit(button.winImg,(button.position[0],button.position[1]))