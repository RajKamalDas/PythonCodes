import pygame
import random


def rgb(hex):
    return tuple(bytes.fromhex(hex.lstrip("#")))


class ConflictHandler:
    def __init__(self):
        self.enemies = [random.randint(0, 2) for i in range(random.randint(2, 5))]
        # Create Enemy Function ↑ later
        self.offset = 40
        self.border = {
            "width": 5,
            "color": rgb("#C73F53"),
            "rect": (self.offset, self.offset, 640, 640),
        }

    def draw(self, screen, player, font=("Arial", 30), inv=False):
        pygame.draw.rect(screen, "white", (self.offset, self.offset + 500, 140, 140), width=3)
        pygame.draw.line(
            screen,
            "white",
            (self.offset, self.offset + 500),
            (self.offset + 637, self.offset + 500),
            3,
        )
        font = pygame.font.SysFont(*font)
        screen.blit(
            font.render(player.name, False, "white"), (self.offset + 150, self.offset + 510)
        )
        health = player.curHP / player.stats[0]
        pygame.draw.rect(
            screen,
            rgb("#3EE649"),
            (self.offset + 150, self.offset + 550, 350 * health, 30),
        )
        pygame.draw.rect(screen, "white", (self.offset + 150, self.offset + 550, 350, 30), 5)

        sanity = player.curSanity / player.stats[2]
        pygame.draw.rect(
            screen,
            rgb("#1D77DE"),
            (self.offset + 150, self.offset + 590, 350 * sanity, 30),
        )
        pygame.draw.rect(screen, "white", (self.offset + 150, self.offset + 590, 350, 30), 5)
        pygame.draw.rect(screen, **self.border)
