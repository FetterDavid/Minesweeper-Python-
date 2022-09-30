import pygame

HEIGHT = 480
WIDTH = 640
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Minesweeper")

def draw():
    pass

def main():
    run = True

    while run:
        for evant in pygame.event.get():
            if evant.type == pygame.QUIT:
                run = False

    pygame.quit() 

 
if __name__ == '__main__':
    main()