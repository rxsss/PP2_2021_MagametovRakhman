#Game
import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
turn = True
#Variables
playerX = 0
playerY = 50

#Initialize files
playerImage = pygame.image.load('Materials/Player.png')
enemyImage = pygame.image.load("Materials/Enemy.png")
streetImage = pygame.image.load("Materials/AnimatedStreet.png")
crashSound = pygame.music.load(("Materials/crash.wav"))
backgroundSound = pygame.music.load(("Materials/background.wav"))

#Clock and FPS
clock = pygame.time.Clock()

#Programm start
while turn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            turn = False
                
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_DOWN]: y += 5
    if pressed[pygame.K_UP]: y -= 5
    if pressed[pygame.K_LEFT]: x -= 5
    if pressed[pygame.K_RIGHT]: x += 5
    if y < 0:
        y = 0
    if y > screen.get_height() - 30:
        y = screen.get_height() - 30
    if x < 0:
        x = 0
    if x > screen.get_width() - 30:
        x = screen.get_width() - 30
    pygame.display.flip()
    screen.blit(playerImage, (playerX,playerY))
    screen.fill((255,255,255))
    clock.tick(60)