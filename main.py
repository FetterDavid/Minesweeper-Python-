import pygame
import button

tableSize = 15

HEIGHT = tableSize*50
WIDTH = tableSize*50
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 60
pygame.display.set_caption("Minesweeper")

def createTable(size):
    table = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(button.Button(size,WIDTH)) 
        table.append(row)

    return table

def drawTable():
    table = createTable(tableSize)
    
    y = 0
    for row in table:
        x = 0
        for button in row:
            print(x)
            WIN.blit(button.images,(x,y))
            x += WIDTH//tableSize
        y += HEIGHT//tableSize  

    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    drawTable()

    while run:
        clock.tick(FPS)
        for evant in pygame.event.get():
            if evant.type == pygame.QUIT:
                run = False

    pygame.quit() 

 
if __name__ == '__main__':
    main()