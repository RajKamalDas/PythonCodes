import pygame
import random


def rgb(hex):
    return tuple(bytes.fromhex(hex.lstrip("#")))


class DungeonMap:
    def __init__(self, gridSize=8, weights=[50, 30]):
        self.height = 640
        self.gridSize = gridSize
        self.cellSize = self.height // gridSize
        self.grid = [[False for cell in range(gridSize)] for row in range(gridSize)]
        self.offse = -11

        def rand():
            roll = random.randint(1, 100)
            if roll < weights[0]:
                return 0
            elif roll < sum(weights[:2]):
                return 1
            else:
                return 2

        bagOfEvents = [5, 4] + [rand() for cell in range((gridSize * gridSize - 2))]
        random.shuffle(bagOfEvents)
        self.events = [
            [bagOfEvents[row * gridSize + cell] for cell in range(gridSize)]
            for row in range(gridSize)
        ]
        self.startPos = (bagOfEvents.index(4) % gridSize, bagOfEvents.index(4) // gridSize)
        self.grid[self.startPos[1]][self.startPos[0]] = True

    def getStartLoc(self):
        return self.startPos

    def draw(self, screen, playerLoc):
        self.offset = (screen.height - self.height) // 2

        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if not cell:
                    pygame.draw.rect(
                        screen,
                        rgb("#C9C9C9"),
                        (
                            self.offset + self.cellSize * j,
                            self.offset + self.cellSize * i,
                            self.cellSize,
                            self.cellSize,
                        ),
                    )
                elif self.events[i][j] == 5:
                    pygame.draw.rect(
                        screen,
                        "green",
                        (
                            self.offset + self.cellSize * j + 15,
                            self.offset + self.cellSize * i + 10,
                            self.cellSize - 30,
                            self.cellSize - 20,
                        ),
                    )

        pygame.draw.circle(
            screen,
            "White",
            (
                self.offset + self.cellSize * playerLoc[0] + self.cellSize // 2,
                self.offset + self.cellSize * playerLoc[1] + self.cellSize // 2,
            ),
            10,
        )

        for i in range(self.gridSize + 1):
            pygame.draw.line(
                screen,
                "white",
                (self.offset + self.cellSize * i, self.offset),
                (self.offset + self.cellSize * i, self.offset + self.height),
                3,
            )
            pygame.draw.line(
                screen,
                "white",
                (self.offset, self.offset + self.cellSize * i),
                (self.offset + self.height, self.offset + self.cellSize * i),
                3,
            )

    def update(self, pos, playerLoc):
        if self.offset == -11:
            return 0, playerLoc

        x, y = pos
        x = (x - self.offset) // self.cellSize
        y = (y - self.offset) // self.cellSize

        if not (0 <= x < self.gridSize and 0 <= y < self.gridSize):
            return 0, playerLoc
        if abs(playerLoc[0] - x) + abs(playerLoc[1] - y) != 1:
            return 0, playerLoc

        if self.grid[y][x] and self.events[y][x] != 5:
            ambush = 0 if random.random() > 0.3 else 1
            return ambush, (x, y)

        self.grid[y][x] = True
        return self.events[y][x], (x, y)
