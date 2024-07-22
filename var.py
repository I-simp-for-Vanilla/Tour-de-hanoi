import pygame
pygame.init()

WIDTH, HEIGHT = 1200, 745

screen = pygame.display.set_mode((WIDTH, HEIGHT))

black = (0, 0, 0)
white = (255, 255, 255)

level = int(input(".\nEnter the number of discs of the tower you want to solve : "))

ARIAL = pygame.font.SysFont("Arial", 25, 1, 1)