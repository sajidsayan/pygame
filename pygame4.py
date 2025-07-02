import pygame
import sys
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rectangle with pygame")

BLACK = (0, 0, 0)
RED = (255, 0, 55)

RECT_X = 100
RECT_Y = 100
RECT_WIDTH = 50
RECT_HEIGHT = 50

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, RED, (RECT_X, RECT_Y, RECT_WIDTH, RECT_HEIGHT))
    pygame.display.update()

pygame.quit()
