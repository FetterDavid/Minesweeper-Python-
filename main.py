import pygame
import field
import fieldTable
import gameButton
import timer

WIN = pygame.display.set_mode((fieldTable.WIDTH,fieldTable.HEIGHT+fieldTable.BUTTON_SIZE*2))
FPS = 60
pygame.display.set_caption("Minesweeper")
table = fieldTable.CreateTable(fieldTable.tableSize)
gameBtn = gameButton.GameButton(fieldTable.BUTTON_SIZE*1.5,[fieldTable.WIDTH/2-fieldTable.BUTTON_SIZE*1.5/2,fieldTable.BUTTON_SIZE*0.25]) 
myTimer = timer.Timer()

def DrawWindow():
    DrawTable()
    WIN.blit(gameBtn.playImg,(gameBtn.position[0],gameBtn.position[1]))

def DrawTable():
    global table 
    table = fieldTable.CreateTable(fieldTable.tableSize)
    for row in table:
        for button in row:
            WIN.blit(button.coverImg,(button.position[0],button.position[1]))
    pygame.display.update()

def ButtonCheck(clickType):
    for row in table:
        for button in row:
            if button.CheckForInput(pygame.mouse.get_pos()) and not button.disabled:
                if clickType == 1 and not button.flaged:
                    field.FieldClicked(button, WIN, table, fieldTable.tableSize, gameBtn,myTimer)
                elif clickType == 3 and not button.clicked:
                    field.SetFlag(button, WIN)

def main():
    clock = pygame.time.Clock()
    run = True

    DrawWindow()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                    ButtonCheck(event.button)
                    if gameBtn.CheckForInput(pygame.mouse.get_pos()):
                        DrawWindow()
                        myTimer.ResetTimer(WIN)

        myTimer.DrawTime(WIN)
        pygame.display.update()

        

    pygame.quit() 

 
if __name__ == '__main__':
    main()