from asyncio import events
import pygame
import button as btn
import random

tableSize = 10
numberOfMine = 10

BUTTON_SIZE = 50
HEIGHT = tableSize*BUTTON_SIZE
WIDTH = tableSize*BUTTON_SIZE
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 60
pygame.display.set_caption("Minesweeper")
table = []

def CreateTable(size):
    y = 0
    for i in range(size):
        x = 0
        row = []
        for j in range(size):
            row.append(btn.Button(size,WIDTH,[x,y],[i,j])) 
            x += WIDTH//tableSize
        y += HEIGHT//tableSize  
        table.append(row)
    
    #Plant mines
    mines = []
    while len(mines) < numberOfMine:
        mPos = [random.randint(0,tableSize-1),random.randint(0,tableSize-1)]
        if(not table[mPos[0]][mPos[1]].isMine):
            table[mPos[0]][mPos[1]].SetToMine()
            mines.append( table[mPos[0]][mPos[1]])
    
    #Set helping numbers
    for mine in mines:
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                pos = [mine.index[0]+i,mine.index[1]+j]
                if( not (pos[0] < 0 or pos[0] >= size or pos[1] < 0 or pos[1] >= size) and not table[pos[0]][pos[1]].isMine):
                    table[pos[0]][pos[1]].nearMines += 1


def DrawTable():
    CreateTable(tableSize)
    
    for row in table:
        for button in row:
            WIN.blit(button.coverImg,(button.position[0],button.position[1]))

    pygame.display.update()

def ButtonCheck(clickType):
    for row in table:
        for button in row:
            if button.CheckForInput(pygame.mouse.get_pos()):
                if clickType == 1:
                     ButtonClicked(button)
                elif clickType == 3:
                    SetFlag(button)

def Burst(buttonIndex):
    index = buttonIndex
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            pos = [index[0]+i,index[1]+j]
            if( not (pos[0] < 0 or pos[0] >= tableSize or pos[1] < 0 or pos[1] >= tableSize) and not table[pos[0]][pos[1]].clicked):
                    ButtonClicked(table[pos[0]][pos[1]])

def ButtonClicked(button):
    button.clicked = True
    if(button.isMine):
        WIN.blit(button.mineImg,(button.position[0],button.position[1]))
    else:
        WIN.blit(button.emptyImg,(button.position[0],button.position[1]))
        if button.nearMines > 0:
            buttonText = button.nearMinesText.render(str(button.nearMines),1,(0,0,0))
            WIN.blit(buttonText,(button.position[0]+10,button.position[1]))
        else:
            Burst(button.index)

def SetFlag(button):
     WIN.blit(button.flagImg,(button.position[0],button.position[1]))

def main():
    clock = pygame.time.Clock()
    run = True
    DrawTable()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                    ButtonCheck(event.button)

        pygame.display.update()

        

    pygame.quit() 

 
if __name__ == '__main__':
    main()