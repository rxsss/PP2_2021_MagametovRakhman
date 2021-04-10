#Game
import pygame
import random
import time
import sys
import os
pygame.init()


#Initialize files
playerImage = pygame.image.load('./materials/Player.png')
playerWidth = playerImage.get_width()
playerHeight = playerImage.get_height()
enemyImage = pygame.image.load("./materials/Enemy.png")
enemyWidth = enemyImage.get_width()
enemyHeight = enemyImage.get_height()
streetImage = pygame.image.load("./materials/AnimatedStreet.png")
streetWidth = streetImage.get_width()
streetHeight = streetImage.get_height()


#main Settings
screen = pygame.display.set_mode((streetWidth, streetHeight))
pygame.display.set_caption("My first game")


#Booleans
repeatMusic = True
turn = True


#Variables
step = 5
score = 0

playerX = 0
playerY = streetHeight - playerHeight - 15

enemyX = random.randint(40, streetWidth - enemyWidth - 40)
enemyY = 0 - enemyHeight

#Texts
font = pygame.font.SysFont("Helvetica", 60)
smallFont = pygame.font.SysFont("Helvetica", 30)
gameOver = font.render("Game Over", True, (0,0,0))



#Clock and FPS
FPS = 60
clock = pygame.time.Clock()


#Functions
def enemyMove(x,y):
    global enemyY
    global enemyX
    global score
    global step
    if enemyY > streetHeight + enemyHeight:
        enemyY = 0 - enemyHeight
        enemyX = random.randint(40, streetWidth - enemyWidth - 40)
        score += 1
        step = random.randint(2,5)
    screen.blit(enemyImage,(x, y))
    enemyY += (step*2)
def showScore(x,y):
    scoreText = smallFont.render("Score: " + str(score), True, (0,0,255))
    screen.blit(scoreText, (x,y))
def isCrash(x,y,xx,yy):
    if (x in range(xx + 1, xx + enemyImage.get_width() - 1)) and (y in range(yy + 1, yy + enemyImage.get_height() - 1)):
        return True
    elif (xx in range(x + 1, x + playerImage.get_width() - 1)) and (yy in range(y + 1, y + playerImage.get_height() - 1)):
        return True
    
#Programm start
while turn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            turn = False
    #Turning music
    if repeatMusic:
        pygame.mixer.Sound('./materials/background.wav').play()
        repeatMusic = False
    #Pressed keys
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: playerX -= 5
    if pressed[pygame.K_RIGHT]: playerX += 5
    if playerX < 0:
        playerX = 0
    if playerX > screen.get_width() - playerImage.get_width():
        playerX = screen.get_width() - playerImage.get_width()
    #crash
    if isCrash(playerX, playerY, enemyX, enemyY):
        pygame.mixer.Sound('./materials/crash.wav').play()
        time.sleep(1)
        screen.fill((255,0,0))
        screen.blit(gameOver,((screen.get_width() - gameOver.get_width())/2, (screen.get_height() - gameOver.get_height())/2))
        pygame.display.flip()
        time.sleep(5)
        pygame.quit()
        sys.exit()
    
    #MARK: - Final 
    pygame.display.flip()
    screen.blit(streetImage, (0,0))
    enemyMove(enemyX,enemyY)
    showScore(200,5)
    screen.blit(playerImage, (playerX, playerY))
    clock.tick(FPS)