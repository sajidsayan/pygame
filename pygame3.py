import pygame
import sys
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Circle with pygame")
BLACK = (0, 0, 0)
CYAN = (7, 154, 227)
CIR_X = 100
CIR_Y = 100
CIR_RADIUS = 25

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.circle(screen, CYAN, (CIR_X, CIR_Y), CIR_RADIUS)
    pygame.display.update()

pygame.quit()
