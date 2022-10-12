import fieldTable
import pygame
import gameButton
import timer

def IsWin(table):
    for row in table:
        for field in row:
            if not field.clicked and not field.isMine:
                return False
    
    return True

def GameOver(table,win,gameBtn,myTimer):
    for row in table:
        for field in row:
            field.disabled = True
            if field.isMine and not field.flaged:
                win.blit(field.mineImg,(field.position[0],field.position[1]))
            if not field.isMine and field.flaged:
                win.blit(field.incorrectFlagImg,(field.position[0],field.position[1]))

    myTimer.StopTimer()
    win.blit(gameBtn.deadImg,(gameBtn.position[0],gameBtn.position[1]))
