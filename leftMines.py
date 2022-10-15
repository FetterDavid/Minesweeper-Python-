import pygame
import os

pygame.font.init()

COVER_IMG = pygame.image.load(os.path.join("Assets","black.png"))
MINE_IMG = pygame.image.load(os.path.join("Assets","mineIcon.png"))

class LeftMines():

    def __init__(self,mineAmount):
        self.mineText = pygame.font.SysFont("monospace", 40, bold=True)
        self.leftMine = mineAmount
        self.coverImg = pygame.transform.scale(COVER_IMG,(80,40))
        self.mineImg = pygame.transform.scale(MINE_IMG,(40,40))


    def DrawLeftMines(self,win,type):
        # Type: 0 - stay ; 1 - add mine ; -2 -remove mine
        self.leftMine+=type
        buttonText = self.mineText.render(str(self.leftMine),1,(255,0,0))
        win.blit(self.coverImg,(0,20))
        win.blit(self.mineImg,(85,20))
        win.blit(buttonText,(14,20))

    def ResetLeftMines(self,win,mineAmount):
        self.leftMine=mineAmount
        buttonText = self.mineText.render(str(self.leftMine),1,(255,0,0))
        win.blit(self.coverImg,(0,20))
        win.blit(buttonText,(14,20))