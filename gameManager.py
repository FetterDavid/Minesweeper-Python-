from datetime import datetime
import fieldTable
import pygame
import gameButton
import timer

def IsWin(table,myTimer):
    for row in table:
        for field in row:
            if not field.clicked and not field.isMine:
                return False
    
    SaveProgress({ "WIN":True, "time":myTimer.timeSpent, "date":datetime.now().strftime("%Y %m %d %H %M")})
    myTimer.StopTimer()
    return True

def GameOver(table,win,gameBtn,myTimer):
    for row in table:
        for field in row:
            field.disabled = True
            if field.isMine and not field.flaged:
                win.blit(field.mineImg,(field.position[0],field.position[1]))
            if not field.isMine and field.flaged:
                win.blit(field.incorrectFlagImg,(field.position[0],field.position[1]))

    win.blit(gameBtn.deadImg,(gameBtn.position[0],gameBtn.position[1]))

    SaveProgress({ "WIN":False, "time":myTimer.timeSpent, "date":datetime.now().strftime("%Y.%m.%d %H:%M")})
    myTimer.StopTimer()

def SaveProgress(progress):
    with open('data.txt', 'a') as f:
        f.write(str(progress)+"\n")
