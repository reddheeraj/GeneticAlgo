import pygame

pygame.init()


from math import sin
from math import cos
from math import radians

font = pygame.font.Font(None, 30)

# --- FUNCTIONS ----------------------------------------------------------------+


def plot_organism(x1, y1, theta, screen):
    radius = 10
    pygame.draw.circle(screen, (0, 100, 0), (x1, y1), radius)
    pygame.draw.circle(screen, (144, 238, 144), (x1, y1), radius - 3)
    tail_len = 12
    x2 = cos(radians(theta)) * tail_len + x1
    y2 = sin(radians(theta)) * tail_len + y1
    pygame.draw.line(screen, (0, 100, 0), (x1, y1), (x2, y2), 2)


def plot_food(x1, y1, screen):
    radius = 7
    pygame.draw.circle(screen, (72, 61, 139), (x1, y1), radius)
    pygame.draw.circle(screen, (123, 104, 238), (x1, y1), radius - 3)
