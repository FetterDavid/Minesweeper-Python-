from dataclasses import field
import pygame
import os
import fieldTable
import gameManager

pygame.font.init()

COVER_IMG = pygame.image.load(os.path.join("Assets","fieldCover.png"))
MINE_IMG = pygame.image.load(os.path.join("Assets","fieldMine.png"))
EMPTY_IMG = pygame.image.load(os.path.join("Assets","fieldEmpty.png"))
FLAG_IMG = pygame.image.load(os.path.join("Assets","fieldFlag.png"))
INCORRECT_FLAG_IMG = pygame.image.load(os.path.join("Assets","incorrectFlag.png"))

class Field():

    def __init__(self, tableSize, windowWidth, position, index):
        self.position = position
        self.index = index
        self.size = windowWidth // tableSize 
        self.coverImg = pygame.transform.scale(COVER_IMG,(self.size,self.size))
        self.mineImg = pygame.transform.scale(MINE_IMG,(self.size,self.size))
        self.emptyImg = pygame.transform.scale(EMPTY_IMG,(self.size,self.size))
        self.flagImg = pygame.transform.scale(FLAG_IMG,(self.size,self.size))
        self.incorrectFlagImg = pygame.transform.scale(INCORRECT_FLAG_IMG,(self.size,self.size))
        self.clicked = False
        self.flaged = False
        self.disabled = False
        self.isMine = False
        self.nearMines = 0
        self.nearMinesText = pygame.font.SysFont("monospace", 40, bold=True)

    def CheckForInput(self,mousePos):
        if mousePos[0] in range(self.position[0],self.position[0]+self.size) and mousePos[1] in range(self.position[1],self.position[1]+self.size):
            return True
        return False

    def SetToMine(self):
        self.isMine = True

def FieldClicked(button,win,table,tableSize):
    button.clicked = True
    if(button.isMine):
        gameManager.GameOver(table,win)
    else:
        win.blit(button.emptyImg,(button.position[0],button.position[1]))
        if button.nearMines > 0:
            buttonText = SetNearMinesText(button)
            win.blit(buttonText,(button.position[0]+8,button.position[1]))
        else:
            Burst(button.index, table, win, tableSize)
    
    if gameManager.IsWin(table):
        print("Win")

def SetNearMinesText(button):
    color = (0,0,0)
    if button.nearMines == 1:
        color = (0,0,139)
    elif button.nearMines == 2:
        color = (0,128,0)
    elif button.nearMines == 3:
        color = (200,0,0)
    elif button.nearMines == 4:
        color = (11, 11, 69)
    elif button.nearMines == 5:
        color = (128,0,0)
        
    buttonText = button.nearMinesText.render(str(button.nearMines),1,color)
    return buttonText

def Burst(buttonIndex,table,win,tableSize):
    index = buttonIndex
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            pos = [index[0]+i,index[1]+j]
            if( not (pos[0] < 0 or pos[0] >= tableSize or pos[1] < 0 or pos[1] >= tableSize) and not table[pos[0]][pos[1]].clicked):
                FieldClicked(table[pos[0]][pos[1]], win, table, tableSize)

def SetFlag(button,win):
    if button.flaged:
        button.flaged = False
        win.blit(button.coverImg,(button.position[0],button.position[1]))
    else:
        button.flaged = True
        win.blit(button.flagImg,(button.position[0],button.position[1]))
    