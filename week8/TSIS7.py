#Game
import pygame
pygame.init()

screen = pygame.display.set_mode((400, 300))
turn = True
x = 30
y = 30
while turn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            turn = False
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_DOWN]: y += 5
        if pressed[pygame.K_UP]: y -= 5
        if pressed[pygame.K_LEFT]: x -= 5
        if pressed[pygame.K_RIGHT]: x += 5
    pygame.display.flip()
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, 30, 30))
