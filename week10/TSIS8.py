#Game
import pygame
import random
import time
import sys
pygame.init()


#Initialize files
playerImage = pygame.image.load('./materials/Player.png')
enemyImage = pygame.image.load("./materials/Enemy.png")
streetImage = pygame.image.load("./materials/AnimatedStreet.png")


#main Settings
screen = pygame.display.set_mode((streetImage.get_width(), streetImage.get_height()))
pygame.display.set_caption("My first game")
turn = True


#Variables
step = 5
score = 0

playerX = 0
playerY = screen.get_height() - playerImage.get_height() - 15

enemyX = random.randint(40, screen.get_width() - enemyImage.get_width() - 40)
enemyY = 0 - enemyImage.get_height()

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
    if enemyY > screen.get_height() + enemyImage.get_height():
        enemyY = 0
        enemyX = random.randint(40, screen.get_width() - enemyImage.get_width() - 40)
        score += 1
    screen.blit(enemyImage,(x, y))
    enemyY += step
def showScore(x,y):
    scoreText = smallFont.render("Score: " + str(score), True, (0,0,255))
    screen.blit(scoreText, (x,y))

#Crash
def isCrash(x,y,xx,yy):
    if (x in range(xx, xx + enemyImage.get_width())) and (y in range(yy, yy + enemyImage.get_height())):
        return True
    elif (xx in range(x, x + playerImage.get_width())) and (yy in range(y, y + playerImage.get_height())):
        return True
    
#Programm start
while turn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            turn = False
    #Pressed keys
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: playerX -= step
    if pressed[pygame.K_RIGHT]: playerX += step
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
    pygame.display.flip()
    screen.blit(streetImage, (0,0))
    enemyMove(enemyX,enemyY)
    showScore(200,5)
    screen.blit(playerImage, (playerX, playerY))
    clock.tick(FPS)