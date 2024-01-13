import pygame

pygame.init()

BLACK = (0,0,0)
GREY = (128,128,128)
YELLOW = (255,255,0)

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clocl = pygame.time.Clock()