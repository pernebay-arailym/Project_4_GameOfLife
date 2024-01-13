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

clock = pygame.time.Clock()

def draw_grid(positions):
    for position in positions:
        column, row = position
        top_left = (column*TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, BLACK, (*top_left, TILE_SIZE, TILE_SIZE))        

    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))
    for column in range(GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (column * TILE_SIZE, 0), (column * TILE_SIZE, HEIGHT))

def main():
    running = True

    positions = set()
    positions.add((10, 10))
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(YELLOW)
        draw_grid(positions)
        pygame.display.update()
   
   
    pygame.quit()

if __name__ == "__main__":
    main()
