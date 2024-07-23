import pygame
pygame.init()

WIDTH, HEIGHT = 1200, 745

screen = pygame.display.set_mode((WIDTH, HEIGHT))

black = (0, 0, 0)
white = (255, 255, 255)

level = 5

TITLE = pygame.font.SysFont("Arial", 50, 1, 1)
PARAGRAPH = pygame.font.SysFont("Arial", 25, 1, 1)