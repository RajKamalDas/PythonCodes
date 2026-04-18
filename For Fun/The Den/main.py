import pygame
from map import DungeonMap
from player import Player
from combatHandler import ConflictHandler


def rgb(hex):
    return tuple(bytes.fromhex(hex.lstrip("#")))


pygame.init()


screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

gameState = "map"

dungeon = DungeonMap()
combat = ConflictHandler()
player = Player()
player.loc = dungeon.getStartLoc()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    eID = 0
    screen.fill(rgb("#2D373A"))

    if gameState == "map":
        dungeon.draw(screen, player.loc)
    elif gameState == "combat":
        combat.draw(screen, player)

    if pygame.mouse.get_just_released()[0]:
        eID, player.loc = dungeon.update(pygame.mouse.get_pos(), player.loc)

    match (eID):
        case 1:
            gameState = "combat"
            # Trigger
        case 2:
            pass
            # Tigger loot
        case 3:
            gameState = "map"
            # Doubles as Win / Comes from combat
        case 4:
            gameState = "loss"
            # Usable since dungeon doesn't return 4 / Comes from combat
        case 5:
            pass
            # propmt for exit

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
