import pygame
import field
import fieldTable


WIN = pygame.display.set_mode((fieldTable.WIDTH,fieldTable.HEIGHT))
FPS = 60
pygame.display.set_caption("Minesweeper")
table = fieldTable.CreateTable(fieldTable.tableSize)


def DrawTable():
    print(len(table))
    for row in table:
        for button in row:
            WIN.blit(button.coverImg,(button.position[0],button.position[1]))
    pygame.display.update()

def ButtonCheck(clickType):
    for row in table:
        for button in row:
            if button.CheckForInput(pygame.mouse.get_pos()):
                if clickType == 1 and not button.flaged:
                    field.FieldClicked(button, WIN, table, fieldTable.tableSize)
                elif clickType == 3 and not button.clicked:
                    field.SetFlag(button, WIN)

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