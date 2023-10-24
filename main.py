import pygame
import sys
import random

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 4
TILE_SIZE = WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sliding Tile Puzzle")

# Create the puzzle grid
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Shuffle the tiles
numbers = list(range(1, GRID_SIZE**2))
random.shuffle(numbers)

for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        number = grid[row][col]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # Implement the logic to move tiles up
                pass
            elif event.key == pygame.K_DOWN:
                # Implement the logic to move tiles down
                pass
            elif event.key == pygame.K_LEFT:
                # Implement the logic to move tiles left
                pass
            elif event.key == pygame.K_RIGHT:
                # Implement the logic to move tiles right
                pass

    # Clear the screen
    screen.fill(WHITE)

    # Draw the grid with numbers
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            number = grid[row][col]
            if number > 0:
                pygame.draw.rect(screen, (0, 0, 0), (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                font = pygame.font.Font(None, 36)
                text = font.render(str(number), True, (255, 255, 255))
                screen.blit(text, (col * TILE_SIZE + TILE_SIZE//3, row * TILE_SIZE + TILE_SIZE//3))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
