import pygame
import sys

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Circle, Square, Rectangle with Pygame")

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

CIRCLE_POSITION = (150, 200)
CIRCLE_RADIUS = 40

SQUARE_POSITION = (275, 160)
SQUARE_SIZE = 80

RECT_POSITION = (420, 150)
RECT_WIDTH = 120
RECT_HEIGHT = 60

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.circle(screen, BLUE, CIRCLE_POSITION, CIRCLE_RADIUS)
    pygame.draw.rect(screen, RED, (SQUARE_POSITION[0], SQUARE_POSITION[1], SQUARE_SIZE, SQUARE_SIZE))
    pygame.draw.rect(screen, GREEN, (RECT_POSITION[0], RECT_POSITION[1], RECT_WIDTH, RECT_HEIGHT))

    pygame.display.update()

pygame.quit()
sys.exit()
