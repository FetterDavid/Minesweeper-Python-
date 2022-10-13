import pygame
import time
import os

pygame.font.init()

COVER_IMG = pygame.image.load(os.path.join("Assets","black.png"))

class Timer():

    def __init__(self):
        self.timeText = pygame.font.SysFont("monospace", 40, bold=True)
        self.startTime = time.time()
        self.timeSpent = 0
        self.stoped = False
        self.coverImg = pygame.transform.scale(COVER_IMG,(100,40))


    def DrawTime(self,win):
        if not self.stoped:
            self.timeSpent = int(time.time() - self.startTime)
            buttonText = self.timeText.render(str(self.timeSpent),1,(255,255,255))
            win.blit(self.coverImg,(win.get_size()[0]-100,0))
            win.blit(buttonText,(win.get_size()[0]-100,0))

    def ResetTimer(self,win):
        self.stoped = False

        self.startTime = time.time()
        self.timeSpent = int(time.time() - self.startTime)
        buttonText = self.timeText.render(str(self.timeSpent),1,(255,255,255))
        win.blit(self.coverImg,(win.get_size()))
        win.blit(buttonText,(win.get_size()))
    
    def StopTimer(self):
        self.stoped = True