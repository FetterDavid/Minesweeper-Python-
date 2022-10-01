import random
import field

tableSize = 15
numberOfMine = 30

BUTTON_SIZE = 50
HEIGHT = tableSize*BUTTON_SIZE
WIDTH = tableSize*BUTTON_SIZE

def CreateTable(size):
    table = []
    y = 0
    for i in range(size):
        x = 0
        row = []
        for j in range(size):
            row.append(field.Button(size,WIDTH,[x,y],[i,j])) 
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

    return table