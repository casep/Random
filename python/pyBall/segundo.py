#!/bin/python
#Programa de Carlos "casep" Sepulveda
#Casep, 20130629, Version 1
#casep@fedoraproject.org
#

from pygame import *

ballpic = image.load('ball.png')

listo = False

ballx = 0	
bally = 0
ballxmove = 5
ballymove = 1

init()					
screen = display.set_mode((640, 480))	
display.set_caption('Juego de pelota')	

while listo == False:
    screen.fill(0)	
    screen.blit(ballpic, (ballx, bally))
    display.update()
    
    time.delay(5)

    ballx = ballx + ballxmove
    bally = bally + ballymove

    if ballx > 600:
        ballxmove = -5
    if ballx < 0:
        ballxmove = 5
    if bally > 440:
        ballymove = -1
    if bally < 0:
        ballymove = 1
    
    for e in event.get():
        if e.type == KEYUP:
            if e.key == K_ESCAPE:
                listo = True










