import pygame
import os
import fieldTable
pygame.font.init()

COVER_IMG = pygame.image.load(os.path.join("Assets","fieldCover.png"))
MINE_IMG = pygame.image.load(os.path.join("Assets","fieldMine.png"))
EMPTY_IMG = pygame.image.load(os.path.join("Assets","fieldEmpty.png"))
FLAG_IMG = pygame.image.load(os.path.join("Assets","fieldFlag.png"))

class Button():

    def __init__(self, tableSize, windowWidth, position, index):
        self.position = position
        self.index = index
        self.size = windowWidth // tableSize 
        self.coverImg = pygame.transform.scale(COVER_IMG,(self.size,self.size))
        self.mineImg = pygame.transform.scale(MINE_IMG,(self.size,self.size))
        self.emptyImg = pygame.transform.scale(EMPTY_IMG,(self.size,self.size))
        self.flagImg = pygame.transform.scale(FLAG_IMG,(self.size,self.size))
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

def ButtonClicked(button,win,table,tableSize):
    button.clicked = True
    if(button.isMine):
        win.blit(button.mineImg,(button.position[0],button.position[1]))
    else:
        win.blit(button.emptyImg,(button.position[0],button.position[1]))
        if button.nearMines > 0:
            buttonText = button.nearMinesText.render(str(button.nearMines),1,(0,0,0))
            win.blit(buttonText,(button.position[0]+10,button.position[1]))
        else:
            Burst(button.index, table, win, tableSize)

def Burst(buttonIndex,table,win,tableSize):
    index = buttonIndex
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            pos = [index[0]+i,index[1]+j]
            if( not (pos[0] < 0 or pos[0] >= tableSize or pos[1] < 0 or pos[1] >= tableSize) and not table[pos[0]][pos[1]].clicked):
                ButtonClicked(table[pos[0]][pos[1]], win, table, tableSize)

def SetFlag(button,win):
     win.blit(button.flagImg,(button.position[0],button.position[1]))
    