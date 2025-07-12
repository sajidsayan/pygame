import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom Event Example")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

sprite1 = pygame.Rect(100, 150, 100, 100)
sprite2 = pygame.Rect(400, 150, 100, 100)

color1 = RED
color2 = BLUE

COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(COLOR_CHANGE_EVENT, 2000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == COLOR_CHANGE_EVENT:
            color1 = GREEN if color1 == RED else RED
            color2 = YELLOW if color2 == BLUE else BLUE

    screen.fill(WHITE)
    pygame.draw.rect(screen, color1, sprite1)
    pygame.draw.rect(screen, color2, sprite2)
    pygame.display.flip()

pygame.quit()
sys.exit()
