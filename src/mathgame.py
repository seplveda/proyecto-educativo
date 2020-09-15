# Setup Python ----------------------------------------------- #
import pygame
from time import sleep
from random import randint
from sys import exit


# logic ------------------------------------------------------ #
def evolve_cell(alive, neighbors):
    return neighbors == 3 or (alive and neighbors == 2)

def count_neighbors(grid, position):
    x,y = position
    neighbour_cells = [(x - 1, y - 1), (x - 1, y + 0), (x - 1, y + 1),
                       (x + 0, y - 1),                 (x + 0, y + 1),
                       (x + 1, y - 1), (x + 1, y + 0), (x + 1, y + 1)]
    count = 0
    for x,y in neighbour_cells:
        if x >= 0 and y >= 0:
            try:
                count += grid[x][y]
            except:
                pass
    return count

def make_empty_grid(x, y):
    grid = []
    for r in range(x):
        row = []
        for c in range(y):
            row.append(0)
        grid.append(row)
    return grid

def make_random_grid(x, y, density):
        grid = []
        for r in range(x):
            row = []
            for c in range(y):
                if (c+r) % density == 0:
                    val = randint(0,1)
                else:
                    val = 0
                row.append(val)
            grid.append(row)
        return grid

def evolve(grid):
    x = len(grid)
    y = len(grid[0])
    new_grid = make_empty_grid(x, y)
    for r in range(x):
        for c in range(y):
            cell = grid[r][c]
            neighbors = count_neighbors(grid, (r, c))
            new_grid[r][c] = 1 if evolve_cell(cell, neighbors) else 0
    return new_grid


def draw_block(x, y, alive_color, block_size):
    x *= block_size
    y *= block_size
    xc  = (x + (block_size // 2))
    yc = (y + (block_size // 2))
    pygame.draw.circle(screen, alive_color, (xc,yc), block_size // 2,0)


def main():
    h = 0
    density = 1
    alive_color = pygame.Color(0,0,0)
    alive_color.hsva = [h, 100, 100]
    xlen = int(maxX / block_size)
    ylen = int(maxY / block_size)
    print("make new random_grid")
    world = make_random_grid(xlen, ylen, density)
    i = 1
    # Loop ------------------------------------------------------- #
    while True:

        if i % iters == 0:
            print("make new random_grid")
            world = make_random_grid(xlen, ylen, density)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                world = make_random_grid(xlen, ylen, density)
                i = 1

        for x in range(xlen):
            for y in range(ylen):
                alive = world[x][y]
                cell_color = alive_color if alive else BLACK
                draw_block(x, y, cell_color, block_size)

        pygame.display.flip()
        h = (h + 2) % 360
        alive_color.hsva = (h, 100, 100)
        world = evolve(world)
        i+=1
        pygame.display.set_caption('iteration: ' + str(i))
        sleep(.05)
        
# Setup Python ----------------------------------------------- #
if __name__ == '__main__':
    pygame.init()
    BLACK = (0, 0, 0)
    maxX = input("Enter max xval (1024): ")
    if maxX == "":
       maxX = 1024
    else:
       maxX = int(maxX)

    maxY = input("Enter max yval (768): ")
    if maxY == "":
        maxY = 768
    else:
        maxY = int(maxY)
    iters = input("Enter number of iterations (200): ")
    if iters == "":
        iters = 500
    else:
        iters = int(iters)

    block_size = input("Enter block size (18): ")
    if block_size == "":
        block_size = 18
    else:
        block_size = int(block_size)

    print("press escape to quit, or return to reset board")
    screen = pygame.display.set_mode((maxX, maxY), 0, 24)
    main()