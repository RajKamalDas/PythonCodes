import pygame

# pygame setup
pygame.init()

WIDTH = 1280
HEIGHT = 720
CELL_WIDTH = 20
CELL_HEIGHT = 20

grid = [[False for i in range(WIDTH // CELL_WIDTH)] for j in range(HEIGHT // CELL_HEIGHT)]
gridColour = "black"
gridLineColour = "white"
cellColour = "#00D277"
runSim = False
simSpeed = 200
lastSim = 200

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True


def simulate():
    global grid
    newGrid = [row.copy() for row in grid]

    for y in range(HEIGHT // CELL_HEIGHT):
        for x in range(WIDTH // CELL_WIDTH):
            count = 0
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    if (
                        (i == 0 and j == 0)
                        or (x + j == -1)
                        or (x + j == WIDTH // CELL_WIDTH)
                        or (y + i == -1)
                        or (y + i == HEIGHT // CELL_HEIGHT)
                    ):
                        continue
                    if grid[y + i][x + j]:
                        # print(i, j, end=" ")
                        count += 1
            if newGrid[y][x] == False and count == 3:
                newGrid[y][x] = True
                # print("Born: ", x, y, '|', count)
            elif newGrid[y][x] == True and (count == 3 or count == 2):
                newGrid[y][x] = True
                # print("live: ", x, y, '|', count)
            else:
                newGrid[y][x] = False
                # print("die: ", x, y, '|', count)
    # print("-------------")
    grid = newGrid


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(gridColour)

    for x in range(CELL_WIDTH, WIDTH, CELL_WIDTH):
        pygame.draw.line(screen, gridLineColour, (x, 0), (x, HEIGHT))
    for y in range(CELL_HEIGHT, HEIGHT, CELL_HEIGHT):
        pygame.draw.line(screen, gridLineColour, (0, y), (WIDTH, y))

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(
                    screen, cellColour, (x * CELL_WIDTH + 1, y * CELL_HEIGHT + 1, CELL_WIDTH - 1, CELL_HEIGHT - 1)
                )

    leftClick, _, rightClick = pygame.mouse.get_pressed()
    middleClick = pygame.mouse.get_just_released()[1]

    if leftClick:
        mouseX, mouseY = pygame.mouse.get_pos()
        grid[mouseY // CELL_HEIGHT][mouseX // CELL_WIDTH] = True

    if rightClick:
        mouseX, mouseY = pygame.mouse.get_pos()
        grid[mouseY // CELL_HEIGHT][mouseX // CELL_WIDTH] = False

    if middleClick:
        runSim = not runSim
        gridColour = "#505051" if runSim else "black"
        gridLineColour = "#F17070" if runSim else "white"
        cellColour = "#4BF1A9" if runSim else "#00D277"

    if runSim:
        if lastSim >= simSpeed:
            simulate()
            lastSim = 0
        else:
            lastSim += clock.get_time()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)

pygame.quit()
