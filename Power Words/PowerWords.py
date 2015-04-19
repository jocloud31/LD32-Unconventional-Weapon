'''
Created on Apr 18, 2015

@author: Jay
'''
import pygame
import random
import sys

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))

gameRun = True
heroXPos = 100
heroYPos = 85
heroMove = 0
clock = pygame.time.Clock()
moveLeft = False
moveRight = False

while gameRun:
    windowSizeX,windowSizeY = gameDisplay.get_size()
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRun = False
            
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                gameRun = False
            
            if key[pygame.K_a]:
                moveLeft = True
            
            if key[pygame.K_d]:
                moveRight = True 
 
            if key[pygame.K_F12]:
                print windowSizeX
                print windowSizeY           
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moveLeft = False
            if event.key == pygame.K_d:
                moveRight = False   
                

    if moveLeft:
        heroMove -= .1
    if moveRight:
        heroMove += .1
    
    if not moveLeft and not moveRight:
        heroMove = 0
    
    if heroMove > 5:
        heroMove = 5
    if heroMove < -5:
        heroMove = -5
        
    heroXPos += heroMove        
    gameDisplay.fill((55,100,255))
    pygame.draw.rect(gameDisplay, (35,200,15), [0, windowSizeY-50, windowSizeX, 50])
    pygame.draw.rect(gameDisplay, (0,0,0), [heroXPos, windowSizeY-85, 35, 35])
    pygame.display.update()
    clock.tick(60)
    

pygame.quit()
quit